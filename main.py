
from Graph import *

Gr = Graph('My first Graph!')

Gr.add_new_edge('A', 'B', 4.5)
Gr.add_new_edge('B', 'C', 3.8)
Gr.add_new_edge('B', 'D', 3.7)
Gr.add_new_edge('C', 'D', 2.3)


print(Gr.graph)
l = Gr.shortest_path('A', 'A')
print(l)
