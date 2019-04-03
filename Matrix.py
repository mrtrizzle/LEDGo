import time, random, sys, argparse
import numpy as np
import includes.opc as opc
from random import randint

class Matrix(object):
	def __init__(self, width, height):
		self.w = width
		self.h = height
		self.connection = self.initOPC()
		self.mat = np.zeros((self.w,self.h,3))

	def initOPC(self, url='localhost:7890'):
		return opc.Client(url)

	def can_connect(self):
		return self.connection.can_connect()
		
	def setPixel(self,x,y,r,g,b):
		self.mat[x,y,0] = r
		self.mat[x,y,1] = g
		self.mat[x,y,2] = b

	def drawMatrix(self):
		self.connection.put_pixels(self.image2pixels(self.mat))

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
		
	def image2pixels(self, image):
	    """
	    imgage2pixels(image) convert an numpy rgb image (3D array) to the low level
	    pixel (tuple) sequence for opc
	    
	    Parameters
	    ----------
	    image: 3D numpy array, rowfirst, i.e. row x cols x 3
	    
	    Returns
	    -------
	    a column-first reshaped and padded array of tuples to match opc format
	    """
	    # An image is layouted in first x, then y direction starting with the most 
	    # top left index: 
	    # 0,0 1,0 2,0 ...
	    # 0,1 1,1 2,1 ...
	    # 0,2 1,2 2,2 ...
		# ... ... ... ... 
		# 
	    # In opc the pixels are adressed column-first and it seems to be fixed to
	    # 512 pixels in total (check JSON of fcserver?)
	    # 0  64
	    # 1  65
	    # .. ..
	    # 63 127
	    pixels = [ (0,0,0) ] * 512
	    imgS = image.shape
	    for xInd in range(imgS[0]):
	        for yInd in range(imgS[1]):
	            index = xInd*8 + yInd if xInd % 2 == 0 else (xInd*8)+(7-yInd)
	            pixels[index] = tuple(image[xInd,yInd,0:3])
	    return pixels
	
	def destOPC(self,c,img,fadetime = .66):
		"""
		destOPC() Destructor for the client of OPC,
				ensures, that all pixels are faded out and are hence off when stopping
				the programm.
			
		Parameters
		----------
		c   : the OPC client
		img : the image to fade out
		fadetime : the speed with wich to fade out
		"""
		# flash!
		img_BLACK = np.zeros( (8,16,3) )
		c.put_pixels(self.image2pixels(np.mean(img).astype(int)-img_BLACK))
		time.sleep(fadetime/10)
		c.put_pixels(self.image2pixels(img))
		for i in range(np.round(np.max(img)).astype(int),0,-1):
			c_img = np.round(img/np.max(img)*i)
			c.put_pixels(self.image2pixels(c_img))
			time.sleep(fadetime*9/(10*np.max(img)))
		print('Ciaobelko. LEDGo out.')
