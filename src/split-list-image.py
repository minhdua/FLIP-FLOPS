# import labrarys 
import os
from random import shuffle

path = 'data/images/'

imgList = os.listdir(path)

#print (imgList)

pathImgList = []
for img in imgList:
	pathImg = path + img + '\n'
	pathImgList.append(pathImg)

nSplit = len(pathImgList)*80//100
print(nSplit)
listImgListTrain = pathImgList[:nSplit]
listImgListVal = pathImgList[nSplit:]

fTrain = open('train.txt','w')
fVal = open('val.txt','w')

for img in listImgListTrain:
	fTrain.write(img)

for img in listImgListVal:
	fVal.write(img)
	
# get list images in directory images

# join images with path relative

# plit list images in directory /data/images to 80 percent train and 20 test

# write list path relative in the file train.txt

# write list path realtive in the file val.txt

