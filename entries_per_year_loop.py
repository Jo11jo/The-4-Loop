# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header):
    out=[]
    stdin = file == "-"
    fd = sys.stdin if stdin else codecs.open(file, 'r', 'UTF-8')
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

# The variable 'entries per year' counts the people for whom the birth year is the same as indicated by the file
    # This way we sort our all the wrongly assigned entries
entries_per_year = 0
for number in ("years\\1500"):
    if __name__ == "__main__":
        header = read_header("h.txt")
        out = process_csv("years\\1500", header)
        for person in out: 
            #The next few steps select only the part of the birth date that indicates the year  (birth date starts either with the year or with double quotes)
            if person['birthDate'][0] == '1':
                    person['birthDate'] = str(person['birthDate'][0]) + str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3])                   
            else:
                    person['birthDate'] = str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3]) + str(person['birthDate'][4])
            if int(person["birthDate"]) == 1500:
                    entries_per_year += 1