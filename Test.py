import tui
#import QHO_Data_Project.tui as tui
import csv
#welcome()
#error(msg)
#progress()
#menu(variant=0)
#total_records('num_records')
#serial_number()
#observation_dates()

covid_records = []
tui.progress("Loading the Data", 0)
with open("data/covid_19_data.csv") as database:
    csv_reader = csv.reader(database)
    header = next(csv_reader)
    for line in csv_reader:
        covid_records.append(line)
tui.progress("Loading the Data", 100)
print(covid_records)

print(len(covid_records))

x = input("Please select a record between 1 and {}".format(len(covid_records)))