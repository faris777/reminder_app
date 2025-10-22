import time as tm 
from datetime import datetime, timedelta as dt
import tkinter as tk
from time import strftime
def update_time():
    current_time = strftime("%H %M:%S", tm.localtime())
    clock_messagge.config(text=f"Current Time: {current_time}")
    clock_messagge.after(1000, update_time)
    
    
root = tk.Tk()
root.title("Reminder App")
message = tk.Label(root, text="Select O'Clock", font=("Helvetica", 16))
message2 = tk.Label(root, text="(24-Hour Format)", font=("Helvetica", 12))
message3 = tk.Label(root, text="Enter Reminder Message:", font=("Helvetica", 16))
clock = strftime("%H:%M:%S", tm.localtime())
clock_messagge = tk.Label(root,text=f"Current Time: {clock}", font=("Helvetica", 16))
entry_widget = tk.Entry(root, font=("Helvetica", 16))
button_widget = tk.Button(root, text="Set Reminder", font=("Helvetica", 16))
clock_messagge.grid(row=0, column=0, columnspan=2)
message.grid(row=1, column=0)
message2.grid(row=1, column=1)
message3.grid(row=2, column=0)
entry_widget.grid(row=2, column=1)
button_widget.grid(row=3, column=0, columnspan=2)
update_time()
root.geometry("400x400")
root.mainloop()



