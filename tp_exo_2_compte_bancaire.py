import random

import string

from tp_exo_2_client import Client

from datetime import datetime

class CompteBancaire:

    _somme_des_soldes = 0.0

    def __init__(self, date_creation: str, client: Client, solde: float):
        self.date_creation = date_creation  # Validation dans le setter
        self.client = client  # Un objet Client
        self.solde = solde  # Validation dans le setter
        self.identifiant_interne = self._generer_identifiant_interne() #génération automatique

        CompteBancaire._somme_des_soldes += self.solde
 
 
    @property
    def date_creation(self):
        return self._date_creation

    @date_creation.setter
    def date_creation(self, value: str):
        try:
            # Convertir la chaîne en date
            date = datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La date de création doit être au format 'YYYY-MM-DD'.")
        self._date_creation = date

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        if not isinstance(value, Client):
            raise ValueError("L'attribut client doit être une instance de la classe Client.")
        self._client = value

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, value: float):
        if not isinstance(value, (float, int)):
            raise ValueError("Le solde doit être un nombre.")
        CompteBancaire._somme_des_soldes += value - getattr(self, "_solde", 0.0)
        self._solde = float(value)


    def _generer_identifiant_interne(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=4))
        date_formatee = self.date_creation.strftime("%d%m%Y")
        return f"{lettres}{date_formatee}"


    @staticmethod
    def get_somme_des_soldes():
        return CompteBancaire._somme_des_soldes

    def __eq__(self, other): # méthode magique 
        if isinstance(other, CompteBancaire):
            return self.solde == other.solde
        return False
    

    def __str__(self):
        return (f"Compte créé le {self.date_creation}, Client : {self.client.prenom} {self.client.nom}, "
                f"Solde : {self.solde:.2f}€")


# Tests sur NIR, format de la date de création et type client

client_1 = Client("Dupont", "Jean", "10 Rue des Lilas", "123456789012345")

# Test 1 : Création d'un compte avec une date et un solde valides
try:
    compte = CompteBancaire("2024-01-01", client_1, 1500.0)
    print(compte)
except ValueError as e:
    print(f"Erreur : {e}")

# Test 2 : Date avec un mauvais format
try:
    compte_invalide = CompteBancaire("01-01-2024", client_1, 1500.0)  # Format DD-MM-YYYY
except ValueError as e:
    print(f"Erreur : {e}")

# Test 3 : Objet client non valide
try:
    compte_invalide = CompteBancaire("2024-01-01", "Pas un client valide", 1500.0)
except ValueError as e:
    print(f"Erreur : {e}")

# Test 4 : Solde non numérique
try:
    compte_invalide = CompteBancaire("2024-01-01", client_1, "invalid")
except ValueError as e:
    print(f"Erreur : {e}")

# Tests sur l'identifiant interne

client_2 = Client("Potter", "Harry", "1 rue de la Lune", "987654321098765")

# Test 1 : Création d'un compte valide
try:
    compte_2 = CompteBancaire("2022-07-01", client_2, 700.0)
    print(compte_2)
except ValueError as e:
    print(f"Erreur : {e}")

# Test 2 : Vérification de l'identifiant interne
print(f"Identifiant interne du compte : compte_2 : {compte_2.identifiant_interne}")

# Test pour valider la sommes des comptes
print(f"Somme des soldes : {CompteBancaire.get_somme_des_soldes():.2f}€")

# Test mise à jour solde
compte_2.solde = 5.0
print(f"Nouvelle somme des soldes : {CompteBancaire.get_somme_des_soldes():.2f}€")


# Tests

# Création de comptes
compte_1 = CompteBancaire("2024-01-01", client_1, 1500.0)
compte_2 = CompteBancaire("2022-07-01", client_2, 1500.0) 


# Affichage de leur identifiant interne 
print(f"Identifiant interne du compte 1 : {compte_1.identifiant_interne}")
print(f"Identifiant interne du compte 2 : {compte_2.identifiant_interne}")


# Test d'égalité
print(f"Compte 1 et Compte 2 sont égaux ? {compte_1 == compte_2}")  # True

# Afficher le solde total de tous les comptes créés
print(f"Le solde total de tous les comptes créés est : {CompteBancaire.get_somme_des_soldes():.2f}€")

