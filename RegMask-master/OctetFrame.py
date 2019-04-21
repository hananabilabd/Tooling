import tkinter as tk
from tkinter import ttk

class OctetFrame(ttk.Frame):
    """A class for a register octet (8bits). Subclass of ttk.Frame.
    Attributes:
        start_bit (int): defines the starting bit number.
        send_bit(int): defines the starting bit number.
        _bits (list): a list of bit values.
    Methods:
        init_frame(self): Initializes the frame.
        get_dec_value(self): Returns the decimal value of the octet bits.
        get_bin_value(self): Returns the binary value of the octet bits.
        get_hex_value(self): Returns the hexa decimal value of the octet bits.
    """

    def __init__(self, start_bit, end_bit, master=None):
        super().__init__(master)
        self._start_bit = start_bit     # register starting bit number
        self._end_bit = end_bit         # register end bit number
        self._bits = [ttk.Button(self) for _ in range(8)]   # a list of bit buttons
        self._bits_val = [tk.IntVar(0) for _ in range(8)]   # a list of bit variables
        self._octet_val = tk.IntVar(0)          # an integer variable to hold the octet value
        self.__partial_value = tk.IntVar(0)     # an integer variable to hold the octet's within the register

        # print("start: %d, end: %d"%(self._start_bit, self._end_bit))
        # print(*self._bits)
        # print(*self._bits_val)

    def init_frame(self):
        """
        Initilize the octet frame. Adds 8 buttons for each bit, 8 lables for each button.
        :return: None
        """
        # add start bit lable at (0,0), end bit label at (0,7)
        for i in range(self._start_bit, self._end_bit+1):
            ttk.Label(self, text=str(i)).grid(row=0, column=7 -(i%8))

        # add bit buttons at (1,i) i=[0,7]
        for bit in range(8):
            self._bits[bit].grid(row=1, column=bit)
            self._bits[bit].configure(width=3, textvar=self._bits_val[ 7 - bit])
            self._bits[bit].configure(command=lambda x = (7 - bit): self._toggle_bit(x))

    def _toggle_bit(self, bit_number):
        """
        Toggles button (bit) value (by XOR with 1)
        Then updates the register value
        :return: None
        """
        # get the bit value, toggle it, assign the new value then update the register's value
        bit_val = self._bits_val[bit_number].get()
        bit_val ^= 1
        self._bits_val[bit_number].set(bit_val)
        self._update_value()
        return None

    def _update_value(self):
        """
        A private method to update the octet's value each time a bit is toggled.
        And also updates the RegisterFrame's value.
        :return: None
        """
        # update the value of _octet_value from _bits_val
        val = 0
        bits = [self._bits_val[i].get() for i in range(8)]
        for i in range(8):
            val += (bits[i]<<i)
        self._octet_val = val
        # update RegisterFrame according to the change in OctetFrame value change
        self.master._register_value[self._start_bit//8] = self._octet_val << self._start_bit
        self.master.update_reg_value()
        return None

    def get_dec_value(self):
        """
        Returns the decimal value of the current register contents.
        :return: self._octet_val.get() (int)
        """
        return self._octet_val

    def get_bin_value(self):
        """
        Returns the binary representation of the value in the register.
        :return: (string) 0b + 8 bit binary string
        """
        bits = [self._bits_val[i].get() for i in range(8)]
        return '0b'+''.join([str(i) for i in bits])

    def get_hex_value(self):
        """
        Returns the hexadecimal representation of the value in the register.
        :return: (string) 0x 2 hexa digits
        """
        return "0x%02x"%(self._octet_val)


if __name__ == '__main__':
    print("This file is a part of RegisterEdit project. It isn't supposed to run alone!")
    """Begin OctetFrame Test"""

    reg_width = 32

    root = tk.Tk()
    root.title("OctetFrame Test")
    mf = ttk.Frame(root)
    mf.grid(row=0, column=0)
    mf._register_value = [0]*(reg_width//8 + 1*bool(reg_width%8) )
    mf._update_reg_value = print    # the actual function *is not* print
    frames = [OctetFrame(i, i+7, mf) for i in range(0, reg_width, 8)]
    print( "There are %d frames." %(len(frames)) )

    for i in range(len(frames)):
        print("frame no:",i)
        frames[i].grid(row=i, column=0)
        frames[i].init_frame()
        print("frame %d position: (%d, %d)"%(i, i, i))
        # frames[i].children["!button8"].state(["disabled"])

    root.mainloop()

