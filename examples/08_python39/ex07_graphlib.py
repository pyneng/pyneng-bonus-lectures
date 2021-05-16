from graphlib import TopologicalSorter

"""
             |- SW11
     |- SW2 -|- SW12
SW1 -|
     |- SW3 -|- SW13
             |- SW14

"""

topology = {
    "SW1": ["SW2", "SW3"],
    "SW2": ["SW11", "SW12"],
    "SW3": ["SW13", "SW14"]
}

top = TopologicalSorter(topology)
print(list(top.static_order()))
# ['SW11', 'SW12', 'SW13', 'SW14', 'SW2', 'SW3', 'SW1']
