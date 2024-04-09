# python_clock.py

import tkinter as tk
from time import strftime

def update_clock():
    current_time = strftime(time_format.get())
    label.config(text=current_time)
    label.after(1000, update_clock)

def toggle_background_color():
    current_color = root.cget('bg')
    next_color = 'black' if current_color == 'white' else 'white'
    root.config(bg=next_color)
    label.config(bg=next_color)

def toggle_time_format():
    current_format = time_format.get()
    next_format = '%H:%M:%S %p' if current_format == '%I:%M:%S %p' else '%I:%M:%S %p'
    time_format.set(next_format)

root = tk.Tk()
root.title('Python Clock App')
root.configure(bg='black')

# Create clock label
time_format = tk.StringVar()
time_format.set('%I:%M:%S %p')  # Initial time format: 12-hour format with AM/PM
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='#FFD700')
label.pack(anchor='center')
update_clock()

# Create button for toggling background color
toggle_button = tk.Button(root, text="Toggle Background", command=toggle_background_color)
toggle_button.pack(pady=5)

# Create button for toggling time format
time_format_button = tk.Button(root, text="Toggle Time Format", command=toggle_time_format)
time_format_button.pack(pady=5)

root.mainloop()
