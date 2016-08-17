#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os

from maple import Scroll, Equip, Attribute

SCROLLS_DIRECTORY = 'scrolls'

def main():
	print 'Welcome to Dimitars Ding Dong Scroll Script'


	scrolls = []

	# Read through all our scroll files and create scroll objects from them
	available_scroll_files = os.listdir(SCROLLS_DIRECTORY)
	for scroll_file in available_scroll_files:
		with open(os.path.join(SCROLLS_DIRECTORY, scroll_file)) as scroll_data:
			scroll_json = json.load(scroll_data)
			new_scroll = Scroll()
			for attr, value in scroll_json.iteritems():
				setattr(new_scroll, attr, value)
			scrolls.append(new_scroll)


	pprint(scrolls)

if __name__ == '__main__':
	main()
	raw_input('Press enter to exit...')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4