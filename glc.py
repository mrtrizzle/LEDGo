# Source: kellertuer / Glinsterlichten 
# https://github.com/kellertuer/Glinsterlichten
#
# Extends the opc by a few methods to easy usage of images.
#


#
# Constants
#

import includes.opc as opc
import time
import numpy as np

img_BLACK = np.zeros( (8,16,3) )
c_BLACK = [ (0,0,0) ] * 512


#
# Functions
#

def image2pixels(image):
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
    # An image is layouted in first x, then y direction starting with the moest 
    # top left index: 
    # 0,0 1,0 2,0
    # 0,1 1,1 2,1
    # 0,2 1,2 2,2
    # In opc the pixels are adressed column-first and it seems to be fixed to
    # 512 pixels in total (check JSON of fcserver?)
    # 0  64
    # 1  65
    # .. ..
    # 63 127
    pixels = c_BLACK
    imgS = image.shape
    for xInd in range(imgS[0]):
        for yInd in range(imgS[1]):
            
            # TODO: Hier den richtigen Index berechnen
            index = xInd*8 + yInd if xInd % 2 == 0 else (xInd*8)+(7-yInd)

            pixels[index] = tuple(image[xInd,yInd,0:3])
    return pixels

def InitOPC(url='localhost:7890'):
    """
    initOPC() initializes the Open Pixel Control (OPC)
    """
    return opc.Client(url)

def destOPC(c,img,fadetime = .66):
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
    c.put_pixels(image2pixels(np.mean(img).astype(int)-img_BLACK))
    time.sleep(fadetime/10)
    c.put_pixels(image2pixels(img))
    for i in range(np.round(np.max(img)).astype(int),0,-1):
        c_img = np.round(img/np.max(img)*i)
        c.put_pixels(image2pixels(c_img))
        time.sleep(fadetime*9/(10*np.max(img)))
    print('Ciaobelko.')