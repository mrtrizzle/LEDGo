from include.PerlinNoise import PerlinNoiseFactory as PNF
import include.colormaps as cm
import numpy as np
from os import sys, path

X_SIZE = 8
Y_SIZE = 8

if __name__ == '__main__' and __package__ is None:
	# Import from parent directory
	sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
	from Matrix import Matrix

	fac = PNF(3, octaves=2)
	
	mat = Matrix(8,8)

	i = 0
	i_inc = 0.05
	zoom = 4
	framerate = 500

	vals = np.zeros ( (8,8,3))

	while True:
		try:
			for x in range(X_SIZE):
				for y in range(Y_SIZE):
					vals = fac(x/float(X_SIZE/zoom),y/float(Y_SIZE/zoom), i / float(framerate))
			
			# From Sinecosine:
			#img = np.round(cm.viridis(f(x, y, alpha))[:,:,0:3]*255);

			# TODO: Make this work somehow.
			mat.mat = np.round( cm.viridis(vals)[:, :, 0:3]*255 ) 
					
			i += i_inc
			mat.drawMatrix()
		except KeyboardInterrupt:
			mat.destOPC(mat.connection, mat.mat)
			break



