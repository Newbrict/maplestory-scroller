#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from maple import Scroll, Equip, Attribute

def main():
	print 'Welcome to Dimitars Ding Dong Scroll Script'
	original_stat_value = 0
	target_stat_value = 10

	my_scroll = Scroll()
	my_scroll.name = "Scroll for helmet for int 60%"
	my_scroll.chance_success = 0.6
	my_scroll.chance_destroy = 0
	my_scroll.price = 14,000,000

	#my_attribute = Attribute("int", 2)
	my_scroll.attributes['int'] = 2

	print my_scroll.attributes

if __name__ == '__main__':
	main()
	raw_input('Press enter to exit...')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4