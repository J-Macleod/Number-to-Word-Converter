from datetime import date, datetime

from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

import os
import ctypes
from ctypes import wintypes
import msvcrt
import subprocess

from num2words import num2words

ctypes.windll.kernel32.SetConsoleTitleW("Number to Word Converter - Jam - 2022")
os.system('mode con: cols=100 lines=40')
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

maximize_console(lines=None)

init(autoreset=True)

global r
global g
global b
global w
global y
global c
global m
global bl

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
w = Fore.WHITE
y = Fore.YELLOW
c = Fore.CYAN
m = Fore.MAGENTA
bl = Fore.BLACK

global rbg
global gbg
global bbg
global wbg
global ybg
global cbg
global mbg

rbg = Back.RED
gbg = Back.GREEN
bbg = Back.BLUE
wbg = Back.WHITE
ybg = Back.YELLOW
cbg = Back.CYAN
mbg = Back.MAGENTA

global bright
global dim

bright = Style.BRIGHT
dim = Style.DIM

def p(t, color):
    text = color + t
    return text

def bg(t, color):
    text = color + t
    return text

def sty(t, level):
    text = level + t
    return text

fix = '\033[0m'

print("")
print(sty(p(" Number to Word Converter | by Jam | 2022", g), bright))
print("")

def main():
    
    up = True

    while up:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        number = input(p(" Number: ", c) + fix)
        try:
            print(p(" Word: ", c) + fix + num2words(float(number)))
        except:
            print(p(" Error with input or conversion.", r))

main()
