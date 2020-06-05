#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse
from itertools import starmap

def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    test = []
    baby_dict={}
    year_pattern=re.compile(r"([\d]{4})")
    year_match=year_pattern.search(filename)
    
    year=filename[year_match.start():year_match.end()]
    print(year)
    names = [year]
    # baby_dict["year"]=year
    
    # +++your code here+++
    pattern=re.compile(r".+<td>(?P<rank>[\d]+)</td><td>(?P<boy_name>[\w]+)</td><td>(?P<girl_name>[\w]+).{5}")
    with open(filename) as f:
        lines=f.readlines()
        
        # for line in lines:
        #     print(pattern.match(line))
        #     # if result:
        #     #     print("match exists")
    for line in lines:
        if pattern.match(line):
            match=pattern.match(line)
            # print(match.groups())
            # print(pattern.match(line).group("rank"))
            baby_dict[match.group("rank")]=match.group("boy_name", "girl_name")

    def name_assembler(rank,babies):

        return f"rank:{rank} boy: {babies[0]} girl: {babies[1]}\n"  
    # print(baby_dict)  
    # print(baby_dict["1"][0])
    # for line in lines:
    #     if "<td>" in line:
    #         test.append(line)
    # print(lines[300])
    # print(pattern.match(lines[300]))
    # print(test)

    baby_list=list(starmap(name_assembler,baby_dict.items()))

    

    names=[year,*baby_list]
    print(names)
    return names

with open("tests/baby1990.html.summary") as summary:
    summarylines= summary.readlines()

print(summarylines[0:4])
for line in summarylines[0:4]:
    print(line)


extract_names("baby1992.html")

def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser

    


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++


if __name__ == '__main__':
    main(sys.argv[1:])
