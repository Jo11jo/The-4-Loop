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

final_information = {}
for number in range(1820, 1921):
    if __name__ == "__main__":
        header = read_header("h.txt")
        out = process_csv("years/" + str(number), header)
        every_year = []
        for person in out:
            
            if 'birthDate' in person and 'deathDate' in person:
                    if person['birthDate'][0] == '1':
                        person['birthDate'] = str(person['birthDate'][0]) + str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3])
                    else:
                        person['birthDate'] = str(person['birthDate'][1]) + str(person['birthDate'][2]) + str(person['birthDate'][3]) + str(person['birthDate'][4])
                    if person['deathDate'][0] == '1' or person['deathDate'][0] == '2':
                        person['deathDate'] = str(person['deathDate'][0]) + str(person['deathDate'][1]) + str(person['deathDate'][2]) + str(person['deathDate'][3])
                    else:
                        person['deathDate'] = str(person['deathDate'][1]) + str(person['deathDate'][2]) + str(person['deathDate'][3]) + str(person['deathDate'][4])
                        
                    if person['birthDate'].isdigit() and person['deathDate'].isdigit():
                        age = int(person['deathDate']) - int(person['birthDate'])
                        every_year.append(age) 
        final_information[str(number)] = numpy.mean(every_year)
        
with open("years_means.csv", "w") as file:
    content = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    content.writerow(['year', 'lifetime_mean'])
    for key in final_information:
                content.writerow([key, final_information[str(key)]])