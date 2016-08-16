#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['Scroll', 'Equip', 'Attributes'] 

ALL_ATTRIBUTES = [
'str',
'dex',
'int',
'luk',
'hp',
'mp',
'speed',
'jump',
'watt',
'matt',
'wdef',
'mdef',
'avoidability',
'accuracy']

class Attribute(object):

	def __init__(self, name=None, value=0):
		self._name = name
		self._value = value

	def _get_name(self):
		return self._name

	def _set_name(self, new_name):
		self._name = new_name

	name = property(_get_name, _set_name)

	def _get_value(self):
		return self._value

	def _set_value(self, new_value):
		self._value = new_value

	value = property(_get_value, _set_value)

	def __repr__(self):
		return "'{}': {}".format(self._name, self._value)

	__str__ = __repr__

class AbstractItem(object):

	def __init__(self, name=None, attributes={}, price=None):
		self._attributes = attributes
		self._name = name
		self._price = price

	def _get_name(self):
		return self._name

	def _set_name(self, new_name):
		self._name = new_name

	name = property(_get_name, _set_name)


	def _get_attributes(self):
		return self._attributes

	def _set_attributes(self, new_attributes):
		self._attributes = new_attributes

	attributes = property(_get_attributes, _set_attributes)

	def _get_price(self):
		return self._price

	def _set_price(self, new_price):
		self._price = new_price

	price = property(_get_price, _set_price)

class Equip(AbstractItem):
	def __init__(self):
		AbstractItem.__init__(self)
		self._slots = None

class Scroll(AbstractItem):
	def __init__(self):
		AbstractItem.__init__(self)
		self._chance_success = None
		self._chance_destroy = None

	def _get_chance_success(self):
		return self._chance_success

	def _set_chance_success(self, new_chance_success):
		self._chance_success = new_chance_success
		
	chance_success = property(_get_chance_success, _set_chance_success)

	def _get_chance_destroy(self):
		return self._chance_destroy

	def _set_chance_destroy(self, new_chance_destroy):
		self._chance_destroy = new_chance_destroy
		
	chance_destroy = property(_get_chance_destroy, _set_chance_destroy)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4