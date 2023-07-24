import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import sys
import pygame


# Starting balance (if set to 0, user will be prompted for balance on game start)
BALANCE = 0

# Probability for each symbol to appear (from least to most valuable)
PROBABLILITY = [0.4, 0.3, 0.15, 0.1, 0.05]

# Symbol multipliers (from most to the least probable)
MULTIPLIERS = {
    'A': 2,
    'B': 3,
    'C': 5,
    'D': 7,
    'E': 10
}


def main():
    '''Instantiate class SlotMachine and start main event loop'''
    game = SlotMachine()
    game.mainloop()
    
    
def play_sound(sound):
    '''Play a sound file'''
    pygame.mixer.init()
    # Load sound files, error handling
    try:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
    except Exception as ex:
        format_ = 'Error Occured: {0}.\nArguments: {1!r}'
        error_message = format_.format(type(ex), f'"{sound}" file does not exist or is corrupted.')
        messagebox.showerror('ERROR', error_message)
        sys.exit(ex)
    

def load_image(image):
    '''Load image file and handle errors'''
    try:
        return tk.PhotoImage(file=image)
    except Exception as ex:
        format_ = "Error Occured: {0}.\nArguments: {1!r}"
        error_message = format_.format(type(ex).__name__, f'"{image}" file does not exist or is corrupted.')
        messagebox.showerror('ERROR', error_message)
        sys.exit(ex)
        

def get_balance():
    '''Get user's balance through dialog box'''
    while True:
        # Prompt user for a balance (up to $500)
        balance = simpledialog.askinteger('BALANCE', 'Please enter your balance (max. $500):')
        if balance in range(1, 501):
            return balance  
        else:
            pass

                  
class SlotMachine(tk.Tk):
    '''A class to represent a Slot Machine'''
    def __init__(self):
        '''Constructs all the necessary attributes for slot_machine object'''
        super().__init__()
        
        # Set balance either to hardcoded amount of gloabal variable or prompt user to enter custom amount in case BALANCE is set to 0
        if BALANCE == 0:
            self.balance = get_balance()
        else:
            self.balance = BALANCE
        
        # Title of the main game window
        self.title('DINO HUNT')
        # Set main window to be non-resizable
        self.resizable(False, False)
        # Initialize variables that store width and height of the main game window
        app_width = 694
        app_height = 1010
        # Determine size of the screen (display)
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()
        # Center main game window against screen (display)
        x = (scr_width/2) - (app_width/2)
        y = (scr_height/2) - (app_height/2)
        self.geometry(f'{app_width}x{app_height}+{round(x)}+{round(y)}')
        
        # Background image
        self.bg = load_image('images/background.png')
        # Paytable image
        self.pt = load_image('images/pay_table.png')
        # Symbol's images
        self.a = load_image('images/01.png')
        self.b = load_image('images/02.png')
        self.c = load_image('images/03.png')
        self.d = load_image('images/04.png')
        self.e = load_image('images/05.png')
        
        # Store symbols in a list
        self.symbols_list = [self.a, self.b, self.c, self.d, self.e]
        
        # Play sound on start
        play_sound('sounds/new_game.wav')
        
        # Set background of entire main game window
        bg_label = ttk.Label(self, image=self.bg)
        bg_label.place(x=0, y=0)

        # Label that will be displaying dynamic messages and info during the game
        self.msg_lbl = ttk.Label(self, text='Welcome to Dino Hunt!  SPIN to start.', font=('Arial', 18), foreground='white', background='blue', width=35, anchor='center', relief='groove', borderwidth=10)
        self.msg_lbl.grid(row=0, column=1, columnspan=3, pady=10)
        
        # Paylines played (line indicator) widgets
        self.line1 = ttk.Label(self, text='Line 1', foreground='white', background='green', font=('', 18), relief='raised', borderwidth=5)
        self.line2 = ttk.Label(self, text='Line 2', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line3 = ttk.Label(self, text='Line 3', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line11 = ttk.Label(self, text='Line 1', foreground='white', background='green', font=('', 18), relief='raised', borderwidth=5)
        self.line22 = ttk.Label(self, text='Line 2', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        self.line33 = ttk.Label(self, text='Line 3', foreground='white', background='red', font=('', 18), relief='sunken', borderwidth=5)
        # Grid layout of line indicators
        self.line1.grid(row=2, column=0, padx=(10, 0))
        self.line2.grid(row=1, column=0, padx=(10, 0))
        self.line3.grid(row=3, column=0, padx=(10, 0))
        self.line11.grid(row=2, column=4, padx=(0, 10))
        self.line22.grid(row=1, column=4, padx=(0, 10))
        self.line33.grid(row=3, column=4, padx=(0, 10))
        
        # Slot machine's frame encompasing pay table on game start and reels (symbol slots) after first spin 
        self.slot_frm = ttk.Frame(self, relief='sunken', borderwidth=10)
        self.slot_frm.grid(row=1, column=1, rowspan=3, columnspan=3, padx=10)
        
        # Show pay table label as background, containing information about the game (multiplier for specific symbol) on game start
        self.pt_lbl = tk.Label(self.slot_frm, image=self.pt, width=494, height=494)
        self.pt_lbl.pack()
        tk.Label(self.slot_frm, text=f'{MULTIPLIERS["A"]}', font=('', 22, 'bold'), borderwidth=8, relief='groove', bg='black', fg='white', width=2).place(x=355, y=80)
        tk.Label(self.slot_frm, text=f'{MULTIPLIERS["B"]}', font=('', 22, 'bold'), borderwidth=8, relief='groove', bg='black', fg='white', width=2).place(x=355, y=160)
        tk.Label(self.slot_frm, text=f'{MULTIPLIERS["C"]}', font=('', 22, 'bold'), borderwidth=8, relief='groove', bg='black', fg='white', width=2).place(x=355, y=240)
        tk.Label(self.slot_frm, text=f'{MULTIPLIERS["D"]}', font=('', 22, 'bold'), borderwidth=8, relief='groove', bg='black', fg='white', width=2).place(x=355, y=320)
        tk.Label(self.slot_frm, text=f'{MULTIPLIERS["E"]}', font=('', 22, 'bold'), borderwidth=8, relief='groove', bg='black', fg='white', width=2).place(x=355, y=400)
        
        # Instance of a ControlFrame (SlotMachine instance passed in as argument)
        control_frame = ControlFrame(self)
        control_frame.grid(row=4, column=1, columnspan=3, pady=10)


class Slots:
    '''A class to represent slots for a symbols'''
    def __init__(self, container):
    
        # Create slots (containers) for symblos
        self.slot_1x1 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_1x2 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_1x3 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_2x1 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_2x2 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_2x3 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_3x1 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_3x2 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        self.slot_3x3 = tk.Canvas(container, relief='groove', borderwidth=6, width=150, height=150)
        
        # Grid layout for slots
        self.slot_1x1.grid(row=0, column=0)
        self.slot_1x2.grid(row=0, column=1)
        self.slot_1x3.grid(row=0, column=2)
        self.slot_2x1.grid(row=1, column=0)
        self.slot_2x2.grid(row=1, column=1)
        self.slot_2x3.grid(row=1, column=2)
        self.slot_3x1.grid(row=2, column=0)
        self.slot_3x2.grid(row=2, column=1)
        self.slot_3x3.grid(row=2, column=2)
        
        
class ControlFrame(ttk.Frame):
    '''A class to represent controls of the slot machine and its functionality'''
    def __init__(self, slot_machine):
        super().__init__()
        
        # Store a reference to the SlotMachine instance
        self.slot_machine = slot_machine
        
        # Configure control frame appearance
        self.config(relief='raised', borderwidth=10)
        
        # Initalize IntVar to store bet value and set its default value to 1, create bet label and amount-adjust slider that controls bet amount
        self.bet_var = tk.IntVar()
        self.bet_var.set(1)
        self.bet_lbl = tk.Label(self, text=f'Bet: ${self.bet_var.get()}', font=('', 16), relief='ridge', borderwidth=5, bg='black', fg='white', width=8)
        self.bet_scl = tk.Scale(self, from_=1, to=10, orient='horizontal', variable=self.bet_var, bd=3, showvalue=0, troughcolor='black', bg='white', command=self.update_bet)
        
        # Paylines and amount-adjust slider that controls which lines are being played
        self.payline_var = tk.IntVar()
        self.payline_var.set(1)
        self.paylines_lbl = tk.Label(self, text=f'Paylines: {self.payline_var.get()}', font=('', 16), relief='ridge', borderwidth=5, bg='black', fg='white', width=9)
        self.paylines_scl = tk.Scale(self, from_=1, to=3, orient='horizontal', variable=self.payline_var, bd=3, showvalue=0, troughcolor='black', bg='white', command=self.update_lines)

        # Total bet label that stores amount being bet on (paylines * bet)
        self.total_var = tk.IntVar()
        self.total_var.set(1)
        self.total_lbl = tk.Label(self, text=f'Total Bet: ${self.total_var.get()}', font=('', 16, 'bold'), justify='right', bg='black', fg='white', width=13, relief='sunken', borderwidth=6)

        # Balance widget
        self.balance_var = tk.IntVar()
        self.balance_var.set(self.slot_machine.balance)
        self.balance_lbl = tk.Label(self, text=f'BALANCE: ${self.balance_var.get()}', font=('', 16), fg='white', borderwidth=10, relief='groove', bg='blue', width=15)
        
        # Buttons widgets for spin and chasout, and thier appearance
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
        
        # Set variable that stores self.after, which controls flashing of a line indicator labels, to None
        self.flash = None
        # Initialize first_spin variable and set its value to 0
        self.first_spin = 0          
               
                        
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
        self.slot_machine.line2.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
        self.slot_machine.line22.config(background='green' if self.payline_var.get() >= 2 else 'red', relief='raised' if self.payline_var.get() >= 2 else 'sunken')
        self.slot_machine.line3.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
        self.slot_machine.line33.config(background='green' if self.payline_var.get() == 3 else 'red', relief='raised' if self.payline_var.get() == 3 else 'sunken')
        
        
    def update_balance(self, multipliers):
        '''Takes in multiplier and updates balance'''
        total_win = 0
        for multiplier in multipliers:
            total_win += self.total_var.get() * multiplier
        self.balance_var.set(self.balance_var.get() + total_win)
        self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
        # Update message, if last element of list passed in is not 0 (means it's a winning spin)
        if multipliers[-1] != 0:
            self.slot_machine.msg_lbl.config(text=f'You won ${total_win}!')
        else:
            self.slot_machine.msg_lbl.config(text=f'Better luck next time.')
        
    
    def spin(self):
        '''Spinning functionality'''
        # Check whether it is a first spin (if not skip this part)
        if self.first_spin == 0:
            # Remove pay table info label that shows on start - to be replaced by the reels
            self.slot_machine.pt_lbl.destroy()
            # Create an instance of the slots (reels)
            self.reels = Slots(self.slot_machine.slot_frm)
            # Set first_spin to 1 so there wouldn't be unnecessary instantiations of a Slots
            self.first_spin = 1
        
        # If flashing of labels (line indicators) for winning lines is active (self.flash not None), cancel it and revert all lines to back to their default appearance (reset_flash())
        if self.flash:
            self.after_cancel(self.flash)
            self.flash = None
            self.reset_flash(self.flashing_labels)
        
        # Check for insufficient credits
        if self.balance_var.get() < self.total_var.get():
            messagebox.showinfo('Insufficient Balance', 'Not enough credits!')
            return
        
        # Update balance (pass in -1 to substract amount of total bet from balance)
        self.update_balance([-1])
        
        # Start spin animation passing in list of symbols and counter that sets how many times symblos will be randomized to simulate spinning
        self.spin_animation(self.slot_machine.symbols_list, 12)
                
                
    def spin_animation(self, symbols, counter):
        '''Takes in symbols list and counter, simulates spinning'''
        # Run this part only once (if counter  == 12)
        if counter == 12:
            # Play spin sound
            play_sound('sounds/spin.wav')
            # Disable controls while spinning
            self.paylines_scl.config(state='disabled')
            self.bet_scl.config(state='disabled')
            self.spin_btn.config(state='disabled')
            self.cashout_btn.config(state='disabled')
        # Randomly choose and display symbols 'counter' number of times
        if counter != 0:
            self.slot_machine.msg_lbl.config(text=f'Spinning...')
            self.reels.slot_1x1.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_1x2.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_1x3.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_2x1.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_2x2.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_2x3.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_3x1.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_3x2.create_image(75, 75, image=random.choice(symbols))
            self.reels.slot_3x3.create_image(75, 75, image=random.choice(symbols))
            self.after(150, self.spin_animation, symbols, counter - 1)
        else:
            # Clear created images and and quit sound mixer to improve performance
            self.clear_images()
            pygame.mixer.quit()
            # Activate disabled controls, call spin_check() function
            self.paylines_scl.config(state='normal')
            self.bet_scl.config(state='normal')
            self.spin_btn.config(state='normal')
            self.cashout_btn.config(state='normal')
            self.spin_check(self.payline_var.get())
            
                        
    def spin_check(self, lines):
        '''Takes number of paylines, simulates spinning (randomizing) of reels one more time taking probablity of each symbol into account, and checks winnings'''
        
        # Create 3 lists or randomly selected symbols using nested list comprehension
        reels = [[random.choices(self.slot_machine.symbols_list, PROBABLILITY)[0] for _ in range(3)] for _ in range(3)]
        
        # Display randomly choosen symbol on the corresponding slot of the reel (line 1 set to the middle row, line 2 top row, lin 3 bottom row)
        self.reels.slot_1x1.create_image(75, 75, image=reels[0][1])
        self.reels.slot_1x2.create_image(75, 75, image=reels[1][1])
        self.reels.slot_1x3.create_image(75, 75, image=reels[2][1])
        self.reels.slot_2x1.create_image(75, 75, image=reels[0][0])
        self.reels.slot_2x2.create_image(75, 75, image=reels[1][0])
        self.reels.slot_2x3.create_image(75, 75, image=reels[2][0])
        self.reels.slot_3x1.create_image(75, 75, image=reels[0][2])
        self.reels.slot_3x2.create_image(75, 75, image=reels[1][2])
        self.reels.slot_3x3.create_image(75, 75, image=reels[2][2])
        
        # List to store line indicators (lables) from winning lines
        self.flashing_labels = []
        # List that stores winning multipliers, 0 is hardcoded so update_balance function can check if there are no winning lines for msg_label updates
        win_multipliers = [0]
        
        # Compare symbols in appropriate positions by using all() function which returns true if all items in iterable are true
        for line in range(lines):
            if all(reels[i][line] == reels[j][line] for i, j in [(0, 1), (1, 2)]):
                # Win sound
                play_sound('sounds/win.wav')
                # Add line indicators to flashing_labels list
                if line == 0:
                    self.flashing_labels.append(self.slot_machine.line1)
                    self.flashing_labels.append(self.slot_machine.line11)
                if line == 1:
                    self.flashing_labels.append(self.slot_machine.line2)
                    self.flashing_labels.append(self.slot_machine.line22)
                if line == 2:
                    self.flashing_labels.append(self.slot_machine.line3)
                    self.flashing_labels.append(self.slot_machine.line33)
                    
                # Add multipliers for each symbol to win_multipliers list
                match reels[0][line]:
                    case self.slot_machine.a:
                        win_multipliers.append(MULTIPLIERS['A'])
                    case self.slot_machine.b:
                        win_multipliers.append(MULTIPLIERS['B'])
                    case self.slot_machine.c:
                        win_multipliers.append(MULTIPLIERS['C'])
                    case self.slot_machine.d:
                        win_multipliers.append(MULTIPLIERS['D'])
                    case self.slot_machine.e:
                        win_multipliers.append(MULTIPLIERS['E'])
        
        # Pass in a list win_multipliers to update_balance function
        self.update_balance(win_multipliers)
        
        # Pass in flashing_lables list to flash_labels() function            
        if self.flashing_labels:
            self.flash_labels(self.flashing_labels)
            
        # Check for game over and show a message
        if self.balance_var.get() == 0:
            # Play game over effect
            play_sound('sounds/game_over.wav')
            # Configure message label to show game over message
            self.slot_machine.msg_lbl.config(text='Game Over', background='red')
            # Prompt user to start a new game or quit
            answer = messagebox.askyesno('GAME OVER', 'Start a new game?')
             # If clicked on Yes start a new game, else quit the game
            if answer:
                self.new_game()
            else:
                sys.exit('Game terminated by user')
        

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
        # Prompt user to confirm cashout
        answer1 = messagebox.askyesno('CASH-OUT', 'Finish the game and collect winnings?')
        # If yes (true) open another messagebox
        if answer1:                
            answer2 = messagebox.askyesno('CASH-OUT', f'${self.balance_var.get()} collected! Start a new game?')
            # If clicked on Yes start a new game
            if answer2:
                self.new_game()
                # If flashing of labels (line indicators) for winning lines is active (self.flash is not None), cancel it and revert all lines to back to their default appearance
                if self.flash:
                    self.after_cancel(self.flash)
                    self.flash = None
                    self.reset_flash(self.flashing_labels)
            # If clicked No, quit the game (close window)
            else:
                sys.exit('Game terminated by user')
                
        
    def new_game(self):
        '''Resets slot machine to its inital state'''
        # Reset or prompt user for balance and update balance label
        if BALANCE == 0:
            self.balance_var.set(get_balance())
        else:
            self.balance_var.set(self.slot_machine.balance)
            self.balance_lbl.config(text=f'Balance: ${self.balance_var.get()}')
        # Update label that shows dynamic messages
        self.slot_machine.msg_lbl.config(text='Welcome to Dino Hunt!  SPIN to start.', background='blue')
        # Reset paylines and update payline's label
        self.payline_var.set(1)
        self.paylines_lbl.config(text=f'Paylines: {self.payline_var.get()}')
        # Reset bet per line amount and update bet label
        self.bet_var.set(1)
        self.bet_lbl.config(text=f'Bet: ${self.bet_var.get()}')
        # Reset total bet and update it's label
        self.total_var.set(1)
        self.total_lbl.config(text=f'Total Bet: ${self.total_var.get()}')
        # Reset line indicators if some are flashing from last spin
        if self.flash:
            self.after_cancel(self.flash)
            self.flash = None
            self.reset_flash(self.flashing_labels)
        lines_list = [self.slot_machine.line2, self.slot_machine.line22, self.slot_machine.line3, self.slot_machine.line33]
        for line in lines_list:
            line.config(background='red', foreground='white', relief='sunken')
        # Set first_spin back to inital value
        self.first_spin = 0
        # Play new game effect
        play_sound('sounds/new_game.wav')
        
    
    def clear_images(self):
        '''Clears created images from each slot'''
        self.reels.slot_1x1.delete('all')
        self.reels.slot_1x2.delete('all')
        self.reels.slot_1x3.delete('all')
        self.reels.slot_2x1.delete('all')
        self.reels.slot_2x2.delete('all')
        self.reels.slot_2x3.delete('all')
        self.reels.slot_3x1.delete('all')
        self.reels.slot_3x2.delete('all')
        self.reels.slot_3x3.delete('all')
                    
        

if __name__ == '__main__':
    main()