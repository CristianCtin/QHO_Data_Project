#import tui
#import process
from process import *
#import main
from main import *
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
def run():
    tui.welcome()
    tui.progress("Loading the Data", 0)
    with open("data/covid_19_data.csv") as database:
        csv_reader = csv.reader(database)
        header = next(csv_reader)
        for line in csv_reader:
            covid_records.append(line)
    tui.progress("Loading the Data", 100)
    while True:
        option = tui.menu(variant=0)
        if option == 1:
            tui.progress("Operation has started", 0)
            tui.progress("Operation has completed", 101)
            opt = tui.menu(variant=1)
            if opt == 1:
                tui.progress("Process has started", 0)
                process.x()
                print(x)
                tui.progress("Process completed", 101)
            if opt == 2:
                tui.progress("Process has started", 0)
                process.y()
                tui.progress("Retrieved records", 55)
                tui.progress("Process completed", 101)
































# covid_records = []
# tui.progress("Loading the Data", 0)
# with open("data/covid_19_data.csv") as database:
#     csv_reader = csv.reader(database)
#     header = next(csv_reader)
#     for line in csv_reader:
#         covid_records.append(line)
#
#     tui.progress("Loading the Data", 100)
#     while True:
#         option = tui.menu(variant=0)
#         if option == 1:
#             tui.progress("Operation has started", 0)
#             opt = tui.menu(1)
#             if opt == 1:
#                 print(tui.menu(1))
#             tui.progress("Operation has completed", 101)










# tui.progress("Loading the Data", 100)
# print(covid_records)
#
# print(len(covid_records))


#x = input("Please select a record between 1 and {}".format(len(covid_records)))


# def display_record(record, cols=None):
#     if len(cols) == 0:
#         print(record)
#     elif len(cols) != 0:
#         for index in cols:
#             print(record[index])
