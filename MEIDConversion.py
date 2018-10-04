import csv
import pathlib
import HEXtoDEC
import DECtoHEX

sel = input('Enter 0 for HEX to DEC, enter 1 for DEC to HEX.\n')

if sel == '0':
    exec(HEXtoDEC)
elif sel == '1':
    exec(DECtoHEX)
else:
    print('Invalid input.')