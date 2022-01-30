"""
This module is responsible for visualising the data using Matplotlib.
"""
import matplotlib.pyplot as plt
"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here

def cases_pie(region):
    x = list(region.keys())
    y = []
    for keys in region.values():
        y.append(len(keys))
    plt.pie(x,y)
    plt.show()


def countries_bar(top):
