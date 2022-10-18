import csv

def read_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        bookreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in bookreader:
            data.append([row[0], row[1], row[2], row[3], row[4]])
    return data


def write_data(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        bookwriter = csv.writer(csvfile, delimiter='\t',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in data:
            bookwriter.writerow([line[0], line[1], line[2], line[3], line[4]])
