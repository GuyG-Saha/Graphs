from datetime import datetime

from Graph import *
from fileLoader import FileDataUploader

Gr = FileDataUploader.create_graph_from_csv_data('My first Graph!', 'C:/Users/guyg/PycharmProjects/Graphs/data.csv')

# Gr.add_none_ending_to_leaves()

if Gr.is_dag():
    print('No cycles')
else:
    print('Cycle detected in graph!')

start = datetime.now()

print(Gr.shortest_path('A', 'Z'))
print(Gr.shortest_path('A', 'Z', True))

end = datetime.now()

print(f'Time elapsed for 2 algorithms: {end - start}')

'''
Gr = Graph('My first Graph!')

Gr.add_new_edge('A', 'B', 4.5)
Gr.add_new_edge('A', 'C', 4.2)
Gr.add_new_edge('B', 'C', 3.8)
#Gr.add_new_edge('D', 'A', 7.1)
Gr.add_new_edge('B', 'D', 3.7)
Gr.add_new_edge('C', 'D', 2.3)
Gr.add_new_edge('D', 'E', 4.7)
Gr.add_new_edge('E', 'F', 4.5)
Gr.add_new_edge('D', 'F', 2.4)
Gr.add_new_edge('F', 'G', 8)
Gr.add_new_edge('A', 'G', 8.8)
Gr.add_new_edge('G', 'H', 6.4)


print(Gr.graph)

l_1 = Gr.shortest_path('A', 'H')
print(l_1)


print(Gr.shortest_path('A', 'H', True))

print(Gr.topological_sort())

print(Gr._get_all_leaves())

Gr._add_none_ending_to_leaves()
print(Gr.graph)

print(Gr.is_dag())
'''
