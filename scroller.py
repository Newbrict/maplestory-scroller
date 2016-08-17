#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import os
import sys
import argparse

from pprint import pprint

from maple import Scroll, Equip

def process_arguments(argv):
	parser = argparse.ArgumentParser(description='Maplestory scroll cruncher')

	parser.add_argument('scroll_directory',
		metavar='SCROLL_DIRECTORY',
		help='The directory containing all scroll json files for this crunch')

	parser.add_argument('-i', '--input-equip',
		metavar='INPUT_EQUIP',
		dest='input_equip',
		required=True,
		help='The json file representing the equip you are starting with')

	parser.add_argument('-o', '--output-equip',
		metavar='OUTPUT_EQUIP',
		dest='output_equip',
		required=True,
		help='The json file representing the equip you want to end up with')

	return parser.parse_args(argv[1:])

# Can throw OSError
def parse_input_file(filename, input_object):
	with open(filename) as object_data:
		object_json = json.load(object_data)
		for attr, value in object_json.iteritems():
			setattr(input_object, attr, value)

	return input_object

def main(argv):
	args = process_arguments(argv)

	scrolls = []

	# Read through all our scroll files and create scroll objects from them
	try:
		available_scroll_files = os.listdir(args.scroll_directory)
		for scroll_file in available_scroll_files:
				new_scroll = parse_input_file(os.path.join(args.scroll_directory, scroll_file), Scroll())
				scrolls.append(new_scroll)
	except OSError:
		print "There was an error trying to read files from {}, make sure it exists".format(args.scroll_directory)
		return 1

	# Read the input equip file and create an equip object from it
	try:
		input_equip = parse_input_file(args.input_equip, Equip())
	except OSError:
		print "There was an error trying to {}, make sure it exists".format(args.input_equip)
		return 2

	# Read the output equip file and create an equip object from it
	try:
		output_equip = parse_input_file(args.output_equip, Equip())
	except OSError:
		print "There was an error trying to {}, make sure it exists".format(args.output_equip)
		return 2


	pprint(scrolls)
	pprint(input_equip)
	pprint(output_equip)
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4