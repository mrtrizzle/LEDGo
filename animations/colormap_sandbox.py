


import include.colormaps as cm


val = 0

for i in range(100):
	val += 0.1

print(cm.viridis([[0, 1],
				  [2,3]])[:, :, 0:3]*255)
#print(cm.viridis(255)[:, :, 0:3])
#print(cm.viridis(300)[:, :, 0:3])