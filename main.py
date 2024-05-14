import csv

def parse_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            data.append(row)
    return data

# Example usage
filename = 'ek182.csv'
parsed_data = parse_csv(filename)
x = 1
dictp = {}
# Accessing the parsed data
for row in parsed_data:
    answer = row[3]
    print(answer)
    dictp[x] = answer
    x = x + 1
print(dictp)