import matplotlib.pyplot as plt
import csv

def parse_line(line):
    line = line.strip()
    items = line.split(", ")
    values = []
    for item in items:
        values.append(item.split(": ")[1])
    return values

def to_csv(x, y):
    file = open("t1_data_2.csv", "w")
    writer = csv.writer(file)
    for i in range(len(x)):
        line = [x[i], y[i]]
        writer.writerow(line)
    file.close()

if __name__ == '__main__':
    f = open("./task1_result")  # open file
    lines = f.readlines()   # array of lines

    digest_sizes = []
    collision_time = []
    number_inputs = []

    for line in lines:
        values = parse_line(line)
        digest_sizes.append(values[0])
        collision_time.append(values[1])
        number_inputs.append(values[2])

    f.close()

    # to csv then plotted in excel
    to_csv(digest_sizes, number_inputs)