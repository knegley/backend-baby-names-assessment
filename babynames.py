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
    baby_dict = {}
    year_pattern = re.compile(r"([\d]{4})")
    year_match = year_pattern.search(filename)

    year = filename[year_match.start():year_match.end()]
    print(year)
    names = []

    # baby_dict["year"]=year

    # +++your code here+++
    pattern = re.compile(
        r".+<td>(?P<rank>[\d]+)</td><td>(?P<boy_name>[\w]+)</td><td>(?P<girl_name>[\w]+).{5}")
    with open(filename) as f:
        lines = f.readlines()

        # for line in lines:
        #     print(pattern.match(line))
        #     # if result:
        #     #     print("match exists")
    for line in lines:
        if pattern.match(line):
            match = pattern.match(line)
            # print(match.groups())
            # print(pattern.match(line).group("rank"))
            baby_dict[match.group("rank")] = match.group(
                "boy_name", "girl_name")

    # updated code to reflect proper printing
    boys = [f"{value[0]} {key}" for key, value in baby_dict.items()]
    girls = [f"{value[1]} {key}" for key, value in baby_dict.items()]
    children = [year, *boys, *girls]
    sorted_children = sorted(children)
    # print("\n".join(sorted_children))
    return "\n".join(sorted_children)
    ####

    # had to comment name assembler because of having to order list properly
    # def name_assembler(rank, babies):

    #   return f"rank:{rank} boy: {babies[0]} girl: {babies[1]}\n"
    ##########################################################
    # print(baby_dict)
    # print(baby_dict["1"][0])
    # for line in lines:
    #     if "<td>" in line:
    #         test.append(line)
    # print(lines[300])
    # print(pattern.match(lines[300]))
    # print(test)

   # commented this out baby_list = (starmap(name_assembler, baby_dict.items()))

    # commented this out with the baby list variable and name assembler names = [year+"\n", *baby_list]
    # print(names)
    # for name in names:
    #     print(name)


# extract_names("baby2008.html")


# with open("tests/baby1990.html.summary") as summary:
#     summarylines = summary.readlines()

# print(summarylines[0:4])
# for line in summarylines[0:4]:
#     print(line)


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

    print(ns)

    print(ns.files)

    # option flag
    create_summary = ns.summaryfile
    # print(create_summary)
    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    if create_summary:
        # print("yes it's being called")
        for file in file_list:
            try:
                with open(file, "x") as f:
                    for item in extract_names(file):
                        f.write(item)
            except FileExistsError:
                print(
                    f"The file: {file} exists. Would you like to create a summary of this file?\n\ttype yes or no")
                response = input()
                # print(f"your response: {response}")
                if response == "yes":
                    with open(file+".summary", "w") as overwriteFile:
                        for item in extract_names(file):
                            overwriteFile.write(item)
                    print(f"overwrited {file}")
                    extract_names(file)
                else:
                    print("closing file without overwriting")
    else:
        print("no option flag used")
        # for file in file_list:
        #     print(file)
        #     extract_names(file)
        for file in file_list:
            with open(file+".summary") as read_only_file:
                print(read_only_file.read())


if __name__ == '__main__':
    main(sys.argv[1:])
