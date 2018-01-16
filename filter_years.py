#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

import json, logging, csv, re, sys, codecs

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

if __name__ == "__main__":
    header = read_header("h.txt")
    out = process_csv("years/1820", header)
    with open("1820.csv", "w") as file:
        content = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        content.writerow(['birthYear', 'deathYear'])
        for row in out:
            if 'birthDate' in row and 'deathDate' in row:
                if row['birthDate'][0] == '1':
                    row['birthDate'] = str(row['birthDate'][0]) + str(row['birthDate'][1]) + str(row['birthDate'][2]) + str(row['birthDate'][3])
                else:
                    row['birthDate'] = str(row['birthDate'][1]) + str(row['birthDate'][2]) + str(row['birthDate'][3]) + str(row['birthDate'][4])
                if row['deathDate'][0] == '1' or row['deathDate'][0] == '2':
                    row['deathDate'] = str(row['deathDate'][0]) + str(row['deathDate'][1]) + str(row['deathDate'][2]) + str(row['deathDate'][3])
                else:
                    row['deathDate'] = str(row['deathDate'][1]) + str(row['deathDate'][2]) + str(row['deathDate'][3]) + str(row['deathDate'][4])
                    
                if row['birthDate'].isdigit() and row['deathDate'].isdigit():
                    content.writerow([int(row['birthDate']), int(row['deathDate'])])



        
        
        