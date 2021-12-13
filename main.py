#!/usr/bin/env python
"""
CHURCH CALENDAR CSV GENERATOR
"""

import calendar
from dataclasses import dataclass
from datetime import datetime
# from pprint import pprint
import sys
import click
from dataclass_csv import DataclassWriter



@dataclass
class Event():
    """Event for CSV export"""
    # pylint: disable=too-many-instance-attributes
    event_name: str
    venue_name: str
    organizer_name: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    all_day_event: str
    categories: str
    event_cost: str
    event_phone: str
    event_website: str
    show_map_link: str
    show_map: str
    event_description: str


YEAR: int = 2022
MONTHS: dict[int, list[list[int]]]
MONTHS = dict(enumerate([calendar.monthcalendar(2022, month) for month in
                         range(1, 13)], start=1))

def suffix(day: int) -> str:
    """convert day to suffix"""
    result: str = 'th'
    if day in [1, 21, 31]:
        result = 'st'
    elif day in [2, 22]:
        result = 'nd'
    elif day in [3, 23]:
        result = 'rd'
    return result


def sort_events(events: list[Event]) -> list[Event]:
    """sort events"""
    events = sorted(events, key=lambda k: (k.start_date, k.start_time))
    return events

def add_event(events: list[Event],
              name: str,
              categories: str,
              description: str,
              start,
              finish) -> None:
    """create event"""
    # pylint: disable=too-many-arguments
    event = Event(name,
                  "Main Campus",
                  "",
                  start.strftime("%Y-%m-%d"),
                  start.strftime("%I:%M %p"),
                  finish.strftime("%Y-%m-%d"),
                  finish.strftime("%I:%M %p"),
                  "FALSE",
                  categories,
                  "",
                  "",
                  "",
                  "",
                  "",
                  description)
    events.append(event)

def add_wednesdays(events: list[Event],
                year: int,
                month: int,
                weeks: list[list[int]]) -> None:
    """add Wednesday events to calendar"""
    days = [day[2] for day in weeks if day[2]]

    add_event(events,
              "Mid Week Service 6:00pm",
              "Mid Week Service",
              "",
              datetime(year, month, days[0], 19, 00, 00),
              datetime(year, month, days[0], 21, 00, 00),
             )

    add_event(events,
              "Mid Week Service 6:00pm",
              "Mid Week Service",
              "",
              datetime(year, month, days[1], 19, 00, 00),
              datetime(year, month, days[1], 21, 00, 00),
             )

    add_event(events,
              "Mid Week Service 6:00pm",
              "Mid Week Service",
              "",
              datetime(year, month, days[2], 19, 00, 00),
              datetime(year, month, days[2], 21, 00, 00),
             )

    add_event(events,
              "Mid Week Service 6:00pm",
              "Mid Week Service",
              "",
              datetime(year, month, days[3], 19, 00, 00),
              datetime(year, month, days[3], 21, 00, 00),
             )

    if len(days) == 5:
        add_event(events,
                  "Mid Week Service 6:00pm",
                  "Mid Week Service",
                  "",
                  datetime(year, month, days[4], 19, 00, 00),
                  datetime(year, month, days[4], 21, 00, 00),
                 )

def add_thursdays(events: list[Event],
                year: int,
                month: int,
                days: list[list[int]]) -> None:
    """add Thursday events to calendar"""
    days = [day[3] for day in days if day[3]]

    add_event(events,
              "Woman’s Meeting 10:00am",
              "Woman’s Meeting",
              "Woman 2 Woman Bible Study",
              datetime(year, month, days[0], 19, 00, 00),
              datetime(year, month, days[0], 21, 00, 00),
             )

    add_event(events,
              "Woman’s Meeting 10:00am",
              "Woman’s Meeting",
              "Woman 2 Woman Bible Study",
              datetime(year, month, days[1], 19, 00, 00),
              datetime(year, month, days[1], 21, 00, 00),
             )

    add_event(events,
              "Woman’s Meeting 10:00am",
              "Woman’s Meeting",
              "Woman 2 Woman Bible Study",
              datetime(year, month, days[2], 19, 00, 00),
              datetime(year, month, days[2], 21, 00, 00),
             )

    add_event(events,
              "Woman’s Meeting 10:00am",
              "Woman’s Meeting",
              "Woman 2 Woman Bible Study",
              datetime(year, month, days[3], 19, 00, 00),
              datetime(year, month, days[3], 21, 00, 00),
             )

    if len(days) == 5:
        add_event(events,
                  "Woman’s Meeting 10:00am",
                  "Woman’s Meeting",
                  "Woman 2 Woman Bible Study",
                  datetime(year, month, days[4], 19, 00, 00),
                  datetime(year, month, days[4], 21, 00, 00),
                 )


def add_fridays(events: list[Event],
                year: int,
                month: int,
                days: list[list[int]]) -> None:
    """add Friday events to calendar"""
    days = [day[4] for day in days if day[4]]

    if len(days) == 5:
        add_event(events,
                  "Family Movie Night 7:00pm",
                  "Movie Night",
                  "Movie to be announced",
                  datetime(year, month, days[4], 19, 00, 00),
                  datetime(year, month, days[4], 21, 00, 00),
                 )

def add_saturdays(events: list[Event],
                year: int,
                month: int,
                weeks: list[list[int]]) -> None:
    """add Saturday events to calendar"""
    days = [day[5] for day in weeks if day[5]]

    add_event(events,
              "Men's Breakfast 8:00am",
              "Men's Meeting",
              "",
              datetime(year, month, days[1], 19, 00, 00),
              datetime(year, month, days[1], 21, 00, 00),
             )

def add_sundays(events: list[Event],
                year: int,
                month: int,
                weeks: list[list[int]]) -> None:
    """add Sunday events to calendar"""
    days = [day[6] for day in weeks if day[6]]

    add_event(events,
              "Sunday Service 10:00am",
              "Sunday Service",
              "Prayer Room open from 8:30 AM to 9:30 AM. Worship Service "
              "starts at 10:00 AM. First Sunday of the month is "
              "Missions Sunday.",
              datetime(year, month, days[0], 10, 00, 00),
              datetime(year, month, days[0], 12, 00, 00),
             )

    add_event(events,
              "Sunday Service 10:00am",
              "Sunday Service",
              "Prayer Room open from 8:30 AM to 9:30 AM. Worship Service "
              "starts at 10:00 AM. Second Sunday of the month is "
              "Baptism Sunday.",
              datetime(year, month, days[1], 10, 00, 00),
              datetime(year, month, days[1], 12, 00, 00),
             )

    add_event(events,
              "Sunday Service 10:00am",
              "Sunday Service",
              "Prayer Room open from 8:30 AM to 9:30 AM. Worship Service "
              "starts at 10:00 AM. Third Sunday of the month is "
              "Communion Sunday.",
              datetime(year, month, days[2], 10, 00, 00),
              datetime(year, month, days[2], 12, 00, 00),
             )

    add_event(events,
              "Sunday Service 10:00am",
              "Sunday Service",
              "Prayer Room open from 8:30 AM to 9:30 AM. Worship Service "
              "starts at 10:00 AM. Fourth Sunday of the month is "
              "Coins for Kids Sunday.",
              datetime(year, month, days[3], 10, 00, 00),
              datetime(year, month, days[3], 12, 00, 00),
             )

    if len(days) == 5:
        add_event(events,
                  "Sunday Service 10:00am",
                  "Sunday Service",
                  "Prayer Room open from 8:30 AM to 9:30 AM. Worship Service "
                  "starts at 10:00 AM. Fifth Sunday of the month is "
                  "Potluck Sunday",
                  datetime(year, month, days[4], 10, 00, 00),
                  datetime(year, month, days[4], 12, 00, 00),
                 )


def write_calendar(events: list[Event]) -> None:
    """write calendar to csv file"""
    with open("calendar.csv", "w", encoding="utf-8") as handle:
        writer =DataclassWriter(handle, events, Event)
        writer.map("event_name").to("EVENT NAME")
        writer.map("venue_name").to("VENUE NAME")
        writer.map("organizer_name").to("ORGANIZER NAME")
        writer.map("start_date").to("START DATE")
        writer.map("start_time").to("START TIME")
        writer.map("end_date").to("END DATE")
        writer.map("end_time").to("END TIME")
        writer.map("all_day_event").to("ALL DAY EVENT")
        writer.map("categories").to("CATEGORIES")
        writer.map("event_cost").to("EVENT COST")
        writer.map("event_phone").to("EVENT PHONE")
        writer.map("event_website").to("EVENT_WEBSITE")
        writer.map("show_map_link").to("SHOW MAP LINK?")
        writer.map("show_map").to("SHOW MAP?")
        writer.map("event_description").to("EVENT DESCRIPTION")
        writer.write()

@click.command()
def main():
    """create csv file"""
    events: list[Event] = []
    for month, weeks in MONTHS.items():
        add_wednesdays(events, YEAR, month, weeks)
        add_thursdays(events, YEAR, month, weeks)
        add_fridays(events, YEAR, month, weeks)
        add_saturdays(events, YEAR, month, weeks)
        add_sundays(events, YEAR, month, weeks)

    events = sort_events(events)
    write_calendar(events)

    sys.exit(0)


if __name__ == "__main__":
    main()  # pylint: disable=E1120
