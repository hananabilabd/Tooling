import tkinter as tk
from tkinter import ttk
from OctetFrame import OctetFrame


class RegisterFrame(ttk.Frame):
    """A class for a register. A register can hold multiple octets, depending on its size (width).
    Attributes:
        _width (int): The register size (how many bits in the register).
        _octets (int): Octets in the register.
        _value (int): The value stored in the register bits.
    Methods:
        init_frame(self): Initialize the frame.
        get_dec_value(self): Returns the decimal value of the register.
        get_bin_value(self): Returns the binary value of the register.
        get_hex_value(self): Returns the hexa decimal value of the register.
    """

    def __init__(self, master, width=32):
        super().__init__(master)
        self.__mod_width = 32 if width >= 32 else (width//8 + 1*bool(width%8) ) * 8
        self._width = self.__mod_width
        self._octets = [OctetFrame(i, i + 7, self) for i in range(0, self.__mod_width, 8)]
        self._labels = [ttk.Label(self) for i in range(2)]
        self._register_value = [ 0 for _ in range(0, self.__mod_width, 8)]
        self.__reg_value = 0
        self.__hex_value = tk.StringVar(master=self, value="0x00")
        self._copy_button = ttk.Button(self, text="Copy hex value", command=self.__copy_value)
        self.update_reg_value()

    def init_frame(self):
        """
        Initliazes the frame contents. creates octet frames and place them. Add lables to show registers value
        :return: None
        """
        # Configure OctetFrames
        # print( "There are %d registers."%(len(self._octets)) )
        for i in range(len(self._octets)):
            self._octets[i].init_frame()
            self._octets[i].configure(padding="3 3 3 3", relief="groove", borderwidth=2)
            self._octets[i].grid(row=i//2, column=2-(i%2)^1, columnspan=2)

        # Configure Labels
        reg_txt = self._labels[0]
        reg_val = self._labels[1]

        reg_txt.configure(anchor=tk.W, text="Register Value:")
        reg_txt.grid(row=4, column=0)

        reg_val.configure(textvariable=self.__hex_value, anchor=(tk.CENTER,))
        reg_val.grid(row=4, column=1)

        # configure copy button
        self._copy_button.grid(row=4, column=3)

        return None

    def update_reg_value(self):
        """
        Updates the register value (from all sub octets)
        :return: None
        """
        self.__reg_value = sum(self._register_value)
        hex_val = "%08X"%(self.__reg_value)
        self.__hex_value.set( "0x {} {} {} {}".format(hex_val[:2], hex_val[2:4], hex_val[4:6], hex_val[6:8]) )

    def get_reg_value(self):
        """
        Gets current register hex value
        :return: (int)
        """
        return "".join([byte.strip() for byte in self.__hex_value.get().split()])

    def __copy_value(self):
        """
        Copies the current register value
        :return: None
        """
        hex_val = ''.join([byte.strip() for byte in self.__hex_value.get().split()])
        self.clipboard_clear()
        self.clipboard_append(hex_val)
        self.update()
        return None


if __name__ == '__main__':
    print("This script is a part of RegisterEdit project. It's not supposed to run alone!")

    root = tk.Tk()
    root.title("RegisterFrame Test")
    mf = tk.Frame(root, padx=2, pady=5, relief="groove", borderwidth=3)
    mf.grid(column=0, row=0)
    test = RegisterFrame(mf, 32)
    test.init_frame()
    test.grid(column=0, row=0)
    # print(test._register_value)
    root.mainloop()
