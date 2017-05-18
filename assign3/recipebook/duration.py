# Turns a thing like PT45M into a duration like 45 minutes
class Duration(object):
    def __init__(self, duration_string):
        # This isn't perfect, but we'll claim it's good enough.
        # More info at https://en.wikipedia.org/wiki/ISO_8601#Durations
        # Assume all durations here are less than a day, so everything is of the form
        # PT[#H][#M][#S]
        if not duration_string:
            self.duration = 0
            self.private_final = 'M'
            return
        if duration_string == 'PT':
            self.duration = 0
            self.private_final = 'M'
            return

        duration_string = duration_string[2:] # Strip the leading PT
        minutes = 0
        if 'H' in duration_string:
            end = duration_string.index('H')
            hours = float(duration_string[:end])
            minutes += hours * 60
            duration_string = duration_string[end+1:]
        if 'M' in duration_string:
            end = duration_string.index('M')
            minutes += float(duration_string[:end])
            duration_string = duration_string[end+1:]
        if 'S' in duration_string:
            end = duration_string.index('S')
            seconds = float(duration_string[:end])
            minutes += seconds / 60
            duration_string = duration_string[end+1:]

        self.duration = minutes

    def how_long(self):
        return self.duration

    def __str__(self):
        return "Duration(minutes={})".format(self.duration)
