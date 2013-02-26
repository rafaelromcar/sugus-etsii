#!/bin/python

from player import Tennis_player
import unittest

class TestPlayer(unittest.TestCase):
	
	def setUp(self):
		self.player = Tennis_player(name="Sergio Soto")
	
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
		
	def test_addpoint_3(self):
		self.player.set_points(40)
		self.player.add_point()
		assert self.player.get_points() == 45
	def test_addpoint_4(self):
		self.player.set_points(45)
		self.assertRaises(Exception, self.player.add_point)

if __name__ == "__main__":
	unittest.main()
