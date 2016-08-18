#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['Node'] 

class Node(object):
	def __init__(self):
		self._children = []
		self._value = None
		self._parent = None

	def _get_children(self):
		return self._children

	def _set_children(self, new_children):
		self._children = new_children

	children = property(_get_children, _set_children)

	def _get_value(self):
		return self._value

	def _set_value(self, new_value):
		self._value = new_value

	value = property(_get_value, _set_value)

	def _get_parent(self):
		return self._parent

	def _set_parent(self, new_parent):
		self._parent = new_parent

	parent = property(_get_parent, _set_parent)

	def add_children(self, new_child):
		self._children.append(new_child)

	def is_root(self):
		return self._parent is None

	def is_leaf(self):
		return len(self._children) is 0

	def __repr__(self):
		return str(self._value)

	__str__ = __repr__

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4