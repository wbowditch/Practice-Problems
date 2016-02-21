
#Lab exercise.  Instead of modifying an image loaded from a file, create
#a synthetic 512X512 pixel image by directly stuffing values into the pixels.


#Imported libraries

#for the GUI
from Tkinter import *

#for the file-selection dialog
import tkFileDialog

#you may need some math-y stuff for the effects
import math

# Professors Bill Ames and John Donaldson supplied these  routines
#to convert arrays to tkinter photo images, and vice-versa.


import BCImage
import random
import math

######################Create the Image########################

def create_image():
    newimage = []
    for row in range(512):
        rowentries=[]
        for col in range(512):
            rowentries.append([col/2,col/2,col/2])
        newimage.append(rowentries)
    return newimage

def create_imaged():
    newimage = []
    for row in range(512):
        rowentries=[]
        for col in range(512):
            rowentries.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        newimage.append(rowentries)
    return newimage
##
##def create_image():
##    newimage = []
##    for row in range(512):
##        rowentries=[]
##        col_block = 512/10
##        for col in range(512):
##            rowentries.append([col/2,col/2,col/2])
##        newimage.append(rowentries)
##    return newimage








#This section handles the work of reading an image from a file,
#converting between Tkinter's image type and the 3D array representation,
#and displaying the image in the canvas.
#DO NOT CHANGE ANYTHING IN THIS SECTION!


    
#draw the image, as given by the 3D array, on the canvas
def draw(can,imarray):
    photo=PhotoImage(height=len(imarray),width=len(imarray[0]))
    BCImage.setPixels(photo,imarray)
    can.image=photo
    can.create_image(256,256,image=photo)


######################################################################################
#############  The Event Handler and the Main Loop ###################################
#####################################################################################


    
def buttonHandler(event):
    wid=event.widget
    w.update_idletasks()
    if wid==create_button:
        image_array=create_imaged()
        the_canvas.delete('all')
        draw(the_canvas,image_array)

        
            
    
w = Tk()
the_canvas=Canvas(w,width=512,height=512)
the_canvas.grid(row=0,column=0,columnspan=3)
create_button=Button(w,text='Create Image')
create_button.grid(row=1,column=1)
create_button.bind('<Button-1>',buttonHandler)
w.mainloop()
