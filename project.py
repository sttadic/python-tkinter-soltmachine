import tkinter as tk
from tkinter import ttk


class SlotMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.resizable(False, False)
        
        # Load image file
        self.bg = tk.PhotoImage(file = 'background.png')

        # Set background of entire window
        bg_label = ttk.Label(self, image=self.bg)
        bg_label.place(x=0, y=0)

        # Message displaying information during the game
        msg_lbl = ttk.Label(self, text='Welcome!', font=('Arial', 18), foreground='white', background='black', width=35, anchor='center')
        msg_lbl.grid(row=0, column=0, columnspan=3, pady=10)

        # Slot machine's frame encompasing reels
        slot_frm = ttk.Frame(self, relief='ridge', borderwidth=5)
        slot_frm.grid(row=1, column=0, columnspan=3, padx=10)


        # Reels
        class Reel:
            def __init__(self, container):
                self.canvas = tk.Canvas(container, relief='groove', borderwidth=2, width=150, height=150)
                
                
        reel_1x1 = Reel(slot_frm)
        reel_1x2 = Reel(slot_frm)
        reel_1x3 = Reel(slot_frm)
        reel_2x1 = Reel(slot_frm)
        reel_2x2 = Reel(slot_frm)
        reel_2x3 = Reel(slot_frm)
        reel_3x1 = Reel(slot_frm)
        reel_3x2 = Reel(slot_frm)
        reel_3x3 = Reel(slot_frm)

        # Grid layout for reels
        reel_1x1.canvas.grid(row=0, column=0)
        reel_1x2.canvas.grid(row=0, column=1)
        reel_1x3.canvas.grid(row=0, column=2)
        reel_2x1.canvas.grid(row=1, column=0)
        reel_2x2.canvas.grid(row=1, column=1)
        reel_2x3.canvas.grid(row=1, column=2)
        reel_3x1.canvas.grid(row=2, column=0)
        reel_3x2.canvas.grid(row=2, column=1)
        reel_3x3.canvas.grid(row=2, column=2)


        # Controls frame
        class ControlFrame(ttk.Frame):
            def __init__(self, container):
                super().__init__(container)
                
                self.grid(columnspan=3, pady=10)
                
                # Initalize IntVar to store bet value and set its default value to 1, create bet label and amount-adjust slider for bet
                self.bet_var = tk.IntVar()
                self.bet_var.set(1)
                self.bet_lbl = ttk.Label(self, text='Bet: $1', font=('', 16), justify='left')
                self.bet_scl = ttk.Scale(self, from_=1, to=10, orient='horizontal', variable=self.bet_var, command=self.update_bet)
                
                # Paylines label and amount-adjust slider for lines
                self.payline_var = tk.IntVar()
                self.payline_var.set(1)
                self.paylines_lbl = ttk.Label(self, text='Paylines: 1', font=('', 16), justify='center')
                self.paylines_scl = ttk.Scale(self, from_=1, to=3, orient='horizontal', variable=self.payline_var, command=self.update_lines)

                # Total bet label
                self.total_lbl = ttk.Label(self, text=f'Total Bet: $1', font=('', 16), justify='right', foreground='red', width=11)

                # Balance label
                self.balance_lbl = ttk.Label(self, text='BALANCE: $100', font=('', 16))

                # Buttons widgets and thier appearance
                self.spin_btn = ttk.Button(self, text='SPIN')
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
    
    
            # Function that opens cashout menu window and set it as modal - active widow with .grab_set() module
            def cashout_menu(self):
                cashout_window = tk.Toplevel(self, takefocus=True)
                cashout_window.grab_set()
                amount_lbl = ttk.Label(cashout_window, text=f"Collect $100?", font=('', 20))
                collect_btn = ttk.Button(cashout_window, text='Collect')
                cancel_btn = ttk.Button(cashout_window, text='Cancel')
                amount_lbl.grid(row=0, columnspan=2, padx=20, pady=20)
                cancel_btn.grid(row=1, column=0, pady=(0, 20), padx=10)
                collect_btn.grid(row=1, column=1, pady=(0, 20), padx=10)
                                    
            # Function that updates text value of bet (bet_lbl) widget based on a scale value and total
            def update_bet(self, *args):
                self.bet_lbl.config(text=f'Bet: ${self.bet_var.get()}')
                self.total_lbl.config(text=f'Total bet: ${self.bet_var.get()*self.payline_var.get()}')
                
            # Update number of bet lines (paylines) and total
            def update_lines(self, *args):
                self.paylines_lbl.config(text=f'Paylines: {self.payline_var.get()}')
                self.total_lbl.config(text=f'Total bet: ${self.bet_var.get()*self.payline_var.get()}')


        # Create instance of ControlFrame passing self as the parent
        control_frame = ControlFrame(self)
        
        
        
if __name__ == '__main__':
    game = SlotMachine()
    game.mainloop()