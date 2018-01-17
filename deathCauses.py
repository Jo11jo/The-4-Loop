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
# The following obtains a dictionary for the range of years 1820 until 1920, which includes the death causes of the people and the number of people that died from that specific cause
# Creates an empty dictionary which we are going to fill in
deathCause = {}
# In order to count the total number of deaths in this range, we create a variable called "deaths"
deaths = 0
for number in range(1820, 1921):
    header = read_header("h.txt")
    out = process_csv("years/" + str(number), header)
    for person in out: 
# If the header "deathCause" is included in the person, we go on
        if 'deathCause' in person:
# Turns the birth date into a single number, the year of birth            
            if person['birthDate'][0] == '1':
                person['birthDate'] = str(person['birthDate'][0]) + str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3])                   
            else:
                person['birthDate'] = str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3]) + str(person['birthDate'][4])
# Checks if the birth date of each person corresponds to the folder he/she is put in
            # AND if the death cause has already occured in a preceding person, 1 is added to the value of this death cause    
            if int(person["birthDate"]) == number and person["deathCause"] in deathCause:
                deathCause[(person["deathCause"])] += 1
            # AND if the death cause has not been indicated yet, this creates a new key with the new death cause and the value 1
            elif int(person["birthDate"]) == number and person["deathCause"] not in deathCause:
                deathCause[(person["deathCause"])] = 1  
            # Adds a 1 to the variable "deaths" each time, the death cause of a person is indicated            
            deaths += 1
#                