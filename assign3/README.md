# Assignment 3: Wallscraper

## Congratulations!

Congratulations on completing Week 6! Midterm season is almost over, and we've basically finished discussing the syntax of the Python language. At this point, you know most of the important stuff about the language itself. Therefore, we'll spend most of the rest of the time in class going over useful builtin- or third-party modules that are omnipresent in the Python ecosystem. However, as far as the language itself goes, you have all become skilled in the art of the Python language.

## Overview

Sigh... another CS41 lab day and boring assignment. Better open up reddit and see what's new on /r/funny.

**PSYCH IT'S THE MOST AMAZING LAB EVER.**

And while you're at it, you really need a new desktop background wallpaper. So, head on over to /r/wallpapers, or maybe /r/wallpaper. If you're feeling up for it, even /r/earthporn and /r/spaceporn.

Generally, these labs have focused on exploring nuances of the Python language - whether the syntax, semantics, or style of thinking. However, since we've know almost wrapped up talking about the language, labs will become a period of time for you to build something awesome.

In particular, today you will write a program that automatically downloads the top wallpaper from reddit every night to your local computer, and optionally sets it as your desktop background. So cool!

## Getting Set Up

While Python's standard library has a lot of functionality included, we sometimes prefer to work with third-party packages. For this project, we're going to primarily use `requests`, a fantastic web client for Python written by Kenneth Reitz.

### Installing Required Packages

As always, the first step is installing any required packages using `pip`. At the very least, you should ensure that `requests` and `Pillow` are installed inside your virtual environment:

```
$ # Activate your virtual environment
(cs41)$ pip install requests
(cs41)$ pip install Pillow
```

You are free to install any other third-party libraries you think will be useful. In particular, `awesome-slugify` can be used to normalize possibly complicated filenames.

Our solution also uses the `os`, `sys`, `io`, `subprocess`, `pathlib`, `imghdr`, and `mimetypes` packages from the standard library, if you're looking for possibly useful builtin tools.

### Check Installations
To ensure that you've successfully installed requests, enter an interactive session and check:

```
(cs41)$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from PIL import Image
>>>
```

If you get back the interactive prompt `>>>`, everything is installed correctly! If, on the other hand, you get an `ImportError` - please let one of the course staff know.

## Wallscraper Specification

The internet is full of many awesome things: [cat videos](https://www.youtube.com/v/2XID_W4neJo), [the most awesome person in the world](https://www.facebook.com/), and most importantly, [reddit](https://www.reddit.com/r/python).

Take a (brief) look at [reddit.com/r/wallpapers](https://www.reddit.com/r/wallpapers) - there is so much happening on the page. Images are dynamically loaded, buttons ask you to click them, ads on the side demand your attention - it can be hard to find the data, and although we could use something like `BeautifulSoup` to parse all this junk, it seems too complicated to be worth it.

On the other hand, take a (long) look at [reddit.com/r/wallpapers.json](https://www.reddit.com/r/wallpapers.json) (note the suffix `.json`). By adding this suffix to the query, we get back a rich data structure representing, in this case, posts on /r/wallpapers.

### Overview

At a high level, you will need to extract a list of the top posts from a subreddit, and for each of the posts, download the linked image if it represents a (SFW) image.

### Aside: Using `requests`

In this section, we'll explore some of the functionality of the `requests` module, which will be quite useful for this assignment. You can skip this if you already know how `requests` works.

A sample usage of the `requests` package is shown below.

```
>>> import requests
>>> response = requests.get('http://stanfordpython.com')
>>> print(response)
<Response [200]>
>>> print(type(response))
<class 'requests.models.Response'>
```

The `requests.get` function returns a `Response` object that represents the response returned by the server, in this case by `stanfordpython.com`. (There are similar `post`, `put`, `patch`, and `delete` functions defined by `requests`).

A `Response` instance supports a lot of attribute references:

```
>>> response.<tab>
response.apparent_encoding      response.history                response.raise_for_status
response.close                  response.is_permanent_redirect  response.raw
response.connection             response.is_redirect            response.reason
response.content                response.iter_content           response.request
response.cookies                response.iter_lines             response.status_code
response.elapsed                response.json                   response.text
response.encoding               response.links                  response.url
response.headers                response.ok
```

For the purposes of this assignment, we only care about a few of them:

```
# true iff the request to the server was successful
response.ok

# the raw server response, as a bytestring
response.content

# return a python dictionary of the response data, if the data represents JSON-encoded data, otherwise raise an Exception
response.json()
```

More information on the `requests` library can be found [here](http://docs.python-requests.org/en/latest/)

### Query Subreddit Data

In this section, your task is to write a function `query` that accepts as an argument a subreddit to query (e.g. `'wallpapers'` or `'funny+gifs'`), and returns the JSON server response from reddit as a Python dictionary. You can add any additional positional or keyword arguments as you see fit.

Your function should gracefully handle all of the following scenarios:

* There is no internet connection
* The user supplies a string that doesn't represent a valid subreddit
* The requests module, in particular the `get` function, throws any exception from `requests.exceptions` (hint: look through [the source code](https://github.com/kennethreitz/requests/blob/master/requests/exceptions.py) to find the base exception class for the `requests` package.)
* reddit responds with a status that is not `ok`

In all of these situations, your `query` function should print out an informative error message.

To test this function, write a few lines of code with a reasonable subreddit, and compute the number of posts with a score greater than 500.

#### Note: Rate Limits

Reddit imposes a rate limit on generic scripts that make too many requests to its server (default is >30 per minute). If your script is getting rate-limited, Reddit will respond with a `<Response [429]>`, which specifically means: *429 Client Error: Too Many Requests.*

To avoid this problem, we need to tell Reddit that we're not just some random script by adding a `User-Agent` to our request. In particular, you need to add `headers={'User-Agent': <unique_identifier>}` as a keyword argument to `requests.get`.

For instance, I would use 

```
requests.get(
    'http://www.website.com', 
    headers={'User-Agent': 'Wallscraper Script by sredmond'}
)
```

This should get around the rate-limit problem.


### Building a `RedditPost` Class

Next, you should build a `RedditPost` class that represents a single post.

A RedditPost object must support two methods, and can support as many helper functions as you see fit.

* `__init__(self, data)`: Initialize a RedditPost from a JSON dictionary representing the post, as extracted from the top-level subreddit JSON.
* `download(self)`: Tries to download the Reddit post. Must determine (1) if the post can be downloaded, (2) where to download the post, and (3) actually download the post.

For now, let's focus on the constructor. As discussed in the data model section, there are lots of irrelevant attributes in the JSON returned by the subreddit.

Write the `__init__` method, and only keep the attributes that correspond to an attribute you think will be useful. If an attribute is missing or the data is otherwise corrupted, your program should handle the error gracefully.

Additionally, you can implement the magic method `__str__(self)` to return a string representing a human-readable form of a post, allowing us to more easily debug when printing a `RedditPost` to the console. We suggest printing the posts in the following format: `"{title} ({score}): {url}"`.

### Load Response Data into Post Objects

Write the code to convert the data returned by `query` into a list of `RedditPost` objects. You can accomplish this in one line using a list comprehension. As a sanity check, your list of `RedditPost`s should have length 25 (or perhaps 26 or 27).

If the data is bad - i.e. keys are missing, information is not structured as you suspect, etc. - your program should not crash. Rather, it should gracefully handle the errors and proceed accordingly. Who's responsibility is it to check for malformed data?

At this point, rewrite your old code to determine the number of posts with a score greater than 500. This should also take one line of code.

### Download an Image Post

Ultimately, our goal is to download wallpapers. Implement the `download(self)` method in the `RedditPost` class that attempts to download the post. 

If the post doesn't represent an image, don't download anything. How can you tell if the post represents an image? You can look at the `url` - does it end with `'.jpg'`,`'.png'`. or any other image suffix? Is `is_self` `True` or `False`? Is `post_hint` `image`, `link`, or something else? Is the domain something recognizable like `'i.imgur.com'`?

You can add any other conditions you'd like on the downloaded wallpapers - perhaps you only download images from imgur, or only wallpapers with a score over 500, or only gilded posts.

Where do you download the file to? Use the aspect ratio and width/height to store the download in a structured place. For example, if an image is 1920 by 1080, store it in `wallpapers/16x9/1920x1080/image.png`. How can you title the file? For one, you can use the title of the post. However, sometimes Reddit posts have titles that aren't amenable to filesystems, so you should probably slugify the title in some way. Furthermore, most titles have something like `'[1920x1080]'` in the title. You should use a regular expression to detect and remove anything that looks like that, possibly using `re.sub`.

Hint: if you're writing image data to an open file object, make sure that the file has been opened with `wb` flags for (w)riting in (b)inary mode. Generally, when reading or writing binary data like images or sound files, it's a good idea to use the `'b'` option.

Test this method by downloading one of the posts.

If you have successfully downloaded a photo, congratulations! That's pretty dang impressive.


### Tying Everything Together

Ultimately, the goal of this step is to combine all of the pieces you've already written to complete the final project.

Write the code to take the list of posts generated earlier, and download them all to your filesystem. Cool!

## Data Model

Building this wallpaper scraper involves scraping structured data from Reddit. How exactly is this data structured?

### Top-Level Subreddit Data - `listing`

The data returned by a subreddit is a `listing` object, which is used to paginate content that is too long to display in one go.

```
{'data': {'after': 't3_4if6xu',
          'before': None,
          'children': [array of Things],
          'modhash': ''},
 'kind': 'Listing'}
```

Where `'children'` is a list of `Thing`s (the real Reddit name for this data model!)

If you want to get the previous or next page, supply a query argument `before` or `after` with the value, usually used in conjunction with `count`.

### Intermediate Storage - `Thing`

A `Thing`, for our purposes, looks like the following:

```
{
    'data': Post,
    'kind': 't3'
}
```

where the only important field, `'data'`, contains a single `Post` object.

### Reddit Post - `Post`

The most important data model to understand is that of a Reddit post. In it's entirety, a post looks like:

```
{
    'approved_by': None,
    'archived': True,
    'author': 'onewallpaperaweek',
    'author_flair_css_class': None,
    'author_flair_text': None,
    'banned_by': None,
    'clicked': False,
    'created': 1431645046.0,
    'created_utc': 1431616246.0,
    'distinguished': None,
    'domain': 'i.imgur.com',
    'downs': 0,
    'edited': False,
    'from': None,
    'from_id': None,
    'from_kind': None,
    'gilded': 0,
    'hidden': False,
    'hide_score': False,
    'id': '35ybkb',
    'is_self': False,
    'likes': None,
    'link_flair_css_class': None,
    'link_flair_text': None,
    'locked': False,
    'media': None,
    'media_embed': {},
    'mod_reports': [],
    'name': 't3_35ybkb',
    'num_comments': 27,
    'num_reports': None,
    'over_18': False,
    'permalink': '/r/wallpaper/comments/35ybkb/its_a_misty_mood_sort_of_day_1920x1080/',
    'post_hint': 'image',
    'preview': {
        'images': [{
            'id': '_8zF29cGX1DwJ0KDnbYGbh2oycytb6RQS1d807LC898',
            'resolutions': [{
                'height': 60,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=108&amp;s=43747ff659df46f3a8cbd0699b3fc2ec',
                'width': 108
            }, {
                'height': 121,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=216&amp;s=5a7b8c50f90f08cf38121bfbbb518cc2',
                'width': 216
            }, {
                'height': 179,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=320&amp;s=dddde0d7b2389824adf43cae298bcd92',
                'width': 320
            }, {
                'height': 359,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=640&amp;s=c2a05cd908a84f0261dafe2b99b70a8a',
                'width': 640
            }, {
                'height': 539,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=960&amp;s=f9112c9b8a95cf8a9399bd4c049a510e',
                'width': 960
            }, {
                'height': 607,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=1080&amp;s=95913eda85a710c8e753cc15f498c7e2',
                'width': 1080
            }],
            'source': {
                'height': 1079,
                'url': 'https://i.redditmedia.com/jwI5mvqJE-Cx1C5S99XP-RSB6B3TJKVJr-KKTVmb2zg.jpg?s=c69cfcbf626335086ae4273a6b54b45e',
                'width': 1919
            },
            'variants': {}
        }]
    },
    'quarantine': False,
    'removal_reason': None,
    'report_reasons': None,
    'saved': False,
    'score': 833,
    'secure_media': None,
    'secure_media_embed': {},
    'selftext': '',
    'selftext_html': None,
    'stickied': False,
    'subreddit': 'wallpaper',
    'subreddit_id': 't5_2qmjl',
    'suggested_sort': None,
    'thumbnail': 'http://a.thumbs.redditmedia.com/VJxDvwX98DdVVckX5-bXrO6gmoh7oHCHPBLIfyjvRn4.jpg',
    'title': "It's a Misty Mood sort of day [1920x1080]",
    'ups': 833,
    'url': 'http://i.imgur.com/fWbnJYt.jpg',
    'user_reports': [],
    'visited': False
}
```

That's quite a lot of information! Much of this information isn't relevant to our purposes. For this assignment, you should keep only the following attributes:

```
subreddit - which subreddit this post originated from
is_self - True iff the post is a self-, text-only post
ups - number of upvotes
post_hint - reddit's guess of the content of the post (could be 'image', 'link', or something else.)
title - title of the post
downs - number of downvotes 
score - the overall score of the post (basically ups - downs, but with "vote fuzzing")
url - the post's link, if it is not a self post
domain - the domain of the url 
permalink - a permanent link to the reddit post
created_utc - epoch timestamp in UTC of the post's creation
num_comments - how many comments the post has
preview - data structure containing image previews
name - unique name for this post
over_18 - true iff the post is not safe for work (NSFW)
```

You will find that some of these attributes are more helpful than others.

### Extras

#### Learning More

For the full description of Reddit JSON objects, check out [the documentation](https://github.com/reddit/reddit/wiki/JSON)

#### Viewing JSON Data In-Browser

If you're planning to poke around sample JSON data from the browser, I highly recommend JSONView for [Chrome](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) and [Firefox](https://addons.mozilla.org/en-us/firefox/addon/jsonview/). This browser addition makes it easy to explore the structure of JSON from the browser. Unfortunately, there isn't a good equivalent tool for Safari.

## Pythonic Suggestions

When processing the data from a given subreddit, make use of list comprehensions to simplify your data exploration. For example, you should never need to build an empty list during any part of this project.

If you pass `stream=True` as a keyword argument to `requests.get`, the `.content` will not be loaded at once into memory. Instead, you can use `requests.iter_content(chunk_size=1024)` to iterate over the server response content. This is generally considered good practice, and should be used when downloading image files, which may be arbitrarily large.

In keeping with the motto of "coding for the common case", you should generally blindly assume that your data is properly formatted, and catch any improper behavior in an `except` block. That is, use exceptional control flow to simplify error handling.

## Extensions

Some of these are easy, some of these are very hard.

### Download Albums

Add support for downloading imgur albums.

### Command Line Utility
We saw in class that command-line arguments can be passed to Python scripts, and these arguments will be available through `sys.argv`. Modify your program so that it can be invoked with a single command-line argument representing the subreddit to scrape data from. So, `$ python wallscraper.py wallpaper` would download all the top wallpapers of the day, and `$ python wallscraper.py fffffffuuuuuuuuuuuu` would download all the top rage comics.

### Configure your computer so that this script runs every hour/day/month
Both OS X and Linux have ways to schedule a program to run every so often (Windows is harder). If you decide to do this option, talk with us. It's one of the coolest extensions, because you get awesome wallpapers over time, but it's also one of the hardest to get right. If you want to read up on your own, look up `launchd` and `cron`.

### Programmatically set the highest-scoring wallpaper as your desktop wallpaper
Both OS X and Linux have command-line tools to programmatically set your desktop background to be a specified file path (again, Windows is harder). In combination with the previous extension, you could have an automatically shifting desktop background of the internet's top trending wallpapers!

### Support for Pagination
We currently scrape only one page of Reddit data at a time. In the response data, there are pagination tokens `before` and `after` than can be used to scroll through pages and pages of reddit. Use these pagination tokens to search through arbitrarily many pages of a subreddit.

### Wallpaper deduplication
If we ever encounter the same wallpaper twice, we'll process the data twice, download it twice, etc. Implement a system that will eliminate image download duplication. You have freedom to implement this however you want.

### Logging
When you encounter errors, log the errors instead of printing an error message. Use the `logging` library.

### Parallel Processing and Multithreading
Extend the current download code to make use of Python's multiprocessing and multithreading primitives.

## Starter Code

```
assign3/
├── README.md
└── wallpapers/
└── wallscraperutils.py
└── wallscraper.py
```

In addition to this `README`, the other starter files are:

* `wallpapers/`: where all the downloaded wallpapers will go.
* `wallscraper.py`: Barebones starter code. All of your program logic will go into this file.
* `wallscraperutils.py`: A few helper functions that may simplify some of the less interesting steps of the assignment. Read through the file for more information.

## Submitting     

Submit your final code using the `submit` script on AFS, as with previous assignments.

```
myth$ /usr/class/cs41/tools/submit
```

Furthermore, we have built a style-checking tool for you. On AFS, you can run

```
myth$ /usr/class/cs41/tools/stylecheck path/to/wallscraper.py
```

to run PEP8 linting on your Python files. We highly recommend fixing all of the style  before submitting your final solution. You can do so using the `autopep8` module discussed in lecture, although you'll have to `pip install autopep8` first inside your virtual environment.

## Grading

As stated in class, this assignment is optional. If you choose to complete this assignment, we will replace your lowest grade so far with the grades from this assignment if it helps you.

### Functionality

We'll be testing your code on live Reddit data, so make sure it works on real subreddits (as stated, we suggest `'/r/wallpapers+wallpaper+earthporn'`). There a lot of different ways you can take this assignment, so we'll be assessing functionality on a case-by-case basis. If your program handles errors gracefully and successfully downloads wallpapers from the internet, that's deserving of a &check;+! If the wallscraper is mostly correct, but fails on some inputs or crashes in certain conditions, that's a &check;. If the program *drastically* fails to either (1) connect to the internet and extract a list of top posts or (2) save posts to  the filesystem, that would be a &check;-.

### Style

As always, your style grade is comprised of three main components:

* **Pythonic practices:** Proper use of the Python tools and ways of thinking introduced in this class - using list comprehensions where appropriate, intelligent utilizing iterables/generators where appropriate, etc.
* **Program design:** General programming style - decomposition, commenting, logic, algorithm design, etc.
* **Python mechanics:** Basically everything covered in PEP8 - naming, spacing, parenthesizing, etc.

## Credit

*This assignment was inspired by a late-night conversation with Eddie Wang (@eddiew), and wouldn't be possible without the careful review of Sherman Leung (@skleung) and course helpers David Slater (@dsslater), Brexton Pham (@bpham), Conner Smith (@csmith95), and Matt Mahowald (@mmahowald)*

> With <3 by @sredmond 