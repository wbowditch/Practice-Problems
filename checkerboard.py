#some GUI drawing basics

from Tkinter import *


def checkerboard(can):
    w=can.winfo_width()
    h=can.winfo_height()
    cellwidth = w/10
    cellheight=h/10
    for row in range(10):
        for col in range(10):
            if col <=row:
                color = 'red'
            else:
                color = 'blue'
                
            can.create_rectangle(col*cellwidth,row*cellheight,(col+1)*cellwidth,(row+1)*cellheight,fill=color)


window=Tk()
thecanvas = Canvas(window, width=500,height=500)
thecanvas.grid(row=0,column=0)
window.update_idletasks()
checkerboard(thecanvas)
window.mainloop()
    
