import csv
import os

from Graph import *
from Edge import Edge

PATH = 'C:/Users/guyg/PycharmProjects/Graphs/data.txt'

G = Graph('Graph from file')

with open(PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_file:
        if line_count > 0:
            G.add_new_edge(row.split(',')[0], row.split(',')[1], float(row.split(',')[2]))
        line_count += 1

    print(G)
    print(G.graph)

    destinations = ['C', 'E', 'F', 'G']
    for d in destinations:
        print(G.shortest_path('A', d))