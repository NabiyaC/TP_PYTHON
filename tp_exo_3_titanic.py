import csv

# Ouvrir le fichier CSV
with open('titanic_survival.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    ages = []  # Liste pour stocker les âges valides
    
    for row in reader:
        # Vérifier si la clé "Age" existe et si la valeur est non vide
        if 'age' in row and row['age']:
            try:
                age = float(row['age'])  # Convertir en nombre flottant
                ages.append(age)  # Ajouter à la liste des âges valides
            except ValueError:
                # Ignorer les valeurs non convertibles
                continue
    
    # Calcul de la moyenne d'âge
    if ages:
        average_age = sum(ages) / len(ages)
        rounded_average = round(average_age)
        print(f"\n La moyenne d'âge des passagers est : {rounded_average} ans.\n")
    else:
        print("Aucune donnée valide pour l'âge.")


# Pourcentage de survie par classe

survival_data = {}

with open('titanic_survival.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # Vérifier si les clés "Pclass" et "Survived" existent
        if 'pclass' in row and 'survived' in row:
            try:
                passenger_class = int(row['pclass'])  # Convertir la classe en entier
                survived = int(row['survived'])  # Convertir la survie en entier (0 ou 1)
                
                # Initialiser les données pour une nouvelle classe si elle n'existe pas
                if passenger_class not in survival_data:
                    survival_data[passenger_class] = {'survived_passengers': 0, 'total_passengers': 0}
                
                # Mettre à jour les totaux
                survival_data[passenger_class]['total_passengers'] += 1
                if survived == 1:
                    survival_data[passenger_class]['survived_passengers'] += 1
            except ValueError:
                continue

# Calcul
for pclass, data in survival_data.items():
    survived_passengers = data['survived_passengers']
    total_passengers = data['total_passengers']
    survival_percentage = round((survived_passengers / total_passengers) * 100)  # Calculer le pourcentage arrondi
    print(f" Classe {pclass}: {survival_percentage}% de survie\n")


# Initialiser un dictionnaire pour les bateaux de sauvetage
boat_counter = {}

# Ouvrir le fichier CSV
with open('titanic_survival.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Vérifier si la clé "boat" existe
        if 'boat' in row:
            boat = row['boat']  # Récupérer le bateau de sauvetage
            if boat:  # Ignorer les lignes où "boat" est vide
                # Incrémenter le compteur pour ce bateau
                if boat in boat_counter:
                    boat_counter[boat] += 1
                else:
                    boat_counter[boat] = 1

# Trouver le bateau avec le plus de passagers sauvés
most_saving_boat = None
max_passengers = 0

for boat, count in boat_counter.items():
    if count > max_passengers:
        max_passengers = count
        most_saving_boat = boat

# Afficher le résultat
if most_saving_boat:
    print(f"Le bateau de sauvetage ayant sauvé le plus de passagers est le bateau {most_saving_boat} avec {max_passengers} passagers.\n")
else:
    print("Aucun bateau de sauvetage trouvé dans les données.")

    