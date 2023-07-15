import tkinter as tk
from tkinter import ttk, messagebox
import random


BALANCE = 200



class SlotMachine(tk.Tk):
    '''A class to represent a Slot Machine'''
    def __init__(self):
        '''Constructs all the necessary attributes for slot_machine object'''
        super().__init__()
        
        # Set title and non-resizable root window
        self.title('DINO HUNT')
        self.resizable(False, False)
        
        # Load image files
        self.bg = tk.PhotoImage(file = 'background.png')
        
        # Load symbol images
        try:
            self.a = tk.PhotoImage(file='01.png')
            self.b = tk.PhotoImage(file='02.png')
            self.c = tk.PhotoImage(file='03.png')
            self.d = tk.PhotoImage(file='04.png')
            self.e = tk.PhotoImage(file='05.png')
        except Exception as ex:
            format_ = "Error Occured: {0}.\nArguments: {1!r}"
            error_message = format_.format(type(ex).__name__, ex.args)
            messagebox.showerror('ERROR', error_message)
            return
            
        # Set background of entire window
        bg_label = ttk.Label(self, image=self.bg)
        bg_label.place(x=0, y=0)

        # Message displaying information during the game
        msg_lbl = ttk.Label(self, text='Welcome to Dino Hunt! Spin to start.', font=('Arial', 18), foreground='white', background='blue', width=35, anchor='center', relief='groove', borderwidth=10)
        msg_lbl.grid(row=0, column=1, columnspan=3, pady=10)
        
        # Paylines played (line indicator) widgets
        self.line1 = ttk.Label(self, text='Line 1', foreground='white', background='green', font=('', 18), relief='raised', borderwidth=5)
        self.line2 = ttk.Label(self, text='Line 2', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line3 = ttk.Label(self, text='Line 3', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line11 = ttk.Label(self, text='Line 1', foreground='white', background='green', font=('', 18), relief='raised', borderwidth=5)
        self.line22 = ttk.Label(self, text='Line 2', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line33 = ttk.Label(self, text='Line 3', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line1.grid(row=2, column=0, padx=(10, 0))
        self.line2.grid(row=1, column=0, padx=(10, 0))
        self.line3.grid(row=3, column=0, padx=(10, 0))
        self.line11.grid(row=2, column=4, padx=(0, 10))
        self.line22.grid(row=1, column=4, padx=(0, 10))
        self.line33.grid(row=3, column=4, padx=(0, 10))
        
        # Slot machine's frame encompasing reels (slots)
        slot_frm = ttk.Frame(self, relief='sunken', borderwidth=10)
        slot_frm.grid(row=1, column=1, rowspan=3, columnspan=3, padx=10)



        class Slot:
            '''A class representing slot for a symbol'''
            def __init__(self, container):
                self.canvas = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
                
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
        control_frame.grid(row=4, column=1, columnspan=3, pady=10)
    
    
    
    class ControlFrame(ttk.Frame):
        '''A class to represent controls of the slot machine and its functionality'''
        def __init__(self):
            super().__init__()
            
            self.config(relief='raised', borderwidth=10)
            
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

            # Balance widget
            self.balance_var = tk.IntVar()
            self.balance_var.set(BALANCE)
            self.balance_lbl = ttk.Label(self, text=f'BALANCE: ${self.balance_var.get()}', font=('', 16))
            
            # Buttons widgets and thier appearance
            self.spin_btn = tk.Button(self, text='SPIN', font=('', 16, 'bold'), width=6, height=3, relief='raised', bd=8, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.spin)
            self.cashout_btn = tk.Button(self, text='Cash Out', font=('', 16), relief='raised', bd=5, command=self.cashout_menu)

            # Grid layout for widgets inside of a control frame
            self.bet_lbl.grid(row=0, column=0, padx=(3, 0))
            self.bet_scl.grid(row=1,column=0, padx=(3, 0))
            self.paylines_lbl.grid(row=0, column=1, padx=30)
            self.paylines_scl.grid(row=1, column=1)
            self.total_lbl.grid(row=0, column=2, padx=(0, 3))
            self.balance_lbl.grid(row=2, columnspan=3, pady=20)
            self.spin_btn.grid(row=3, columnspan=3)
            self.cashout_btn.grid(row=4, columnspan=3, pady=20) 

            
        def cashout_menu(self):
            '''Opens cashout menu window'''
            answer = messagebox.askyesno('CASH-OUT', f'${self.balance_var.get()} collected! Start a new game?')
            if answer:
                self.balance_var.set(BALANCE)
                self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
            else:
                self.quit()
            
                            
        def update_bet(self, *args):
            '''Updates text value of bet (bet_lbl) widget based on a scale value and total'''
            self.bet_lbl.config(text=f'Bet: ${self.bet_var.get()}')
            self.total_var.set(self.bet_var.get()*self.payline_var.get())
            self.total_lbl.config(text=f'Total Bet: ${self.total_var.get()}')
            
            
        def update_lines(self, *args):
            '''Updates number of bet lines (paylines), total, and line indicator'''
            self.paylines_lbl.config(text=f'Paylines: {self.payline_var.get()}')
            self.total_var.set(self.bet_var.get()*self.payline_var.get())
            self.total_lbl.config(text=f'Total Bet: ${self.total_var.get()}')
            
            # Lines indicator update using ternary conditional operator
            game.line2.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
            game.line22.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
            game.line3.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
            game.line33.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
            
            
        def spin_reels(self, lines):
            '''Takes number of payline and simulates spinning of reels'''
            symbols = [game.a, game.b, game.c, game.d, game.e]
            probability = [0.4, 0.4, 0.1, 0.05, 0.05]
            
            # Randomly generate 3 lists using nested list comprehension
            reels = [[random.choices(symbols, probability)[0] for _ in range(3)] for _ in range(3)]
           
            # Display randomly choosen symbol on the corresponding slot of the reel (line 1 set to the middle row, line 2 top row, lin 3 bottom row)
            game.slot_1x1.canvas.create_image(75, 75, image=reels[0][1])
            game.slot_1x2.canvas.create_image(75, 75, image=reels[1][1])
            game.slot_1x3.canvas.create_image(75, 75, image=reels[2][1])
            game.slot_2x1.canvas.create_image(75, 75, image=reels[0][0])
            game.slot_2x2.canvas.create_image(75, 75, image=reels[1][0])
            game.slot_2x3.canvas.create_image(75, 75, image=reels[2][0])
            game.slot_3x1.canvas.create_image(75, 75, image=reels[0][2])
            game.slot_3x2.canvas.create_image(75, 75, image=reels[1][2])
            game.slot_3x3.canvas.create_image(75, 75, image=reels[2][2])
            
            # Compare symbols in appropriate positions by using all() function which returns true if all items in iterable are true
            for line in range(lines):
                if all(reels[i][line] == reels[j][line] for i, j in [(0, 1), (1, 2)]):
                    # Winnings (multipliers per symbol)
                    match reels[0][line]:
                        case game.a:
                            self.update_balance(2)
                        case game.b:
                            self.update_balance(3)
                        case game.c:
                            self.update_balance(4)
                        case game.d:
                            self.update_balance(6)
                        case game.e:
                            self.update_balance(8)
        
        
        def update_balance(self, m):
            '''Takes in multiplier and updates balance'''
            self.balance_var.set(self.balance_var.get() + self.total_var.get()*m)
            self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
        

        def spin(self):
            '''Spinning functionality'''
            
            # Check for insufficient credits
            if self.balance_var.get() < self.total_var.get():
                messagebox.showinfo('Insufficient Credits', 'Not enough credits!')
                return
            
            # Update balance (pass in -1 to substract amount of total bet from balance)
            self.update_balance(-1)
            
            # Spin the reels and check for winnings
            self.spin_reels(self.payline_var.get())
            
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