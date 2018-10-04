import csv
import pathlib

main_in = input('Please type the path of the .csv file with the HEX data in it.\n')
main_in_path = pathlib.PureWindowsPath(main_in)

with open(main_in_path, newline='') as f:
    reader = csv.reader(f)
    codesout = list(f)
with open('codes_dec.csv', 'w', newline='') as out:
    outwriter = csv.writer(out, delimiter=' ',quotechar='|')
    for codes in codesout:
        a = codes[0:8]
        b = '0' + codes[8:14]
        c = int(a,16)
        d = int(b,16)
        e = '0' + str(c) + '0' + str(d)
        outwriter.writerow([e])