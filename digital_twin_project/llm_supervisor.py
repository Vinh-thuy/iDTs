"""
Interface pour la supervision intelligente via LLM externe.
"""

class LLMSupervisor:
    def __init__(self, api_url):
        self.api_url = api_url

    def analyze(self, graph_state):
        # À implémenter : appel à l’API LLM
        pass
