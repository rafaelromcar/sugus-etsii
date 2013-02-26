#!/bin/python

import unittest

class TestPlayer(unittest.TestCas):
	def setUp(self):
		self.player = Player(name="Sergio Soto")
	
	def test_addpoint_0(self):
		self.player.set_points(0)
		self.player.add_point()
		assert self.player.get_points() == 15 
		
	def test_addpoint_1(self):
		self.player.set_points(15)
		self.player.add_point()
		assert self.player.get_points() == 30 

	def test_addpoint_2(self):
		self.player.set_points(30)
		self.player.add_point()
		assert self.player.get_points() == 40 
		
	def test_addpoint(self):
		self.player.set_points(40)
		self.player.add_point()
		assert self.player.get_points() == 45

if __name__ == "__main__" 
	unittest.main()
