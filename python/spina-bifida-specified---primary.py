# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"P11y.00","system":"readv2"},{"code":"7043y00","system":"readv2"},{"code":"P100.00","system":"readv2"},{"code":"P118000","system":"readv2"},{"code":"P100000","system":"readv2"},{"code":"Pyu0400","system":"readv2"},{"code":"P110z00","system":"readv2"},{"code":"P110000","system":"readv2"},{"code":"P10y.00","system":"readv2"},{"code":"A49.8","system":"readv2"},{"code":"A49.9","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spina-bifida-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["spina-bifida-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["spina-bifida-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["spina-bifida-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
