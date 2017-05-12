from Tkinter import *
import time
X = 80
N = int(sys.argv[1])
array = [-1]*N

master = Tk()
canvas_width = (N+1)*X+14
canvas_height = (N)*X+14
w = Canvas(master, 
    width=canvas_width,
    height=canvas_height)
w.pack()
w.create_rectangle(94,4,N*X+94,N*X+4)
img = PhotoImage(file="Queens.gif")
for i in range(N):
    for k in range(N):
        if k%2==0 and i%2==0:
            w.create_rectangle(94+X*k,4+X*i,94+X*(k+1),4+X*(i+1),fill="#000000")
        if k%2==1 and i%2==1:
            w.create_rectangle(94+X*k,4+X*i,94+X*(k+1),4+X*(i+1),fill="#000000")
a = w.create_image(4, 4, anchor=NW, image=img)
arrImg=[a]*N
w.delete(a)
w.create_line(4,4,84,4)
w.create_line(4,4,4,4+X*N)
w.create_line(84,4,84,4+X*N)
w.create_line(4,4+X*N,84, 4+X*N)
for i in range(N):
    arrImg[i] = w.create_image(4, 4+X*i, anchor=NW, image=img)
Label(master, text="N-QUEENS by Nguyen Trong Tuyen", fg = "black", font = "Times").pack()


def isAvailable(column) :
    for i in range(column) :
        if array[i] == array[column] or abs(i-column) == abs(array[i] - array[column]) :
            return False
    return True


def BackTracking(column) :
    if column == N :
        Label(master, text="SOLUTION FOUNDS !!!", fg = "red", font = "Times").pack()
        w.update()
        time.sleep(7)
    else :
        for i in range(N) :
            array[column] = i
            w.coords(arrImg[column],94+X*column,4+X*i)
            time.sleep(0.7)
            w.update()
            if isAvailable(column) :
                BackTracking(column+1)


def nQueens(N) :
    BackTracking(0)
    
nQueens(N)
mainloop()
