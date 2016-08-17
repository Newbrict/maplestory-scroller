#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['Scroll', 'Equip'] 

class AbstractItem(object):

	def __init__(self, name=None, price=None, attributes={}):
		self._name = name
		self._price = price
		self._attributes = attributes

	def _get_name(self):
		return self._name

	def _set_name(self, new_name):
		self._name = new_name

	name = property(_get_name, _set_name)

	def _get_price(self):
		return self._price

	def _set_price(self, new_price):
		self._price = new_price

	price = property(_get_price, _set_price)


	def _get_attributes(self):
		return self._attributes

	def _set_attributes(self, new_attributes):
		self._attributes = new_attributes

	attributes = property(_get_attributes, _set_attributes)

	def __repr__(self):
		return 'name: {}, price:{}, attributes:{}'.format(self._name, self._price, self._attributes)

	__str__ = __repr__

class Equip(AbstractItem):
	def __init__(self):
		AbstractItem.__init__(self)
		self._slots = None

	def _get_slots(self):
		return self._slots

	def _set_slots(self, new_slots):
		self._slots = new_slots

	slots = property(_get_slots, _set_slots)

	@staticmethod
	def compute_delta(lhs, rhs):
		delta = Equip()
		delta.name = "delta"
		delta.price = rhs.price - lhs.price
		delta.slots = rhs.slots - lhs.slots

		# Go over the left hand attributes and compute their deltas
		for attr, value in lhs.attributes.iteritems():
			value = -value
			if attr in rhs.attributes:
				value += rhs.attributes[attr]

			if value > 0:
				delta.attributes[attr] = value

		# Do the same for the right hand
		for attr, value in rhs.attributes.iteritems():
			if attr not in lhs.attributes:
				delta.attributes[attr] = value

		return delta

	def __repr__(self):
		return '{}, slots:{}'.format(AbstractItem.__str__(self), self._slots)

	__str__ = __repr__

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

	def __repr__(self):
		return '{}, chance_success:{}, chance_destroy:{}'.format(AbstractItem.__str__(self), self._chance_success, self._chance_destroy)

	__str__ = __repr__

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4