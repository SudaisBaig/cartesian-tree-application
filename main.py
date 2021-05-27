# This code reads the Data from csv file 
# And fills array covidDataNodes = [] 
# this is a 2D array where each array is a list of comma seperated strings


# Data Set is retrieved from Data Set of John Hopkins University. Below is the Link for reference.
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data 

import csv
from tree import Node

covidDataNodes = []
with open("covid-data.csv", 'r') as file:

    csv_file = csv.reader(file)
    
    for row in csv_file:
        #
        #
        #
        covidDataNodes.append(row)






