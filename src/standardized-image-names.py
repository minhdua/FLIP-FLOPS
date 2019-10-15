import os

path = 'data/objects/'

n=0
for image in os.scandir(path):
	n +=1
	os.rename(image.path,os.path.join(path,"{:06}.jpg".format(n)))
