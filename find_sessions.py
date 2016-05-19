#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
from __future__ import print_function
from __future__ import unicode_literals
usage = """\
Finds the best set of conference or workshop sessions to attend.
"""
import argparse
import sys
import os

import csv
import random

parser = argparse.ArgumentParser(
    description=usage,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("sessions", help="CSV with session time, session, rating")
parser.add_argument("output_file", nargs="?", type=argparse.FileType('w'),
                    default=sys.stdout)

args = parser.parse_args()

with open(args.sessions, "r") as sws_file:
    csv_reader = csv.reader(sws_file)
    header = next(csv_reader)
    sessions = {}
    to_attend = []
    for row in csv_reader:
        if row[0] not in sessions:
            sessions[row[0]] = []
        if row[1] not in to_attend:
            to_attend.append(row[1])
        session = {'session': row[1], 'score': int(row[2])}
        sessions[row[0]].append(session)

def choose_session(sessions):
    """ randomly choose one session from a list """
    random_sessions = random.sample(sessions, len(sessions))

    return random_sessions[0]

def choose_sessions(sessions, to_attend):
    """ randomly choose a set of sessions to attend, and a score """
    attend = list(to_attend)
    total_score = 0
    output = ""
    for dt in sorted(sessions):
        output += dt + ":  "
        tries = 0
        session = choose_session(sessions[dt])
        while session['session'] not in attend:
            session = choose_session(sessions[dt])
            tries += 1
            if tries > 20:
                session = {'session': 'None', 'score': 0}
                break
        session_name = session['session']
        score = session['score']
        total_score += score
        output += session_name + "\n"
        if session_name in attend:
            attend.remove(session_name)

    # print(total_score)
    output += str(attend)

    return (total_score, output)

max_count = 0
outputs = []
for i in range(10000):
    (score, output) = choose_sessions(sessions, to_attend)
    if score > max_count:
        max_count = score
        outputs = []
    if score == max_count and output not in outputs:
        # print(output)
        outputs.append(output)

for output in outputs:
    args.output_file.write(output)
    args.output_file.write("\n")
    args.output_file.write("\n")
