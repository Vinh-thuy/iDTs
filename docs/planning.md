# Plan d'action — Développement Digital Twin IT & Chatbot IA Agentique

---

## 🎯 Objectif global

Construire rapidement une première version du Digital Twin IT combinée à un chatbot IA agentique, avec des livrables visibles à chaque mois pour rassurer le CTO et démontrer les avancées.

L'équipe repose sur 6 personnes (5 recrutements + PO/Tech Lead R&D).

---

## 🏗 Sprint 0 — Mise en place technique (Durée : 2 à 3 semaines)

**Objectif** : Poser les fondations techniques, sans dépendre des flux réels.

### Livrables :
- [ ] Pipeline CI/CD GitLab fonctionnelle (build, test, déploiement backend et frontend).
- [ ] Base de code SimPy + NetworkX opérationnelle.
- [ ] API FastAPI minimale exposant un premier service.
- [ ] Frontend React simple connecté à l'API.

### Résultat attendu :
- Système déployable automatiquement.
- Première boucle backend <-> frontend démontrée.

---

## 📈 Sprint 1 — Premier prototype vivant du Digital Twin (Durée : 3 semaines)

**Objectif** : Faire vivre un premier graphe dynamique et détecter un incident basique.

### Livrables :
- [ ] Graphe NetworkX avec 3 à 5 nœuds types (serveur, base, réseau).
- [ ] Simulation d’un premier événement IT (ex: surcharge CPU simulée).
- [ ] Détection d’un incident simple par règle symbolique.
- [ ] Affichage dans React du graphe et des alertes détectées.

### Résultat attendu :
- Premier Digital Twin vivant et visualisable.
- Premier raisonnement symbolique appliqué.

---

## 📈 Sprint 2 — Introduction de l'IA agentique (Durée : 3 à 4 semaines)

**Objectif** : Construire la base du chatbot IA raisonné.

### Livrables :
- [ ] Intégration de LangChain pour gérer les premiers prompts.
- [ ] Construction d’un moteur RAG basique (recherche de contexte simulé).
- [ ] Déploiement d’un premier chatbot IA minimal en React.
- [ ] Début de raisonnement multi-étapes (LangGraph).

### Résultat attendu :
- Agent IA capable d'interagir avec l'état du Digital Twin.
- Démonstration de flux RAG basique.

---

## 📈 Sprint 3 — MVP complet Digital Twin + Chatbot IA Agentique (Durée : 4 semaines)

**Objectif** : Avoir une V0 exploitable du Digital Twin et du chatbot.

### Livrables :
- [ ] Graphe NetworkX étendu à 10 nœuds types avec interactions.
- [ ] Moteur de règles enrichi avec plusieurs types d'incidents IT.
- [ ] Agent IA capable de raisonner sur plusieurs étapes via LangGraph.
- [ ] RAG complet connecté à la base documentaire simulée.

### Résultat attendu :
- MVP Digital Twin IT opérationnel.
- MVP Chatbot IA opérationnel.

---

## 🚩 Jalons intermédiaires officiels

| Jalon | Contenu | Date cible |
|:------|:--------|:-----------|
| **J1** | Pipeline DevOps + Base technique posée (Sprint 0 terminé) | M+1 |
| **J2** | Premier graphe vivant + Détection d'incident basique (Sprint 1 terminé) | M+2 |
| **J3** | Premier agent IA interactif avec base simulée (Sprint 2 terminé) | M+3 |
| **J4** | MVP Digital Twin + MVP Chatbot IA livrés (Sprint 3 terminé) | M+4 |

---

## 📣 Points stratégiques

- Travailler sur données simulées au départ pour éviter la dépendance aux flux réels.
- Livrer visuellement des résultats fonctionnels à chaque fin de Sprint.
- Prioriser les livrables démonstratifs pour maintenir la confiance du CTO.
- Préparer progressivement la montée en charge vers TigerGraph et l'intégration LLM open source (Mistral).

---

# 🚀 Résultat final attendu

Une plateforme Digital Twin IT + Chatbot IA agentique :
- Agile,
- Scalable,
- Gouvernée par la combinaison Symbolic AI, GNN, RAG et LLM orchestration.

---