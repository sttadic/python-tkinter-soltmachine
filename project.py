import tkinter as tk
from tkinter import ttk
import random
import sys


# Function that opens cashout menu window and set it as modal - active widow with .grab_set() module
def cashout_menu():
    cashout_window = tk.Toplevel(root, takefocus=True)
    cashout_window.grab_set()
    amount_lbl = ttk.Label(cashout_window, text=f"Collect $100?", font=('', 20))
    collect_btn = ttk.Button(cashout_window, text='Collect')
    cancel_btn = ttk.Button(cashout_window, text='Cancel')
    amount_lbl.grid(row=0, columnspan=2, padx=20, pady=20)
    cancel_btn.grid(row=1, column=0, pady=(0, 20), padx=10)
    collect_btn.grid(row=1, column=1, pady=(0, 20), padx=10)
    
    
# Function that updates text value of bet (bet_lbl) widget based on a scale value and total
def update_bet(*args):
    bet_lbl.config(text=f'Bet: ${bet_var.get()}')
    total_lbl.config(text=f'Total bet: ${bet_var.get()*payline_var.get()}')


# Update number of bet lines (paylines) and total
def update_lines(*args):
    paylines_lbl.config(text=f'Paylines: {payline_var.get()}')
    total_lbl.config(text=f'Total bet: ${bet_var.get()*payline_var.get()}')
    

# Create window object (non resizable)
root = tk.Tk()
root.resizable(width=False, height=False)


# Load image file
bg = tk.PhotoImage(file = 'background.png')

# Set background of entire window
bg_label = ttk.Label(root, image=bg)
bg_label.place(x=0, y=0)

# Message displaying information during the game
msg_lbl = ttk.Label(root, text='Welcome!', font=('Arial', 18), foreground='white', background='black', width=35, anchor='center')
msg_lbl.grid(row=0, column=0, columnspan=3, pady=10)


# Slot machine's frame encompasing reels
slot_frm = ttk.Frame(root, relief='ridge', borderwidth=5)
slot_frm.grid(row=1, column=0, columnspan=3, padx=10)

# Reels
reel_1x1 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_1x2 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_1x3 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_2x1 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_2x2 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_2x3 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_3x1 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_3x2 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)
reel_3x3 = tk.Canvas(slot_frm, relief='groove', borderwidth=2, width=150, height=150)

# Grid layout for reels
reel_1x1.grid(row=0, column=0)
reel_1x2.grid(row=0, column=1)
reel_1x3.grid(row=0, column=2)
reel_2x1.grid(row=1, column=0)
reel_2x2.grid(row=1, column=1)
reel_2x3.grid(row=1, column=2)
reel_3x1.grid(row=2, column=0)
reel_3x2.grid(row=2, column=1)
reel_3x3.grid(row=2, column=2)


# Game menu and controls frame
control_frm = ttk.Frame(root)
control_frm.grid(columnspan=3, pady=10)

# Initalize IntVar to store bet value and set its default value to 1, create bet label and amount-adjust slider for bet
bet_var = tk.IntVar()
bet_var.set(1)
bet_lbl = ttk.Label(control_frm, text='Bet: $1', font=('', 16), justify='left')
bet_scl = ttk.Scale(control_frm, from_=1, to=10, orient='horizontal', variable=bet_var, command=update_bet)

# Paylines label and amount-adjust slider for lines
payline_var = tk.IntVar()
payline_var.set(1)
paylines_lbl = ttk.Label(control_frm, text='Paylines: 1', font=('', 16), justify='center')
paylines_scl = ttk.Scale(control_frm, from_=1, to=3, orient='horizontal', variable=payline_var, command=update_lines)

# Total bet label
total_lbl = ttk.Label(control_frm, text=f'Total Bet: $1', font=('', 16), justify='right', foreground='red', width=11)

# Balance label
balance_lbl = ttk.Label(control_frm, text='BALANCE: $100', font=('', 16))

# Buttons widgets and thier appearance
spin_btn = ttk.Button(control_frm, text='SPIN')
cashout_btn = ttk.Button(control_frm, text='Cash Out', command=cashout_menu)
ttk.Style().configure('TButton', font=('Helvetica', 20))

# Grid layout for widgets inside of a control frame
bet_lbl.grid(row=0, column=0, padx=(3, 0))
bet_scl.grid(row=1,column=0, padx=(3, 0))
paylines_lbl.grid(row=0, column=1, padx=30)
paylines_scl.grid(row=1, column=1)
total_lbl.grid(row=0, column=2, padx=(0, 3))
balance_lbl.grid(row=2, columnspan=3, pady=20)
spin_btn.grid(row=3, columnspan=3)
cashout_btn.grid(row=4, columnspan=3, pady=20) 


# Event loop
root.mainloop()