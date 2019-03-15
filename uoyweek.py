#!/usr/bin/env python3

from datetime import date, timedelta
from calendar import day_name, day_abbr
from argparse import ArgumentParser

def main(short=False, lower=False, termOnly=False):
    message = getTerm(date.today()).toString(date.today(), short=short, lowerC=lower, termOnly=termOnly)
    if message != "":
        print(message)

class Period:
    def __init__(self, date: date, name: str):
        self.start = date
        self.name = name
    
    def toString(self, today: date):
        if self.start <= today:
            return self.name
        else:
            return None
    def __str__(self):
        return "{} \"{}\" at {}".format(self.__class__.__name__, self.name, self.start)

    def __repr__(self): return self.__str__()

class Term(Period):
    def __init__(self, date: date, name: str):
        date = date - timedelta(days=date.weekday())
        Period.__init__(self, date, name)

    def getWeekNum(self, today: date):
        return (today - self.start).days // 7 + 1

    def toString(self, today: date, short=False, lowerC=False, termOnly=False):
        weeknum = self.getWeekNum(today)
        t = self.name[:3] if short else self.name
        d = day_abbr[today.weekday()] if short else day_name[today.weekday()]
        result = "{}/{}/{}".format(t, weeknum, d)
        return result.lower() if lowerC else result

class Holiday(Period):
    def __init__(self, date: date, name: str):
        Period.__init__(self, date, name)

    def toString(self, today: date, short=False, lowerC=False, termOnly=False):
        if termOnly:
            return ""
        result = self.name + ("" if short else " Holidays")
        return result.lower() if lowerC else result

dates = sorted([
    Term(date(2018,9,24),"Autumn"),
    Holiday(date(2018,11,30),"Christmas"),
    Term(date(2019,1,7),"Spring"),
    Holiday(date(2019,3,15), "Easter"),
    Term(date(2019,4,15),"Summer"),
    Holiday(date(2019,6,21),"Summer"),
    Term(date(2019,9,30),"Autumn"),
    Holiday(date(2019,12,6),"Christmas"),
    Term(date(2020,1,6),"Spring"),
    Holiday(date(2020,3,13),"Easter"),
    Term(date(2020,4,14),"Summer"),
    Holiday(date(2020,6,19),"Summer"),
    Term(date(2020,9,28),"Autumn"),
    Holiday(date(2020,12,4),"Christmas"),
    Term(date(2021,1,11),"Spring"),
    Holiday(date(2021,3,19),"Easter"),
    Term(date(2021,4,19),"Summer"),
    Holiday(date(2021,6,25),"Summer"),
    Term(date(2021,9,27),"Autumn"),
    Holiday(date(2021,12,3),"Christmas"),
    Term(date(2022,1,10),"Spring"),
    Holiday(date(2022,3,18),"Easter"),
    Term(date(2022,4,19),"Summer"),
    Holiday(date(2022,6,24),"Summer"),
    Term(date(2022,9,26),"Autumn"),
    Holiday(date(2022,12,2),"Christmas"),
    Term(date(2023,1,9),"Spring"),
    Holiday(date(2023,3,17),"Easter"),
    Term(date(2023,4,17),"Summer"),
    Holiday(date(2023,6,23),"Summer"),
    Term(date(2023,9,25),"Autumn"),
    Holiday(date(2023,12,1),"Christmas"),
    Term(date(2024,1,8),"Spring")
], key=lambda p:p.start)

def getTerm(today: date):
    return max(filter(lambda p:p.start <= today, dates), key=lambda p:p.start)
    # we can probably optimise this, since `dates` is known to be in chronological order,
    # to return the last date from the start that is before today

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--short", help="Prints a shortened version of the date, abbreviating the term and day.", action="store_true")
    parser.add_argument("-l", "--lower", help="Converts to lowercase.", action="store_true")
    parser.add_argument("-t", "--term-only", help="Prints nothing if it is currently a holiday, instead of the holiday name.", dest="termOnly", action="store_true")
    args = parser.parse_args()
    main(**vars(args))