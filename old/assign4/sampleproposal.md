# CS41 Sample Project Proposal: Sous Chef

> Sam Redmond (sredmond) and Guido van Rossum (bdfl)


## Overview

We want to build a program that suggests (and generates) recipes given a set of ingredients to include and exclude.


## Background

There are lots of recipe websites on the internet, where you can search for a term like "pie" and you'll get back a list of pies. Usually, there are lots of good utilities in place to search the results in various ways - by price of ingredients, by total preparation time, etc. However, the results are determined only by the query string.

We want to let a user supply a set of ingredients to include and exclude - say, ingredients they already have in their kitchen and allergens, respectively - and then we suggest highly-rated recipes that use or focus on those ingredients. Perhaps they can restrict the results to dishes with only the specified ingredients in case they *really* don't want to go to the market. Hopefully, we can also use some machine learning techniques to generate new recipes centered on the given ingredients using a variant of k-nearest neighbors and a few hand-chosen heuristics.


## Implementation Strategy

Our project falls into three major categories - scraping the data, interacting with the user, and computing recipes to output to the user.

First, we're going to scrape the [BigOven API](http://api2.bigoven.com/web/documentation), which has over 350,000 recipes. We'll put all of the recipes into a big database so that we can efficiently query it later. For this part, we're going to rely extensively on the `requests` module discussed in class - and perhaps some of the multiprocessing primitives in the standard library to speed up the download. There's also [Food2Fork API](http://food2fork.com/about/api) which has over 200,000 recipes if we need more data points. Lastly, we could always scrape the HTML of other common recipe sites like allrecipes.com.

To interact with the user, we're going to have a simple text-based I/O system where the user enters the ingredients one at a time and then signals when done. We'll then output a bunch of recipes for the user to choose from.

To actually compute the best recipes, we'll simply filter out all the recipes that *don't* contain the desired ingredients or *do* contain the undesired ingredients. Of the remaining recipes, we'll sort them on a combination of relevance to the original ingredient suggestions and overall ratings. We plan to use the awesome pandas library for better data manipulation of the recipes in raw Python.


## Tasks

1. Authenticate to the BigOven API
2. Download all of the recipes into a database
3. Load the recipes into Python Recipe class and Cookbook class
4. Main loop that asks user for ingredients and returns recipes using the class interface
5. Match ingredient names to names in recipes to filter bad recipes
6. Sort remaining recipes by a "good" heuristic (we'll need to try a lot of heuristics)
7. *(Stretch)* Use common food substitutions and word misspellings for more flexible user input (i.e. buter -> butter, pop -> soda)
8. *(Stretch)* Map the recipes into a high-dimensional vector space and run clustering algorithms to find the best-matching recipes
9. *(Stretch)* Integrate with Instacart so that any missing ingredients can get automatically delivered

Honestly, the only part we're worried about is the actual algorithm of choosing the best matching recipes. Can a naive algorithm do "well enough," or do we need to incorporate ML techniques to get reasonable results? We're fairly confident that we can scrape the recipe data and do the console I/O.


### Estimated Timeline

**(Core)**

* Task 1 (1 hours) - both
* Task 2 (2 hours) - both
* Task 3 (0.5 hours) - Guido
* Task 4 (1 hours) - Sam
* Task 5 (1 hours) - Sam
* Task 6 (3 hours) - both

**(Stretch)**

* Task 7 (1.5 hours) - Sam
* Task 8 (4 hours) - Sam
* Task 9 (5 hours) - Guido

We've made a little progress on Task 1 (we acquired an API token), but we haven't used it to connect to the API endpoint yet.


## Resources

All of our data is going to come from the APIs described above, but we're also going to hand-code some test recipes for small data sets to make sure the general logic is working. 