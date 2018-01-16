# -*- coding: utf-8 -*-
import json, logging, csv, re, sys, codecs, numpy

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

# This creates a dictionary that contains the years as keys and a list of two numbers as values: first the people for which birth place = death place and then the people for which birth place does not equal death place
# Creates an empty dictionary
birth_death_Place = {}
# Selects the years 1820 to 1920 in order to loop over them
for number in range(1820, 1921):
    if __name__ == "__main__":
        header = read_header("h.txt")
        out = process_csv("years/" + str(number), header)
# Creates an empty list as a value for each key (the year)
        birth_death_Place[str(number)] = []
# Creates two new variables, birth place equals death place and birth place does not equal death place
        birth_death_same = 0
        birth_death_notsame = 0
        for person in out:
# Selects the year of the birth date
            if person['birthDate'][0] == '1':
                    person['birthDate'] = str(person['birthDate'][0]) + str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3])
            else:
                    person['birthDate'] = str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3]) + str(person['birthDate'][4])
# Selects the people for which the following is true:
# birth place and death place are indicated 
# birth year equals the year file we are looking at
            # AND birth place equals death place                    
            if "birthPlace" in person and "deathPlace" in person and int(person["birthDate"]) == number and person["birthPlace"] == person["deathPlace"]:
                birth_death_same += 1
            # AND birth place does not equal death place    
            elif "birthPlace" in person and "deathPlace" in person and int(person["birthDate"]) == number and person["birthPlace"] != person["deathPlace"]:   
                birth_death_notsame += 1
        # Creates a list with the number of people per year, whose birth and death place are equal and are not equal
        year_list = [birth_death_same, birth_death_notsame]
        # Adds this list as a value to the dictionary
        birth_death_Place[str(number)].append(year_list)
# Creates a csv file with three columns: year, birth_death_same, birth_death_notsame
with open("birth_death_places.csv", "w") as file:
        content = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        content.writerow(['year', 'birth_death_same', 'birth_death_notsame'])
        for key in birth_death_Place:
            content.writerow([key, birth_death_Place[key][0][0], birth_death_Place[key][0][1]])
