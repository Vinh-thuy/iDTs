from symai import Symbol

# Définir les entrées
cpu_utilisation = 92  # Utilisation CPU en pourcentage
ram_utilisation = 88  # Utilisation RAM en pourcentage
incidents_signalés = 2  # Nombre d'incidents signalés

# Créer des Symboles pour chaque entrée
cpu = Symbol(f"CPU utilization is {cpu_utilisation}%")
ram = Symbol(f"RAM utilization is {ram_utilisation}%")
incidents = Symbol(f"{incidents_signalés} incidents reported")

# Définir les règles
règle_critique = Symbol("If CPU > 90% and RAM > 90%, then status is Critical")
règle_instable = Symbol("If incidents reported > 5, then status is Unstable")
règle_stable = Symbol("If CPU < 50% and RAM < 50% and no incidents, then status is Stable")

# Évaluer les règles
état_critique = (cpu & ram & règle_critique).interpret()
état_instable = (incidents & règle_instable).interpret()
état_stable = (cpu & ram & incidents & règle_stable).interpret()

# Afficher les résultats
print(f"Évaluation Critique : {état_critique}")
print(f"Évaluation Instable : {état_instable}")
print(f"Évaluation Stable : {état_stable}")