import time, random, sys, argparse
import numpy as np
import glc
from random import randint


class Matrix(object):
	def __init__(self, width, height):
		self.w = width
		self.h = height
		self.connection = glc.InitOPC()

		self.mat = np.zeros((self.w,self.h,3))
		
	def setPixel(self,x,y,r,g,b):
		self.mat[x,y,0] = r
		self.mat[x,y,1] = g
		self.mat[x,y,2] = b

	def drawMatrix(self):
		self.connection.put_pixels(glc.image2pixels(self.mat))

	def clearMatrix(self):
		self.mat = np.zeros((self.w,self.h,3))
		self.drawMatrix()
	
	def colorPixel(self,x,y,r,g,b):
		self.setPixel(x,y,r,g,b)
		self.drawMatrix()

	def rgb_str2triple(self, rgb):
		triple = rgb[rgb.find("(")+1:rgb.find(")")].split(",")
		return triple[0], triple[1], triple[2]

	def convertJSPixel(self,x,y,color):
		"""
		Helper function that transforms the x,y coordinate from the JS application
		into the adequate coordinates on the axis (y is flipped).
		Also converts the css 'rgb(1,2,3)' String into the r,g,b components.
		"""
		r,g,b = self.rgb_str2triple(color)
		self.colorPixel(x, abs(y-self.h+1),r,g,b)

	def fillWithColor(self,color):
		r,g,b = self.rgb_str2triple(color)
		for i in range(len(self.mat)):
			for j in range(len(self.mat[0])):
				self.mat[i][j] = [r,g,b]
		self.drawMatrix()

