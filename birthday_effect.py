#Loop for the birthday effect

import datetime, logging, csv, re, sys, codecs

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

# "Yes" for same month, "no" for nor borthday effect, "YAHAA" for death on exactly the same day as birth
birthday_effect_yes = 0
birthday_effect_no = 0
birthday_effect_YAHAA = 0

#Just as for all the other loops, we loop through the files for dofferent years and assign keys to the dictionaries (through headers)
for number in range(1820, 1841):
    header = read_header("h.txt")
    out = process_csv("years/" + str(number), header)
    for person in out:
            if 'birthDate' in person and 'deathDate' in person:
            # We sort out for people that include both death and birth, as those information are only valuable together
                if person['birthDate'][0] == '1' and len(person['birthDate']) >= 10:
                # -> If the date begins with the year but also includes month and day 
                    person['birthMonth'] = str(person['birthDate'][5]) + str(person['birthDate'][6]) 
                    #creates a variable for the month
                    person['birthDay'] = str(person['birthDate'][8]) + str(person['birthDate'][9])
                    #creates a variable for the day (of a month, which is only included in 'birthMonth')
                elif len(person['birthDate']) > 10:
                # If the date does not begin with the year, [0] is mostly a special character and the year follows at [1]
                    person['birthMonth'] = str(str(person['birthDate'][6]) + str(person['birthDate'][7]))
                    person['birthDay'] = str(person['birthDate'][9]) + str(person['birthDate'][10])
                if person['deathDate'][0] == '1' or person['deathDate'][0] == '2' and len(person['deathDate']) >= 10:
                #Same thing for deathDate as stated for birthDate
                    person['deathMonth'] = str(str(person['deathDate'][5]) + str(person['deathDate'][6]))
                    person['deathDay'] = str(person['deathDate'][8]) + str(person['deathDate'][9])
                elif len(person['deathDate']) >= 10:
                    person['deathMonth'] = str(str(person['deathDate'][6]) + str(person['deathDate'][7]))
                    person['deathDay'] = str(person['deathDate'][9]) + str(person['deathDate'][10])
                if 'deathMonth' in person and person['deathMonth'].isdigit() and 'birthMonth' in person and person['birthMonth'].isdigit(): 
                # The next steps only count if the variables exist and are actual numbers
                # i.e. if the order of the date was messer up, the variables could include special characters
                    if person['deathMonth'] == person['birthMonth'] and 'deathDay' in person and 'birthDay' in person and person['deathDay'] == person['birthDay']:
                        print(person['birthDate'])# Here we unfortunately find out, that for most dates month and day are not the real information
                        print(person['deathDate'])#Most of the birth and death dates are the first of January and thus cannot be taken as true information
                        #This adds to a variable only if birth day and death day are exactly the same day
                        birthday_effect_YAHAA += 1
                    elif person['deathMonth'] == person['birthMonth']:
                        #This adds to a variable if birth month and death month are the same
                        birthday_effect_yes += 1
                    else:
                        #This adds to a variable if birthday/birthmonth and deathday/deathmonth do not coincide
                        birthday_effect_no += 1
print(birthday_effect_yes)
print(birthday_effect_no)

            