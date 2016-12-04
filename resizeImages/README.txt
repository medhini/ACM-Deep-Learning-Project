First, install Pillow
  pip install Pillow
Install ImageMagick (should already be there in ubuntu 16.04)
  sudo apt-get install imagemagick
Convert all dcm images to jpg:
  open terminal in the directory with all dcm images
  run this command:
  mogrify -format jpg *.dcm
  or, if you want to specify the directory for the converted files :
    mogrify -path <PATH> -format jpg *.dcm

  This should create jpg images for all the dcm files

now to resize the images, use the function resizeAllJpegs(sourceDirectory,writeDirectory)
This will find the smallest jpeg in the source directory , resize all jpegs in the source directory to that size, and then save to the write directory.

Usage example:
from resizeAllInDirectory import resizeAllJpegs
resizeAllJpegs('/home/deepak/Pictures/','/home/deepak/ACMProject/ResizedImages/')
