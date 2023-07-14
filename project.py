import tkinter as tk
from tkinter import ttk, messagebox
import random


BALANCE = 200


# SLOT MACHINE
class SlotMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Set title and non-resizable root window
        self.title('DINO HUNT')
        self.resizable(False, False)
        
        # Load image files
        self.bg = tk.PhotoImage(file = 'background.png')
        # Symbol images
        self.a = tk.PhotoImage(file='01.png')
        self.b = tk.PhotoImage(file='02.png')
        self.c = tk.PhotoImage(file='03.png')
        self.d = tk.PhotoImage(file='04.png')
        self.e = tk.PhotoImage(file='05.png')
     
        # Set background of entire window
        bg_label = ttk.Label(self, image=self.bg)
        bg_label.place(x=0, y=0)

        # Message displaying information during the game
        msg_lbl = ttk.Label(self, text='Welcome! Spin to start a game.', font=('Arial', 18), foreground='white', background='black', width=35, anchor='center')
        msg_lbl.grid(row=0, column=0, columnspan=3, pady=10)

        # Slot machine's frame encompasing reels (slots)
        slot_frm = ttk.Frame(self, relief='sunken', borderwidth=5)
        slot_frm.grid(row=1, column=0, columnspan=3, padx=10)


        # SLOT FOR A SYMBOL
        class Slot:
            def __init__(self, container):
                self.canvas = tk.Canvas(container, relief='groove', borderwidth=2, width=150, height=150)
                
        # Create slots for symblos
        self.slot_1x1 = Slot(slot_frm)
        self.slot_1x2 = Slot(slot_frm)
        self.slot_1x3 = Slot(slot_frm)
        self.slot_2x1 = Slot(slot_frm)
        self.slot_2x2 = Slot(slot_frm)
        self.slot_2x3 = Slot(slot_frm)
        self.slot_3x1 = Slot(slot_frm)
        self.slot_3x2 = Slot(slot_frm)
        self.slot_3x3 = Slot(slot_frm)
        
        # Grid layout for slots
        self.slot_1x1.canvas.grid(row=0, column=0)
        self.slot_1x2.canvas.grid(row=0, column=1)
        self.slot_1x3.canvas.grid(row=0, column=2)
        self.slot_2x1.canvas.grid(row=1, column=0)
        self.slot_2x2.canvas.grid(row=1, column=1)
        self.slot_2x3.canvas.grid(row=1, column=2)
        self.slot_3x1.canvas.grid(row=2, column=0)
        self.slot_3x2.canvas.grid(row=2, column=1)
        self.slot_3x3.canvas.grid(row=2, column=2)
        
        # Instance of the ControlFrame
        control_frame = self.ControlFrame()
        control_frame.grid(row=2, column=0, columnspan=3)
    
    
    # CONTROL FRAME
    class ControlFrame(ttk.Frame):
        def __init__(self):
            super().__init__()
            
            self.grid(columnspan=3, pady=10)
            
            # Initalize IntVar to store bet value and set its default value to 1, create bet label and amount-adjust slider for bet
            self.bet_var = tk.IntVar()
            self.bet_var.set(1)
            self.bet_lbl = ttk.Label(self, text='Bet: $1', font=('', 16), justify='left')
            self.bet_scl = ttk.Scale(self, from_=1, to=10, orient='horizontal', variable=self.bet_var, command=self.update_bet)
            
            # Paylines and amount-adjust slider for lines
            self.payline_var = tk.IntVar()
            self.payline_var.set(1)
            self.paylines_lbl = ttk.Label(self, text='Paylines: 1', font=('', 16), justify='center')
            self.paylines_scl = ttk.Scale(self, from_=1, to=3, orient='horizontal', variable=self.payline_var, command=self.update_lines)

            # Total bet label
            self.total_var = tk.IntVar()
            self.total_var.set(1)
            self.total_lbl = ttk.Label(self, text=f'Total Bet: ${self.total_var.get()}', font=('', 16), justify='right', foreground='red', width=11)

            # Balance
            self.balance_var = tk.IntVar()
            self.balance_var.set(BALANCE)
            self.balance_lbl = ttk.Label(self, text=f'BALANCE: ${self.balance_var.get()}', font=('', 16))
            
            # Buttons widgets and thier appearance
            self.spin_btn = ttk.Button(self, text='SPIN', command=self.spin)
            self.cashout_btn = ttk.Button(self, text='Cash Out', command=self.cashout_menu)
            ttk.Style().configure('TButton', font=('Helvetica', 20))

            # Grid layout for widgets inside of a control frame
            self.bet_lbl.grid(row=0, column=0, padx=(3, 0))
            self.bet_scl.grid(row=1,column=0, padx=(3, 0))
            self.paylines_lbl.grid(row=0, column=1, padx=30)
            self.paylines_scl.grid(row=1, column=1)
            self.total_lbl.grid(row=0, column=2, padx=(0, 3))
            self.balance_lbl.grid(row=2, columnspan=3, pady=20)
            self.spin_btn.grid(row=3, columnspan=3)
            self.cashout_btn.grid(row=4, columnspan=3, pady=20) 

            
        # Function that opens cashout menu window
        def cashout_menu(self):
            answer = messagebox.askyesno('CASH-OUT', f'${self.balance_var.get()} collected! Start a new game?')
            if answer:
                self.balance_var.set(BALANCE)
                self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
            else:
                self.quit()
            
                            
        # Function that updates text value of bet (bet_lbl) widget based on a scale value and total
        def update_bet(self, *args):
            self.bet_lbl.config(text=f'Bet: ${self.bet_var.get()}')
            self.total_var.set(self.bet_var.get()*self.payline_var.get())
            self.total_lbl.config(text=f'Total Bet: ${self.total_var.get()}')
            
            
        # Update number of bet lines (paylines) and total
        def update_lines(self, *args):
            self.paylines_lbl.config(text=f'Paylines: {self.payline_var.get()}')
            self.total_var.set(self.bet_var.get()*self.payline_var.get())
            self.total_lbl.config(text=f'Total Bet: ${self.total_var.get()}')


        # Spin
        def spin(self):
            # Check for insufficient credits
            if self.balance_var.get() < self.total_var.get():
                messagebox.showinfo('Insufficient Credits', 'Not enough credits!')
                return
            
            # Update balance
            self.balance_var.set(self.balance_var.get() - self.total_var.get())
            self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
            
            # Check for game over
            if self.balance_var.get() == 0:
                answer = messagebox.askyesno('GAME OVER', 'Start a new game?')
                if answer:
                    self.balance_var.set(BALANCE)
                    self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
                else:
                    self.quit()
                    


if __name__ == '__main__':
    game = SlotMachine()
    game.mainloop()