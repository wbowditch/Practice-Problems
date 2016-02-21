# BCImage
# Get 2D list of pixels, indexed by [row][col].
# Each element is a list [red, green, blue]
# (So, it's really 3D ...)

import os

def setPixels(photo, pixels):
    """Set each pixel of the photo from the colors in the pixels 3D list"""
    data = ' '.join(['{'+' '.join(["#%02x%02x%02x" % tuple(pixels[row][col]) for col in range(len(pixels[0]))])+'}' for row in range(len(pixels))])
    photo.put(data)           

def getPixels(filename):
    f = open(filename,'rb')
    f.readline()
    c = f.read(1)
    while c=='#':
        f.readline()
        c = f.read(1)
    dim = (c+f.readline()).strip().split()
    w = int(dim[0])
    h = int(dim[1])
    f.readline()
    s = f.read()
    print len(s)

    pix = [[[ord(s[i*3*w+j*3+k]) for k in range(3) ] for j in range(w)] for i in range(h)]
    return pix
              
