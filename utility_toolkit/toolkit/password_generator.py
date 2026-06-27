# A simple password generator

import string
import random as rd

def pass_gen(pass_len: int, upper: bool, lower: bool, num: bool, symbol: bool) -> str:

    digits = string.digits
    lchar = string.ascii_lowercase
    uchar = string.ascii_uppercase
    schar = string.punctuation

    available_chr = ""

    if(pass_len < 8):
        raise ValueError("Password length must be at least 8.")

    if(upper or lower or num or symbol):
        if(upper):
            available_chr += uchar
        if(lower):
            available_chr += lchar
        if(num):
            available_chr += digits
        if(symbol):
            available_chr += schar
        
    if(not upper and not lower and not num and not symbol):
        raise ValueError("At least one character type must be selected.")

    password = "".join(rd.choice(available_chr) for _ in range(pass_len))

    return password