import tkinter as tk
from tkinter import ttk, messagebox
import random


# Starting balance and probability for each symbol to appear (from least to most valuable)
BALANCE = 200
PROBABLILITY = [0.8, 0.05, 0.05, 0.05, 0.05]


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
            
        # List of symbols
        self.symbols_list = [self.a, self.b, self.c, self.d, self.e]
        
        # Set background of entire window
        bg_label = ttk.Label(self, image=self.bg)
        bg_label.place(x=0, y=0)

        # Message displaying information during the game
        self.msg_lbl = ttk.Label(self, text='Welcome to Dino Hunt! Spin to start.', font=('Arial', 18), foreground='white', background='blue', width=35, anchor='center', relief='groove', borderwidth=10)
        self.msg_lbl.grid(row=0, column=1, columnspan=3, pady=10)
        
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
            self.bet_lbl = tk.Label(self, text='Bet: $1', font=('', 16), relief='ridge', borderwidth=5, bg='black', fg='white', width=8)
            self.bet_scl = tk.Scale(self, from_=1, to=10, orient='horizontal', variable=self.bet_var, bd=3, showvalue=0, troughcolor='black', bg='white', command=self.update_bet)
            
            # Paylines and amount-adjust slider for lines
            self.payline_var = tk.IntVar()
            self.payline_var.set(1)
            self.paylines_lbl = tk.Label(self, text='Paylines: 1', font=('', 16), relief='ridge', borderwidth=5, bg='black', fg='white', width=9)
            self.paylines_scl = tk.Scale(self, from_=1, to=3, orient='horizontal', variable=self.payline_var, bd=3, showvalue=0, troughcolor='black', bg='white', command=self.update_lines)

            # Total bet label
            self.total_var = tk.IntVar()
            self.total_var.set(1)
            self.total_lbl = tk.Label(self, text=f'Total Bet: ${self.total_var.get()}', font=('', 16, 'bold'), justify='right', bg='black', fg='white', width=13, relief='sunken', borderwidth=6)

            # Balance widget
            self.balance_var = tk.IntVar()
            self.balance_var.set(BALANCE)
            self.balance_lbl = tk.Label(self, text=f'BALANCE: ${self.balance_var.get()}', font=('', 16), fg='white', borderwidth=10, relief='groove', bg='blue', width=15)
            
            # Buttons widgets and thier appearance
            self.spin_btn = tk.Button(self, text='SPIN', font=('', 16, 'bold'), width=6, height=3, relief='raised', bd=8, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.spin)
            self.cashout_btn = tk.Button(self, text='Cash Out', font=('', 16), relief='raised', bd=5, bg='red', activebackground='#C95858', activeforeground='white', fg='white', command=self.cashout_menu)
            
            # Grid layout for widgets inside of a control frame
            self.bet_lbl.grid(row=0, column=0, padx=10, pady=(10, 2))
            self.bet_scl.grid(row=1,column=0, padx=10)
            self.paylines_lbl.grid(row=0, column=1, padx=10, pady=(10, 2))
            self.paylines_scl.grid(row=1, column=1, padx=10)
            self.total_lbl.grid(row=2, columnspan=2, pady=(10,0))
            self.balance_lbl.grid(row=3, columnspan=2, pady=20)
            self.spin_btn.grid(row=4, columnspan=2)
            self.cashout_btn.grid(row=5, columnspan=2, pady=20) 
            
            # Set variable that stores self.after which controls flashing of a line indicator labels to None
            self.flash = None        
                      
                            
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
            
            # If flashing of labels (line indicators) for winning lines is active, cancel it and revert all lines to back to their default appearance before changing line indicators
            if self.flash:
                self.after_cancel(self.flash)
                self.flash = None
                self.reset_flash(self.flashing_labels)
            # Lines indicator update using ternary conditional operator
            game.line2.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
            game.line22.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
            game.line3.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
            game.line33.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
            
            
        def update_balance(self, multipliers):
            '''Takes in multiplier and updates balance'''
            total_win = 0
            for multiplier in multipliers:
                total_win += self.total_var.get() * multiplier
            self.balance_var.set(self.balance_var.get() + total_win)
            self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
            # Update message, if last element of list passed in is not 0, it means a winning spin
            if multipliers[-1] != 0:
                game.msg_lbl.config(text=f'You won ${total_win}!')
            else:
                game.msg_lbl.config(text=f'Better luck next time.')
            
            
        def spin(self):
            '''Spinning functionality'''
            
            # If flashing of labels (line indicators) for winning lines is active (self.flash not None), cancel it and revert all lines to back to their default appearance (reset_flash())
            if self.flash:
                self.after_cancel(self.flash)
                self.flash = None
                self.reset_flash(self.flashing_labels)
            
            # Check for insufficient credits
            if self.balance_var.get() < self.total_var.get():
                messagebox.showinfo('Insufficient Credits', 'Not enough credits!')
                return
            
            # Update balance (pass in -1 to substract amount of total bet from balance)
            self.update_balance([-1])
            
            # Start spin animation
            self.spin_animation(game.symbols_list, 12)
                    
                    
        def spin_animation(self, symbols, counter):
            '''Takes in symbols list and counter, simulates spinning'''
            
            # Disable bet and paylines adjusting sliders while spinning
            self.paylines_scl.config(state='disabled')
            self.bet_scl.config(state='disabled')
            # Randomlt choose and display symbols counter number of times
            if counter != 0:
                game.msg_lbl.config(text=f'Spinning...')
                game.slot_1x1.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_1x2.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_1x3.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_2x1.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_2x2.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_2x3.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_3x1.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_3x2.canvas.create_image(75, 75, image=random.choice(symbols))
                game.slot_3x3.canvas.create_image(75, 75, image=random.choice(symbols))
                self.after(150, self.spin_animation, symbols, counter - 1)
            else:
                # Activate disabled sliders again and check for winnings
                self.paylines_scl.config(state='active')
                self.bet_scl.config(state='active')
                self.spin_check(self.payline_var.get())
                
                          
        def spin_check(self, lines):
            '''Takes number of payline, simulates spinning of reels and check winnings'''
            
            # Randomly generate 3 lists using nested list comprehension
            reels = [[random.choices(game.symbols_list, PROBABLILITY)[0] for _ in range(3)] for _ in range(3)]
           
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
            
            # List that will store line indicators (lables) from winning lines
            self.flashing_labels = []
            # List that stores winning multipliers, 0 is hardcoded into so update_balance function can check if there are no winning lines for msg_label updates
            win_multipliers = [0]
            
            # Compare symbols in appropriate positions by using all() function which returns true if all items in iterable are true
            for line in range(lines):
                if all(reels[i][line] == reels[j][line] for i, j in [(0, 1), (1, 2)]):
                    # Add line indicators to flashing_labels list
                    if line == 0:
                        self.flashing_labels.append(game.line1)
                        self.flashing_labels.append(game.line11)
                    if line == 1:
                        self.flashing_labels.append(game.line2)
                        self.flashing_labels.append(game.line22)
                    if line == 2:
                        self.flashing_labels.append(game.line3)
                        self.flashing_labels.append(game.line33)
                        
                    # Winnings (multipliers per symbol)
                    match reels[0][line]:
                        case game.a:
                            win_multipliers.append(2)
                        case game.b:
                            win_multipliers.append(3)
                        case game.c:
                            win_multipliers.append(5)
                        case game.d:
                            win_multipliers.append(7)
                        case game.e:
                            win_multipliers.append(9)
            
            # Pass in a list win_multipliers to update_balance function
            self.update_balance(win_multipliers)
            
            # Pass in flashing_lables list to flash_labels() function to simulate flashing of a label             
            if self.flashing_labels:
                self.flash_labels(self.flashing_labels)
                
            # Check for game over and show a message
            if self.balance_var.get() == 0:
                game.msg_lbl.config(text='Game Over')
                answer = messagebox.askyesno('GAME OVER', 'Start a new game?')
                if answer:
                    self.balance_var.set(BALANCE)
                    self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
                    game.msg_lbl.config(text='Welcome to Dino Hunt! Spin to start.')
                else:
                    self.quit()
            
  
        def flash_labels(self, labels_list):
            '''Takes labels (line indicators) from winning lines and swaps background and foreground colors repeatedly using recursion'''
            for lbl in labels_list:
                bg = lbl.cget('background')
                fg = lbl.cget('foreground')
                lbl.config(background=fg, foreground=bg)
            self.flash = self.after(500, self.flash_labels, labels_list)
            
        
        def reset_flash(self, labels_list):
            '''Takes lables (line indicators) from winning (flashing) lines and sets their colors to default ones in case they end up in revert order'''
            for lbl in labels_list:
                lbl.config(background='green', foreground='white')
        
        
        def cashout_menu(self):
            '''Opens cashout menu window'''
            answer1 = messagebox.askyesno('CASH-OUT', 'Finish the game and collect winnings?')
            # If yes (true) open another messagebox
            if answer1:                
                answer2 = messagebox.askyesno('CASH-OUT', f'${self.balance_var.get()} collected! Start a new game?')
                # If clicked on Yes (new game), reset balance and message
                if answer2:
                    self.balance_var.set(BALANCE)
                    self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
                    game.msg_lbl.config(text='Welcome to Dino Hunt! Spin to start.')
                    # If flashing of labels (line indicators) for winning lines is active (self.flash is not None), cancel it and revert all lines to back to their default appearance
                    if self.flash:
                        self.after_cancel(self.flash)
                        self.flash = None
                        self.reset_flash(self.flashing_labels)
                # If clicked No, quit the game (close window)
                else:
                    self.quit()
            
                 


if __name__ == '__main__':
    game = SlotMachine()
    game.mainloop()