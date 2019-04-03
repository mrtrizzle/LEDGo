from include.PerlinNoise import PerlinNoiseFactory as PNF
import include.colormaps as cm
import numpy as np
from os import sys, path
import time

X_SIZE = 8
Y_SIZE = 8

if __name__ == '__main__' and __package__ is None:
	# Import from parent directory
	sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
	from Matrix import Matrix

	fac = PNF(3, octaves=1, unbias=True)
	
	mat = Matrix(8,8)

	i = 0
	i_inc = 0.001
	zoom = 2


	vals = np.zeros ( (8,8))

	while True:
		try:
			for x in range(X_SIZE):
				for y in range(Y_SIZE):
					vals[x, y] = (fac(x/float(X_SIZE/zoom),y/float(Y_SIZE/zoom), i)+1)/2
			
			
			# Some post-processing so that the Perlin values are always stretched over the whole [0,1] interval
			vals = (vals - np.min(vals)) / (np.max(vals) - np.min(vals))

			# available colormaps: {magma, inferno, plasma, viridis}
			mat.mat = np.round( cm.viridis(vals)[:, :, 0:3]*255 ) 
			
			# For debugging
			#print("min: {:.2f}, max: {:.2f}, avg: {:.2f}".format(np.min(vals), np.max(vals), np.average(vals)))

			i += i_inc
			mat.drawMatrix()
		except KeyboardInterrupt:
			mat.destOPC(mat.connection, mat.mat)
			break



