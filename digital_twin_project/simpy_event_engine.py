"""
Moteur SimPy pour la simulation d’événements sur le graphe.
"""

import simpy

class SimPyEventEngine:
    def __init__(self, graph_model):
        self.env = simpy.Environment()
        self.graph_model = graph_model

    def run(self, until=100):
        self.env.run(until=until)

    def cpu_load_event(self, node_id, load_increase, duration):
        def process():
            node = self.graph_model.graph.nodes[node_id]
            node['CPU_Load'] = node.get('CPU_Load', 0) + load_increase
            yield self.env.timeout(duration)
            node['CPU_Load'] -= load_increase
        self.env.process(process())

    def simulate_load(self, node_id):
        self.cpu_load_event(node_id, 90, 10)
