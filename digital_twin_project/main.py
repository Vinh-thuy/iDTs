"""
Orchestration principale du prototype Digital Twin IT.
"""

from config import CONFIG
from graph_model import GraphModel
from simpy_event_engine import SimPyEventEngine
from symbolic_rules import SymbolicRules
from llm_supervisor import LLMSupervisor
from scenarios_generator import ScenariosGenerator


def main():
    # Initialisation
    graph = GraphModel()
    rules = SymbolicRules(CONFIG)
    llm = LLMSupervisor(CONFIG['llm_api_url'])
    scenarios = ScenariosGenerator()
    engine = SimPyEventEngine(graph)

    # 1. Initialiser une stack complète réaliste
    graph.initialize_full_stack_infra()
    graph.print_status()

    # 2. Injecter un incident ServiceNow sur backend1
    graph.inject_servicenow_incident('backend1', {
        'id': 'INC12345',
        'type': 'incident',
        'description': 'Crash applicatif',
        'severity': 'critical',
        'source': 'ServiceNow'
    })

    # 3. Simuler des métriques Dynatrace sur frontend1
    graph.inject_dynatrace_metrics('frontend1', cpu=95, ram=80, latency=120)

    # 4. Ajouter un log Elasticsearch sur db1
    graph.inject_elasticsearch_log('db1', {
        'timestamp': '2025-04-26T23:17:00',
        'level': 'ERROR',
        'message': 'Erreur de réplication',
        'source': 'Elasticsearch'
    })

    # 5. Afficher l'état du graphe après injection
    graph.print_status()

    # 6. Appliquer les règles métiers (alerte CPU, etc.)
    rules.apply_rules(graph)

if __name__ == "__main__":
    main()
