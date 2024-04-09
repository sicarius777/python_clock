# python_clock.py

import tkinter as tk
from time import strftime

def update_clock():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_clock)

def toggle_background_color():
    current_color = root.cget('bg')
    next_color = 'black' if current_color == 'white' else 'white'
    root.config(bg=next_color)
    label.config(bg=next_color)

root = tk.Tk()
root.title('Python Clock App')
root.configure(bg='black')

# Create clock label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='#FFD700')
label.pack(anchor='center')
update_clock()

# Create button for toggling background color
toggle_button = tk.Button(root, text="Toggle Background", command=toggle_background_color)
toggle_button.pack(pady=10)

root.mainloop()
