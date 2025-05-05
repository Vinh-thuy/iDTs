# Plan de gestion des données et flux pour le Stream Digital Twin IT & IA

---

## 🎯 Objectif de cette phase initiale

Construire et démontrer une première version du Digital Twin IT :
- Sans dépendre immédiatement de la qualité ou de l'accès complet aux flux réels (ServiceNow, Dynatrace, base graphe interne),
- En utilisant **des données synthétiques et simulées** pour prouver le concept,
- Tout en préparant **une architecture prête à brancher** sur les flux réels dès qu'ils seront accessibles.

---

## 🧠 Contraintes techniques connues

| Source de données | Contrainte identifiée | Impact |
|:------------------|:----------------------|:-------|
| **ServiceNow** | Connexions API parfois lentes à mettre en place (droits, sécurité, disponibilité) | Ralentit l'accès aux incidents ITSM réels |
| **Dynatrace** | Accès aux métriques nécessitant des autorisations techniques spécifiques | Retarde l'intégration des vraies métriques performance |
| **Base Graphe interne** | Existence de données graphes mais qualité potentiellement hétérogène, voire incomplète | Nécessite un plan de nettoyage ou de reconstruction partielle |

---

## 🚩 Stratégie de mitigation pour la première itération

**1. Utiliser des données synthétiques ou simulées pour ServiceNow**

- Créer un **faux flux d'incidents ITSM** typique :
  - Tickets incident simulés,
  - Statuts (Open, In Progress, Resolved),
  - Typologies d'incidents courants (ex: Panne serveur, Problème réseau, Latence base de données).
- Générer ces incidents localement en Python, avec timestamps simulés.

➡️ **Permet d'alimenter le moteur de règles et le Digital Twin sans attendre ServiceNow.**

---

**2. Simuler des métriques Dynatrace**

- Simuler des métriques sur les nœuds du graphe :
  - CPU Load (%),
  - Memory Usage (MB/GB),
  - Network Latency (ms),
  - Availability status (Up/Down).
- Générer des séries temporelles fictives en Python ou directement via SimPy.

➡️ **Permet de déclencher des incidents basés sur des règles réalistes.**

---

**3. Utiliser et enrichir la base Graphe existante**

- Charger les données de la base graphe existante dans NetworkX (même imparfaites).
- Appliquer un nettoyage basique :
  - Supprimer les nœuds incomplets,
  - Ajouter quelques nœuds manquants manuellement,
  - Ajouter des attributs manquants pour la simulation.
- Compléter par des **nœuds simulés** pour combler les trous.

➡️ **Permet de partir d'une base réelle, tout en la rendant exploitable immédiatement.**

---

## 🛠 Méthode concrète de mise en œuvre

### Backend Python

- Générer données ServiceNow synthétiques dans un fichier JSON local.
- Générer flux métriques Dynatrace simulées via SimPy + NetworkX.
- Intégrer base graphe nettoyée + enrichie en mémoire avec NetworkX.

### API FastAPI

- Exposer l'état du graphe,
- Exposer la liste des incidents IT en cours,
- Exposer les métriques principales des nœuds.

### Frontend React

- Afficher :
  - Le graphe vivant (états, incidents),
  - Liste des incidents simulés,
  - Détail des métriques sur sélection d'un nœud.

---

## 📈 Résultat attendu après 1 mois avec cette approche

| Cible | Réalisation |
|:------|:------------|
| 1. | Premier graphe vivant alimenté (mélange réel + synthétique) |
| 2. | Simulation d'incidents IT réalistes avec ServiceNow simulé |
| 3. | Simulation de dégradations systèmes avec métriques Dynatrace simulées |
| 4. | Agent IA interactif pouvant interroger l'état de l'infrastructure |

---

## 📣 Résumé stratégique

- **Pas d'effet tunnel** lié aux flux réels manquants.
- **Livrables visibles et convaincants** dès le premier mois.
- **Architecture totalement prête** à se connecter aux vrais flux dès qu'ils seront accessibles.
- **Maintien de la confiance du CTO** grâce à la dynamique de livraison continue.

---

# 🚀 Conclusion

Avec cette stratégie de **"bouche à flux" (data simulée + base existante enrichie)** :
- Tu protèges ton planning,
- Tu gagnes du temps,
- Tu évites les dépendances critiques,
- Tu restes agile et focalisé sur les livrables visibles.

---