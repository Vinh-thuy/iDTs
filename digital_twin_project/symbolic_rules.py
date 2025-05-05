"""
Module pour les règles métiers déterministes (Symbolic AI).
"""

class SymbolicRules:
    def __init__(self, config):
        self.config = config

    def apply_rules(self, graph_model):
        for node_id, data in graph_model.graph.nodes(data=True):
            if data.get('CPU_Load', 0) > self.config['cpu_threshold']:
                print(f"[ALERTE] CPU élevé sur {node_id}: {data['CPU_Load']}%")
