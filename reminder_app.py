import time as tm 
from datetime import datetime, timedelta as dt
import tkinter as tk


root = tk.Tk()
root.title("Reminder App")
message = tk.Label(root, text="Select O'Clock", font=("Helvetica", 16))
entry_widget = tk.Entry(root, font=("Helvetica", 16))
button_widget = tk.Button(root, text="Set Reminder", font=("Helvetica", 16))
message.pack()
entry_widget.pack()
button_widget.pack()
root.geometry("300x200")
root.mainloop()

