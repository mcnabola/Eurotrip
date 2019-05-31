from PIL import Image, ImageTk 
import tkinter as tk 

width = 600
size = 300


def show_entry_fields():
    print("hello")

root = tk.Tk()
root.title('EuroTrip 2019 Photo Labeller')
root.geometry("900x400")
root.resizable(0,0)

img = Image.open("lim.jpg") 
img = img.resize((width,size)) 

tkimage = ImageTk.PhotoImage(img)
bbb = tk.Label(root, image=tkimage) #have to put imageTK into a label - then insert the label onto the grid


w = tk.Label(root, text="Museum\nPlanetarium\n\nSUN 19TH MAY\n\tMilan Linate Airport")

w1 = tk.Label(root, text="TAG")
w2 = tk.Label(root, text="Author")
but = tk.Button(root, text='Add Data', command=show_entry_fields)



e1 = tk.Entry(root)
e2 = tk.Entry(root)

w.grid(row=0, column=2)
w2.grid(row=0, column=3)
w1.grid(row=1, column=3)
e1.grid(row=0, column=5)
e2.grid(row=1, column=5)

bbb.grid(row=0, column=6, rowspan=6, columnspan=12)
but.grid(row=3,column=5)


root.mainloop()

