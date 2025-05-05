import networkx as nx
import simpy
import random
from experta import KnowledgeEngine, Rule, Fact, MATCH
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class InfrastructureNode:
    id: str
    type: str
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    network_latency: float = 0.0
    status: str = 'actif'
    dependencies: List[str] = field(default_factory=list)

class ITInfrastructureDigitalTwin(KnowledgeEngine):
    def __init__(self):
        # Initialisation du moteur de connaissance Experta
        super().__init__()
        
        # Création du graphe réseau
        self.graph = nx.DiGraph()
        
        # Types de nœuds
        self.node_types = [
            'serveur', 'base_donnees', 'application', 
            'switch', 'firewall', 'routeur'
        ]
        
        # Stockage des nœuds
        self.nodes: Dict[str, InfrastructureNode] = {}
        
        # Générer l'infrastructure initiale
        self.generate_infrastructure()
    
    def generate_infrastructure(self, num_nodes: int = 50):
        """Génère une infrastructure IT simulée avec des dépendances symboliques"""
        for i in range(num_nodes):
            node_type = random.choice(self.node_types)
            node_id = f"{node_type}_{i}"
            
            # Création d'un nœud avec des attributs dynamiques
            node = InfrastructureNode(
                id=node_id,
                type=node_type,
                cpu_usage=random.uniform(0, 100),
                memory_usage=random.uniform(0, 100),
                network_latency=random.uniform(1, 100),
                status=random.choice(['actif', 'maintenance', 'critique'])
            )
            
            self.nodes[node_id] = node
            self.graph.add_node(node_id, **node.__dict__)
        
        # Création de relations entre nœuds
        self._create_network_dependencies()
    
    def _create_network_dependencies(self):
        """Crée des dépendances réseau entre nœuds"""
        nodes = list(self.graph.nodes())
        for _ in range(len(nodes) * 2):  # Créer environ 2 fois plus de liens que de nœuds
            source = random.choice(nodes)
            target = random.choice(nodes)
            if source != target:
                self.graph.add_edge(source, target, weight=random.uniform(0.1, 1.0))

    @Rule(Fact('infrastructure_scan'))
    def detect_cpu_overload(self):
        """Règle de détection de surcharge CPU"""
        for node_id, node in self.nodes.items():
            if node.cpu_usage > 90:
                self.declare(Fact(type='anomaly', category='CPU_OVERLOAD', node=node_id, severity='haute'))

    @Rule(Fact('infrastructure_scan'))
    def detect_memory_overload(self):
        """Règle de détection de surcharge mémoire"""
        for node_id, node in self.nodes.items():
            if node.memory_usage > 85:
                self.declare(Fact(type='anomaly', category='MEMORY_OVERLOAD', node=node_id, severity='haute'))

    @Rule(Fact('infrastructure_scan'))
    def detect_network_latency(self):
        """Règle de détection de latence réseau"""
        for node_id, node in self.nodes.items():
            if node.network_latency > 50:
                self.declare(Fact(type='anomaly', category='NETWORK_LATENCY', node=node_id, severity='moyenne'))

    @Rule(Fact(type='anomaly', category=MATCH.category), Fact(type='anomaly', category=MATCH.category2))
    def detect_cascading_failure(self, category, category2):
        """Détection de défaillance en cascade"""
        if category != category2:
            self.declare(Fact(type='anomaly', category='CASCADING_FAILURE', severity='critique'))

    def analyze_infrastructure(self):
        """Analyse complète de l'infrastructure"""
        self.reset()
        self.declare(Fact('infrastructure_scan'))
        self.run()
        return [fact for fact in self.facts if fact['type'] == 'anomaly']
    
    def simulate_infrastructure_events(self, env: simpy.Environment):
        """Simulation d'événements dynamiques dans l'infrastructure"""
        while True:
            # Simulation de changements aléatoires
            for node, data in self.graph.nodes(data=True):
                # Mise à jour dynamique des attributs
                data['cpu_usage'] = random.uniform(0, 100)
                data['memory_usage'] = random.uniform(0, 100)
                data['network_latency'] = random.uniform(1, 100)
            
            # Détection d'anomalies
            anomalies = self.symbolic_ai_rules()
            if anomalies:
                print("Anomalies détectées :", anomalies)
            
            # Attente avant prochain cycle
            yield env.timeout(random.uniform(10, 30))

def main():
    # Initialisation du Digital Twin
    digital_twin = ITInfrastructureDigitalTwin()
    
    # Configuration de la simulation
    env = simpy.Environment()
    env.process(digital_twin.simulate_infrastructure_events(env))
    
    # Exécution de la simulation
    env.run(until=300)  # Simulation de 300 unités de temps
    
    # Analyse symbolique de l'infrastructure
    anomalies = digital_twin.analyze_infrastructure()
    
    # Affichage des résultats
    print("\n--- Analyse Symbolic AI de l'infrastructure ---")
    print(f"Nombre total de nœuds : {len(digital_twin.nodes)}")
    print(f"Nombre total de liens : {digital_twin.graph.number_of_edges()}")
    print("\nAnomalies détectées :")
    for anomaly in anomalies:
        print(f"- {anomaly['category']} sur {anomaly['node']} (Sévérité: {anomaly['severity']})")

if __name__ == "__main__":
    main()
