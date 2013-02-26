#!/bin/python

class Tennis_player:

	def __init__(self, name):
		self.__name = name
		self.__points = 0

	def add_point(self):
		if self.__points == 30:
			self.__points+=10
		elif self.__points == 40:
			self.__points+=5
		elif self.__points == 0 or self.__points == 15:
			self.__points+=15
		else:
			raise Exception()
			
	def get_points(self):
		return self.__points

	def set_points(self, points):
		self.__points = points
