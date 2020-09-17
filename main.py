
from Graph import *

Gr = Graph('My first Graph!')

Gr.add_new_edge('A', 'B', 4.5)
Gr.add_new_edge('A', 'C', 4.2)
Gr.add_new_edge('B', 'C', 3.8)
Gr.add_new_edge('B', 'D', 3.7)
Gr.add_new_edge('C', 'D', 2.3)
Gr.add_new_edge('D', 'E', 4.7)
Gr.add_new_edge('E', 'F', 4.5)
Gr.add_new_edge('D', 'F', 2.4)


print(Gr.graph)

l_1 = Gr.shortest_path('A', 'F')
print(l_1)


print(Gr.shortest_path('A', 'F', True))
