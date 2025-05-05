# Digital Twin IT Project (Prototype Version with NetworkX)

## Objectif

Construire une première stack de Digital Twin pour l'infrastructure IT bancaire, utilisant :

- **NetworkX** pour modéliser l'infrastructure sous forme de graphe local,
- **SimPy** pour simuler des événements (pannes, charges, incidents),
- **Symbolic AI** pour définir et appliquer des règles métiers déterministes,
- **LLM Supervisor** pour analyser, expliquer, et enrichir les événements critiques.

Le tout conçu pour être modulaire, extensible et facilement migrable vers TigerGraph + GNN dans une future version.

---

## 📂 Arborescence souhaitée

/digital_twin_project/
│
├── graph_model.py              # Construction et gestion du graphe NetworkX
├── simpy_event_engine.py       # Simulation d’événements avec SimPy
├── symbolic_rules.py           # Définition et application de règles métiers
├── llm_supervisor.py            # Interface pour interroger un LLM externe
├── scenarios_generator.py      # Génération automatique de scénarios d’incidents
│
├── config.py                   # Fichier de configuration du projet
├── main.py                     # Orchestration principale
│
└── README.md                   # Ce fichier


---

## 📌 Spécifications techniques

### 1. Infrastructure IT (NetworkX)

- Utiliser `networkx` pour :
  - Créer des **nœuds** (serveur, base, application, routeur),
  - Créer des **arêtes** (liens fonctionnels : hébergement, communication réseau),
  - Associer des **attributs dynamiques** aux nœuds (CPU Load, RAM Usage, Latency...).

---

### 2. Simulation d'événements (SimPy)

- Implémenter un moteur SimPy qui :
  - Simule des montées en charge, pannes réseau, crash base de données,
  - Met à jour les attributs dynamiques du graphe NetworkX en fonction des événements.

---

### 3. Règles Métier (Symbolic AI)

- Créer un module de **règles simples**, par exemple :
  - `IF CPU_Load > 85% for 5 minutes THEN Trigger Incident`.
  - `IF Network_Latency > 200ms THEN Raise Performance Alert`.

- Les règles doivent s'appliquer **à chaque étape SimPy**.

---

### 4. Superviseur Intelligent (LLM)

- Développer un module capable de :
  - Recevoir un **état du graphe ou un événement critique**,
  - Interroger un **LLM externe** (ex: OpenAI GPT-4, Ollama) pour :
    - **Résumer** l'état du système,
    - **Proposer** des actions correctrices,
    - **Générer** de nouveaux scénarios "what-if" pour les tests.

---

### 5. GNN (Placeholder)

- Créer un fichier `gnn_predictor.py` vide pour préparer l'intégration d'un modèle de Graph Neural Network (GNN) à moyen terme.

---

## 🧠 Mode de fonctionnement global

- `main.py` :
  1. Initialise le graphe avec NetworkX.
  2. Lance SimPy pour exécuter des événements sur les nœuds.
  3. Applique les règles Symbolic après chaque événement.
  4. Appelle le LLM Supervisor si un incident critique est détecté.
  5. (Plus tard) Prédira des anomalies avec le GNN.

---

## ⚙️ Librairies Python utilisées

- `networkx`
- `simpy`
- `openai` (ou API LLM compatible pour appels supervisés)
- (optionnel) moteur de règles maison ou librairie symbolique simple.

---

## 📣 Consignes de développement

- Les modules doivent être **modulaires** et **facilement extensibles**.
- L’appel au LLM doit être **asynchrone** pour ne pas bloquer la simulation.
- Préparer dès maintenant le projet pour pouvoir **migrer** vers TigerGraph + GNN plus tard sans réécriture majeure.

---

# 🚀 Résultat attendu

- Infrastructure modélisée sous forme de graphe dynamique,
- Simulation d'événements IT réalistes,
- Détection d'anomalies par règles métiers,
- Appels LLM pour enrichir les diagnostics et recommandations,
- Stack simple et modulaire pour évoluer ensuite vers plus d'intelligence.

---

# ✨ Roadmap future (non nécessaire pour la première version)

- Migrer NetworkX vers TigerGraph pour la production.
- Remplacer le moteur de règles par une Symbolic AI plus robuste (ex: Pyknow).
- Intégrer un GNN pour prédiction proactive d'incidents.
- Déployer les dashboards de supervision interactifs.

---