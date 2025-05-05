"""
Module de gestion du graphe NetworkX représentant l’infrastructure IT.
"""

import networkx as nx

class GraphModel:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, node_type, **attributes):
        self.graph.add_node(node_id, type=node_type, **attributes)

    def add_edge(self, src, dst, **attributes):
        self.graph.add_edge(src, dst, **attributes)

    def update_node(self, node_id, **attributes):
        nx.set_node_attributes(self.graph, {node_id: attributes})

    def initialize_demo_infra(self):
        # Exemple d'initialisation d'une infra bancaire simple
        self.add_node('srv_app', 'serveur', CPU_Load=10, RAM_Usage=30)
        self.add_node('db1', 'base', CPU_Load=5, RAM_Usage=20)
        self.add_node('router1', 'routeur', Latency=10)
        self.add_node('app1', 'application')
        self.add_edge('srv_app', 'db1', type='hebergement')
        self.add_edge('srv_app', 'router1', type='reseau')
        self.add_edge('app1', 'srv_app', type='hebergement')

    def initialize_full_stack_infra(self):
        # Frontend
        self.add_node('frontend1', 'front', CPU_Load=15, RAM_Usage=25, Latency=40, logs=[], incidents=[], metrics={})
        self.add_node('frontend2', 'front', CPU_Load=10, RAM_Usage=20, Latency=35, logs=[], incidents=[], metrics={})
        # Load Balancer
        self.add_node('loadbalancer1', 'load_balancer', CPU_Load=5, RAM_Usage=10, Latency=5, logs=[], incidents=[], metrics={})
        # Firewall
        self.add_node('firewall1', 'firewall', CPU_Load=2, RAM_Usage=5, Latency=2, logs=[], incidents=[], metrics={})
        # Backend
        self.add_node('backend1', 'back', CPU_Load=25, RAM_Usage=40, Latency=50, logs=[], incidents=[], metrics={})
        self.add_node('backend2', 'back', CPU_Load=20, RAM_Usage=35, Latency=45, logs=[], incidents=[], metrics={})
        # Base de données
        self.add_node('db1', 'database', CPU_Load=30, RAM_Usage=60, Latency=20, logs=[], incidents=[], metrics={})
        self.add_node('db2', 'database', CPU_Load=28, RAM_Usage=55, Latency=18, logs=[], incidents=[], metrics={})
        # Connexions
        self.add_edge('frontend1', 'loadbalancer1', type='http')
        self.add_edge('frontend2', 'loadbalancer1', type='http')
        self.add_edge('loadbalancer1', 'firewall1', type='tcp')
        self.add_edge('firewall1', 'backend1', type='tcp')
        self.add_edge('firewall1', 'backend2', type='tcp')
        self.add_edge('backend1', 'db1', type='sql')
        self.add_edge('backend2', 'db2', type='sql')
        # Pour la redondance
        self.add_edge('backend1', 'db2', type='sql')
        self.add_edge('backend2', 'db1', type='sql')
        self.add_edge('frontend1', 'frontend2', type='cluster')
        self.add_edge('backend1', 'backend2', type='cluster')
        self.add_edge('db1', 'db2', type='replication')

    def inject_servicenow_incident(self, node_id, incident):
        # Ajoute un incident ServiceNow à un noeud
        node = self.graph.nodes[node_id]
        node.setdefault('incidents', []).append(incident)

    def inject_dynatrace_metrics(self, node_id, cpu=None, ram=None, latency=None):
        # Met à jour les métriques Dynatrace simulées
        node = self.graph.nodes[node_id]
        if cpu is not None:
            node['CPU_Load'] = cpu
        if ram is not None:
            node['RAM_Usage'] = ram
        if latency is not None:
            node['Latency'] = latency
        node.setdefault('metrics', {})['dynatrace'] = {'cpu': cpu, 'ram': ram, 'latency': latency}

    def inject_elasticsearch_log(self, node_id, log):
        # Ajoute un log Elasticsearch simulé
        node = self.graph.nodes[node_id]
        node.setdefault('logs', []).append(log)

    def print_status(self):
        print('--- Etat du graphe ---')
        for n, d in self.graph.nodes(data=True):
            print(f"Node {n}: {d}")
        for u, v, d in self.graph.edges(data=True):
            print(f"Edge {u}-{v}: {d}")
