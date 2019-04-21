import tkinter as tk
from tkinter import ttk
from RegisterFrame import RegisterFrame
from OctetFrame import OctetFrame
from ConfirmFrame import ConfirmFrame

def main():

    """
    Create the program GUI.
    :return: None
    """
    # initialize root window
    root = tk.Tk()
    root.title("Resiter Edit Tool")     # window title
    root.resizable(0, 0)                # make it unresizable
    root.attributes("-topmost", True)   # make it always on top

    # initlize the main frame
    main_frame = ttk.Frame(root, padding="3 3 12 12", relief="sunken", borderwidth=3)
    main_frame.grid(row=0, column=0, sticky=tk.NSEW)

    # add register frame and initilize it
    reg_frame = RegisterFrame(main_frame)
    reg_frame.grid(column=0, row=0)
    reg_frame.init_frame()

    # add confirm frame and initilize it
    confirm_frame = ConfirmFrame(main_frame)
    confirm_frame.init_frame()
    confirm_frame.grid(row=1, column=0)

    # start main event loop
    root.mainloop()

if __name__ == '__main__':
    main()
