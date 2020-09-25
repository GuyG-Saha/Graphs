import csv
import os

from Graph import *
from Edge import Edge

START_VERTEX = 0
END_VERTEX = 1
WEIGHT = 2
DEL = ','


class FileDataUploader:

    @staticmethod
    def create_graph_from_csv_data(desc: str, path: str) -> Graph:
        new_graph = Graph(desc)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=DEL)
            line_count = 0
            for row in csv_file:
                if line_count > 0:
                    new_graph.add_new_edge(row.split(DEL)[START_VERTEX], row.split(DEL)[END_VERTEX],
                                           float(row.split(DEL)[WEIGHT]))
                line_count += 1

            print(new_graph)
            print(new_graph.graph)
            return new_graph



'''
PATH = 'C:/Users/guyg/PycharmProjects/Graphs/data.csv'

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

    G.add_new_edge('A', 'B')
    print(G.num_edges)
'''