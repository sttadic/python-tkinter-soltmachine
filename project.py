import tkinter as tk
from tkinter import ttk
import random
import sys

# Root window
root = tk.Tk()

# Message displaying info about wins and instructions during the game
msg_label = ttk.Label(root, text='Welcome', font=('Arial', 20))
msg_label.pack(pady=20)

# Slot machine's frame encompasing reels
slot_frame = ttk.Frame(root, relief='ridge', borderwidth=5)
slot_frame.pack(padx=20)

# Reels
reel_1x1 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_1x2 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_1x3 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_2x1 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_2x2 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_2x3 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_3x1 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_3x2 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)
reel_3x3 = tk.Canvas(slot_frame, relief='solid', borderwidth=2, width=150, height=150)

reel_1x1.grid(column=0, row=0)
reel_1x2.grid(column=0, row=1)
reel_1x3.grid(column=0, row=2)
reel_2x1.grid(column=1, row=0)
reel_2x2.grid(column=1, row=1)
reel_2x3.grid(column=1, row=2)
reel_3x1.grid(column=2, row=0)
reel_3x2.grid(column=2, row=1)
reel_3x3.grid(column=2, row=2)


# Balance, bet & paylines 
info_frame = ttk.Frame(root)
info_frame.pack(pady=20)

balance_label = ttk.Label(info_frame, text='Balance: $1000', font=('', 16))
bet_label = ttk.Label(info_frame, text='Bet: $50', font=('', 16))
paylines_label = ttk.Label(info_frame, text='Paylines: 3', font=('', 16))

balance_label.grid(column=0, row=0, padx=60)
bet_label.grid(column=1, row=0)
paylines_label.grid(column=2, row=0, padx=60)


# Spin button

spin_btn = ttk.Button(info_frame, text='SPIN')
change_btn = ttk.Button(info_frame, text='CHANGE BET')

# Changing appearance of a ttk.Button using configure() method
ttk.Style().configure('TButton', font=('Helvetica', 20))

spin_btn.grid(column=0, row=1, columnspan=2, pady=20)
change_btn.grid(column=1, row=1, columnspan=2, pady=20)



# Event loop
root.mainloop()