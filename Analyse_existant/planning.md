## ✅ Prérequis indispensables avant lancement de la delivery

### 1. Analyse de l'existant (État des lieux technique)

Avant d'engager la phase de delivery, il est indispensable de :

* Comprendre **l'architecture Django de LISAb**, composant central du backend/API utilisé par Eureka.
* Analyser le **métamodèle actuel du GraphDB** : quels sont les types de nœuds, leurs propriétés, les relations, la profondeur du graphe. Cette connaissance est indispensable pour concevoir et entraîner les modèles IA (symboliques et neuronaux) adaptés au graphe.
* Identifier et cartographier les **flux d'ingestion de données dynamiques** (Discovery, Dynatrace, ServiceNow, Elasticsearch, etc.) : fréquence, format, points d'entrée, orchestration.
* Comprendre les **mécanismes actuels de collecte et traitement des données** dans la stack existante (Domino, pipelines Python, etc.) pour évaluer leur réutilisabilité ou upgrade.

### 2. Répartition des responsabilités et rôles

#### 🎯 Rôle et périmètre du Stream 

* Pilotage  du stream Intelligent iDigital Twin.
* Conception des cas d’usage démontrables avec IA neuronale, symbolique et LLM.
* Définition fonctionnelle des règles de propagation et de modélisation dans le graphe.
* Supervision des stratégies d’intégration entre les briques IA, graphes et interfaces.

#### 🤝 Zones de copilotage

Vous assurez un **copilotage fonctionnel et stratégique** sur les sujets suivants :

* La **modélisation de la base graphe** (choix des nœuds, relations, dynamique du graphe).
* L’**usage de Domino** comme environnement de prototypage IA pour les versions V0/V1.
* La **préparation de la migration vers OpenShift**, en lien avec les exigences de déploiement futur.
* La **définition des flux nécessaires** à l’alimentation des IA (métriques Dynatrace, changements ServiceNow, logs Elasticsearch).

Ces points nécessitent une coordination étroite avec les responsables techniques côté Fabrice afin de garantir la disponibilité, la cohérence et la scalabilité de la chaîne de valeur IA/Graph.

#### 🛠️ Rôle de l’équipe de Fabrice

* Mise à disposition et maintien des **flux entrants** : Dynatrace, ServiceNow, Logs.
* Construction et supervision des **pipelines d’ingestion** : scheduler, orchestrateur, stockage.
* Sécurisation, validation et exposition des données au travers de buckets, API ou interfaces techniques internes.
* Collaboration étroite à organiser dès le Sprint 0 pour garantir la faisabilité des POC.

### 3. Cartographie des plateformes techniques

| Composant      | Rôle principal                                                                          |
| -------------- | --------------------------------------------------------------------------------------- |
| **Domino**     | Plateforme actuelle de prototypage pour IA (batch LLM, entraînement GNN / GECO, tests). |
| **OpenShift**  | Cible d’industrialisation des services IA : APIs, scalabilité, orchestration.           |
| **TigerGraph** | Base de données graphe dynamique (knowledge graph vivant du iDigital Twin).             |

⏳ L’activation d’OpenShift n’est pas encore finalisée : prévoir un **fallback temporaire sur Domino** + DevX pour la phase V0 et V1.

---

## 🚀 Plan de livraison – Sprints cibles

### V0 – Maquette intelligente simulée (0–1 mois)

**Objectif fonctionnel** : démontrer la capacité d’un agent intelligent à raisonner sur un graphe simulé.

**Valeur ajoutée** :

* Preuve de faisabilité.
* Simulation d’un incident et raisonnement associé.
* Dialogue raisonné avec un chatbot agentique.

**Contenu** :

* Graphe simplifié en NetworkX.
* Simulation d’impact (SimPy).
* Premier modèle GNN / GECO sur données synthétiques.
* Agent LLM LangGraph connecté à ce graphe.

---

### V1 – Jumeau numérique vivant (1–2 mois)

**Objectif fonctionnel** : connecter le Digital Twin aux données IT réelles pour analyse, détection, simulation.

**Valeur ajoutée** :

* Connexion aux flux Dynatrace, ServiceNow, Discovery.
* Détection d’incidents réels et visualisation des impacts.
* Raisonnement symbolique sur le graphe dynamique.

**Contenu** :

* Migration vers TigerGraph.
* Application des règles IT.
* Analyse de motifs sur métriques réelles.
* Agent LLM enrichi des données réelles.

---

### V2 – Assistant stratégique interconnecté (2–3 mois)

**Objectif fonctionnel** : proposer un assistant raisonneur intégré aux outils internes (LISAb, Eureka).

**Valeur ajoutée** :

* Simulation de changements.
* Recommandations proactives.
* Rapports synthétiques pour les métiers.

**Contenu** :

* Graphe enrichi de scores prédictifs.
* API exposées sur OpenShift.
* Chatbot opérationnel intégré à Eureka et LISAb.
