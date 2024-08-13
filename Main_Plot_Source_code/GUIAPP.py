import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import draw_plot


class FinanceBotApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Finance Bot')
        # Detail about Size of Window
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f'{w-50}x{h-50}')
        self.root.resizable(0, 0)
        center_x, center_y = w//2, h//2
        # size of monitor in tkiner = (width=1707,heigh=1067)
        button_Plot_Gold = tk.Button(self.root, text='Gold Plot',
                                     command=self.create_plots, bg='#A0FFF5', foreground='#04072C', font=('Arial', 20))
        button_Plot_Gold.place(x=center_x-100, y=center_y+90)

        # Exit button
        button_Exit = tk.Button(self.root, text='Exit', command=lambda: self.root.quit(
        ), bg='#FF0000', foreground='#04072C', font=('Arial', 30))
        button_Exit.place(x=10, y=1370)
        
        

    def create_plots(self):
        self.Warning()
        draw_plot.Create_Plots()

    def Warning(self):
        showinfo('!!هشدار','لطفا هنگام استفاده از نمودارها فایرفاکس رو باز نگه دارید')

    def run(self):
        self.root.mainloop()
    
    def restartapp(self) : 
        self.root.destroy()
        App = FinanceBotApp()
        App.run()


if __name__ == '__main__':
    App = FinanceBotApp()
    App.run()
