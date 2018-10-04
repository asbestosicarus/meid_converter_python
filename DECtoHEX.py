#conversion from DEC to HEX for MEID numbers
import csv
import pathlib

main_in = input('Please type the path of the .csv file with the DEC data in it.\n')
main_in_path = pathlib.PureWindowsPath(main_in)

with open(main_in_path, newline='') as f: #opens the .csv stored in main_in_path
    reader = csv.reader(f)
    codesout = list(f) #imports the data into a list

with open('codes_hex.csv', 'w', newline='') as out: #creates new .csv file for storage of HEX codes
    outwriter = csv.writer(out, delimiter=' ',quotechar='|')
    for codes in codesout:
        a = codes[1:10]
        b = codes[11:]
        c = hex(int(a))
        d = hex(int(b))
        e = str(c[2:]) + str(d[2:])
        outwriter.writerow([e]) #writes to new .csv