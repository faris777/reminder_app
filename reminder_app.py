import time as tm 
from datetime import datetime, timedelta as dt
import tkinter as tk


root = tk.Tk()
root.title("Reminder App")
message = tk.Label(root, text="Select O'Clock", font=("Helvetica", 16))
message2 = tk.Label(root, text="(24-Hour Format)", font=("Helvetica", 12))
message3 = tk.Label(root, text="Enter Reminder Message:", font=("Helvetica", 16))
entry_widget = tk.Entry(root, font=("Helvetica", 16),hint="Meeting @ 3pm")
button_widget = tk.Button(root, text="Set Reminder", font=("Helvetica", 16))
message.grid(row=0, column=0)
message2.grid(row=0, column=1)
message3.grid(row=1, column=0)
entry_widget.grid(row=1, column=1)
button_widget.grid(row=2, column=0, columnspan=2)
root.geometry("400x400")
root.mainloop()

