#!/usr/bin/python


class my_class:

	def __init__(self):
		print("init")
		self.s = ""

	def prnt(self):
		print (self.s)


cla = my_class()
cla.s = "1"
cla.prnt()
clb = my_class()
clb.s = "2"
clb.prnt()
cla.prnt()

