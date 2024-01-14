import csv

# with open("day25/weather_data.csv", mode="r") as filename:
#     line = filename.readline()
#     while line:
#         lines.append(line.strip())
#         line = filename.readline()

with open("day25/weather_data.csv") as data_file:

    data = csv.reader(data_file)
    temperatures = []
    i = 0
    for row in data:
        if i > 0:
            temperatures.append(int(row[1]))
        i+=1

print(temperatures)