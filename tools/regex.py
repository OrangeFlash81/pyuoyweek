#!/usr/bin/env python3

import re
from calendar import month_name
month_number = {month_name[n]: n for n in range(1,13)}
print(month_number)

"""
    Given a (very slightly) edited copy of the main text from https://www.york.ac.uk/about/term-dates/,
    will create code that can be pasted into uoyweek.py almost verbatim (some common sense needed).
    Will be helpful in 2/3 years time when current information is out-of-date
"""

regex = re.compile(r"^(\w+)\sterm:\s[^0-9]*(\d+)\s(\w+)\s(\d+)\s-\s(\d+)\s(\w+)\s(\d+)")
print(regex)
with open('terms.txt') as terms:
    for line in terms.readlines():
        match = regex.match(line)
        if match:
            #print("MATCH   \t" + line.strip())
            if match.group(1) == "Autumn":
                monthnum = month_number[match.group(3)]
                print("Term(date({},{},{}),\"Autumn\"),".format(match.group(4),monthnum,match.group(2)))
                monthnum = month_number[match.group(6)]
                print("Holiday(date({},{},{}),\"Christmas\"),".format(match.group(7),monthnum,match.group(5)))
            elif match.group(1) == "Spring":
                monthnum = month_number[match.group(3)]
                print("Term(date({},{},{}),\"Spring\"),".format(match.group(4),monthnum,match.group(2)))
                monthnum = month_number[match.group(6)]
                print("Holiday(date({},{},{}),\"Easter\"),".format(match.group(7),monthnum,match.group(5)))
            elif match.group(1) == "Summer":
                monthnum = month_number[match.group(3)]
                print("Term(date({},{},{}),\"Summer\"),".format(match.group(4),monthnum,match.group(2)))
                monthnum = month_number[match.group(6)]
                print("Holiday(date({},{},{}),\"Summer\"),".format(match.group(7),monthnum,match.group(5)))
            else: print(match.group(1))
        else:
            print("NO MATCH: \t" + line.strip())