
import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def update_time():
        current_time=strftime('%H:%M:%S %p')
        label.config(text=current_time)
        label.after(1000,update_time)
label=tk.Label(root,font=('Arial',48,'bold'),background='pink',foreground='black')
label.pack(anchor='center')

update_time()
root.mainloop()