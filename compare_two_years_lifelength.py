#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

import logging, csv, re, sys, codecs

#The first section creates functions to add headers to the Wiki-information and puts them into dictionaries
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
    out = process_csv("years/1820", header) #We only look at the information for one specific year (here 1820)
    with open("1820.csv", "w") as file:
        #The first line of the csv-file will include the column-headers "birthYear" and "deathYear"
        content = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        content.writerow(['birthYear', 'deathYear'])
        for person in out:
            # We want to filter out to include only people where birth and death date exist
            # The ratio of indicated date and not known date is similar for most years, so the not-indicated date will equal out
            if 'birthDate' in person and 'deathDate' in person:
                #We are only interested in the years of birth and death, so we want to cut off every additional information on the date
                #The dates sometimes start with the year, for others there are double-quotes before the year
                #The next if-statements cut the birth and death dates according to at which place the year is included in the date
                if person['birthDate'][0] == '1':
                    person['birthDate'] = str(person['birthDate'][0]) + str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3])
                else:
                    person['birthDate'] = str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3]) + str(person['birthDate'][4])
                if person['deathDate'][0] == '1' or person['deathDate'][0] == '2':
                    #People born in the 19th century have a chance of living into the 20th century -> include "2" 
                    person['deathDate'] = str(person['deathDate'][0]) + str(person['deathDate'][1]) + str(person['deathDate'][2]) + str(person['deathDate'][3])
                else:
                    person['deathDate'] = str(person['deathDate'][1]) + str(person['deathDate'][2]) + str(person['deathDate'][3]) + str(person['deathDate'][4])
                #To make it easier to use the dates later on, we exclude the dates that are messed up (the ones that cannot be written as integers) 
                #There are no too many of these so the effort to change those few is too much -> We just drop these dates    
                if person['birthDate'].isdigit() and person['deathDate'].isdigit():
                    content.writerow([int(person['birthDate']), int(person['deathDate'])])



        
        
        