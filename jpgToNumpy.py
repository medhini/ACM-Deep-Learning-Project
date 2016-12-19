import os
import numpy
from PIL import Image

PathJpgs="./resizedImages"

#add all the jpg image filenames(absolute path) to a list 
lstFilesJPG= []
for dirName, subdirList, fileList in os.walk(PathJpgs):
    for filename in fileList:
        if ".jpg" in filename.lower():  
            lstFilesJPG.append(os.path.join(dirName,filename))
            
im = Image.open(lstFilesJPG[0])
arr=numpy.array(im)

#get the size of an image
col,row=im.size

#set dimensions of the 3D numpy array 
ConstPixelDims = (int(row), int(col), len(lstFilesJPG))
ArrayJPG = numpy.zeros(ConstPixelDims, dtype=arr.dtype)

#convert each image to a 2D numpy array and stack them up to make a 3D numpy array  
for filenameJPG in lstFilesJPG:
    # read the file
    im = Image.open(filenameJPG)
    #convert to 2D numpy array
    arr=numpy.array(im)
    # store the raw image data
    ArrayJPG[:, :, lstFilesJPG.index(filenameJPG)] = arr

