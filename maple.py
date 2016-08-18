#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

__all__ = ['Scroll', 'Equip', 'ScrollOutcome'] 

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

	def scroll_outcomes(self, scroll):
		outcomes = []

		if self._slots == 0:
			return outcomes

		# The case where the scroll succeeds
		success_equip = copy.deepcopy(self)
		success_equip.slots -= 1

		for attr, value in scroll.attributes.iteritems():
			cur_attr_value = success_equip.attributes.get(attr, 0)
			success_equip.attributes[attr] = cur_attr_value + value

		success_outcome = ScrollOutcome()
		success_outcome.equip = success_equip
		success_outcome.probability = scroll.chance_success

		outcomes.append(success_outcome)

		# The case where the scroll fails
		fail_equip = copy.deepcopy(self)
		fail_equip.slots -= 1
		fail_outcome = ScrollOutcome()
		fail_outcome.equip = fail_equip
		fail_outcome.probability = 1 - scroll.chance_success

		outcomes.append(fail_outcome)

		# The case where the scroll fails, and then is destroyed
		destroy_outcome = ScrollOutcome()
		destroy_outcome.probability = (1 - scroll.chance_success) * scroll.chance_destroy

		outcomes.append(destroy_outcome)

		return outcomes

	def __repr__(self):
		return '{}, slots:{}'.format(AbstractItem.__str__(self), self._slots)

	__str__ = __repr__

class ScrollOutcome(object):
	def __init__(self):
		self._equip = None
		self._probability = None

	def _get_equip(self):
		return self._equip

	def _set_equip(self, new_equip):
		self._equip = new_equip

	equip = property(_get_equip, _set_equip)

	def _get_probability(self):
		return self._probability

	def _set_probability(self, new_probability):
		self._probability = new_probability

	probability = property(_get_probability, _set_probability)

	def __repr__(self):
		return '{}, probability:{}'.format(self._equip, self._probability)

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