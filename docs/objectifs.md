# Hypothèses pour la création du Digital Twin IT

Ce document formalise les hypothèses techniques, fonctionnelles et méthodologiques sur lesquelles repose la première version du projet de Digital Twin IT bancaire.

---

## 1. Hypothèses Techniques

- **Modélisation de l'infrastructure** :  
  L'infrastructure IT (serveurs, bases de données, applications, réseaux) est modélisée comme un **graphe orienté** utilisant **NetworkX** pour le prototypage.

- **Simulation dynamique** :  
  **SimPy** est utilisé pour orchestrer des événements dynamiques (incidents, montées en charge, pannes réseau) qui modifient l'état des entités dans le graphe.

- **Détection basée sur règles symboliques** :  
  Un moteur de **Symbolic AI** en Python évalue des conditions métier déterministes pour détecter les anomalies sur l'infrastructure.

- **Enrichissement intelligent avec LLM** :  
  Un **LLM externe** est utilisé pour :
  - Résumer les événements critiques,
  - Proposer des stratégies de correction ou de mitigation,
  - Générer dynamiquement des scénarios de simulation.

- **LLM agentique et raisonnement conversationnel** :  
  Le LLM est exploité dans une approche agentique, s’appuyant sur des frameworks de type LangGraph pour permettre :
  - Le raisonnement multi-étapes et l’orchestration d’actions complexes,
  - L’interaction conversationnelle et le dialogue naturel avec les Digital Twins,
  - L’échange dynamique d’informations, la supervision proactive et la prise de décision assistée,
  - La capacité à piloter, questionner ou simuler le système via des agents LLM, pour une supervision augmentée et explicable.

- **Évolutivité prévue** :  
  La stack est conçue pour pouvoir migrer vers **TigerGraph** et intégrer un **GNN** pour la détection proactive d’incidents.

---

## 2. Hypothèses Fonctionnelles

- **Entités du graphe** :  
  Les nœuds représentent des équipements IT (serveur, base, application, switch, firewall) avec des attributs dynamiques (CPU, mémoire, latence).

- **Relations fonctionnelles** :  
  Les arêtes modélisent les dépendances fonctionnelles et réseaux.

- **Évolution dynamique des attributs** :  
  Chaque événement SimPy met à jour les attributs des nœuds en temps réel.

- **Détection d'incidents** :  
  Par l'application de règles Symbolic AI à chaque évolution du système.

- **Appels au LLM** :  
  Déclenchés uniquement pour enrichir les événements critiques (résumés, plans d'action, génération de scénarios).

---

## 3. Hypothèses Méthodologiques

- **Modularité** :  
  Chaque brique technique est développée comme un module indépendant et extensible.

- **Interopérabilité** :  
  Les modules doivent être conçus pour pouvoir intégrer à moyen terme des outils externes de supervision ITSM.

- **Pilotage** :  
  Le Digital Twin cible principalement **l'infrastructure IT** et non les couches métiers applicatives.

---

## 4. Stack retenue : SimPy, IA Symbolique, IA Neuronale, LLM

La solution retenue repose sur une architecture combinant :

- **SimPy** pour la simulation dynamique des événements IT,
- **IA Symbolique** (moteur de règles explicites) pour la détection déterministe d’incidents,
- **IA Neuronale (GNN)** pour la prédiction proactive et l’inférence sur le graphe,
- **LLM** pour l’enrichissement, la recommandation et l’explication intelligente.

Cette stack est conçue pour être :
- **Modulaire** (chaque brique indépendante et interfaçable),
- **Scalable** (migration NetworkX → TigerGraph possible),
- **Flexible** (ajout de scénarios what-if, analyses avancées, autonomisation progressive),
- **Interopérable** (préparée à l’intégration avec ITSM, API, etc.).

---

# 📣 Résumé

| Dimension | Hypothèse clé |
|:---------|:--------------|
| Stack initiale | NetworkX + SimPy + Symbolic AI + LLM Supervisor |
| Migration prévue | TigerGraph + GNN pour scalabilité industrielle |
| Objectif | Pilotage intelligent de l'infrastructure IT |
| Gouvernance | Règles Symboliques + Complément LLM |
| Philosophie | Modularité, scalabilité, intelligence progressive |

---