import tkinter as tk
from tkinter import ttk


class ConfirmFrame(ttk.Frame):
    """A frame for operation control (`OK`, `Clear all`, `Exit`).
    """
    def __init__(self, master):
        super().__init__(master)
        self._exit_button = ttk.Button(self, text="Exit", command = self.tear_down)
        self._clear_button = ttk.Button(self, text="Clear", command = self.clear_all)
        # self._copy_button = ttk.Button(self, text="Copy", command=self.copy_value)

    def init_frame(self):
        """
        Initilize the frame contents
        :return: None
        """
        self._exit_button.grid(row=0, column=2, sticky=tk.W)
        self._clear_button.grid(row=0, column=0, sticky=tk.E)
        # self._copy_button.grid(row=0, column=1, sticky=(tk.W, tk.W))
        return None

    # def copy_value(self):
    #     """
    #     Copies current value to clipboard
    #     :return: None
    #     """
    #     reg_val = self.master.children["!registerframe"].get_reg_value()
    #     self.clipboard_clear()
    #     self.clipboard_append(reg_val)
    #     self.update()

    def clear_all(self):
        """
        Cleaars all bits in the register
        :return: None
        """
        for octet in self.master.children['!registerframe']._octets:
            for button in octet._bits_val:
                button.set(0)
            octet._update_value()
        self.master.children["!registerframe"].update_reg_value()
        return None

    def tear_down(self):
        """
        Closes the window
        :return: None
        """
        self._root().destroy()
        return None


if __name__ == '__main__':
    print("This script is a part of RegisterEdit project. It isn't supposed to run alone!")

    from RegisterFrame import RegisterFrame

    root = tk.Tk()
    root.title("ConfirmFrame Test!")
    mf = ttk.Frame(root, padding="3 3 12 12", relief="raised", borderwidth=3)
    mf.grid(column=0, row=0)

    reg = RegisterFrame(mf)
    reg.grid(column=0, row=0)
    reg.init_frame()

    test = ConfirmFrame(mf)
    test.grid(column=0, row=1)
    test.init_frame()

    root.mainloop()

