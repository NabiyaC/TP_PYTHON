# 1- Créer une classe "Entreprise"(nom, adresse, SIRET de 14 chiffres)
class Entreprise:
    def __init__(self, nom, adresse, siret):
        self.nom = nom  
        self.adresse = adresse
        self.siret = siret


# 2- Représentation textuelle de l'objet
    def __str__(self):
        return f"L'entreprise {self._nom}, ayant son siège social au {self._adresse}, possède le numéro de SIRET {self._siret}."
    
    # Getter pour le nom
    @property
    def nom(self):
        return self._nom

    # Setter pour le nom
    @nom.setter
    def nom(self, nom):
        if not nom.strip():
            raise ValueError("Veuillez renseigner votre nom svp.")
        self._nom = nom

    # Getter pour l'adresse
    @property
    def adresse(self):
        return self._adresse

    # Setter pour l'adresse
    @adresse.setter
    def adresse(self, adresse):
        if not adresse.strip():
            raise ValueError("Veuillez renseigner votre adresse svp.")
        self._adresse = adresse

    # Getter pour le SIRET
    @property
    def siret(self):
        return self._siret

    # Setter pour le SIRET
    @siret.setter
    def siret(self, siret):
        if not siret.isdigit():
            raise ValueError("Le numéro de SIRET doit contenir uniquement des chiffres!")
        elif len(siret) != 14:
            raise ValueError("Le numéro de SIRET doit contenir exactement 14 chiffres!")
        self._siret = siret

    
# 3- Création d'un objet Entreprise
mon_entreprise = Entreprise("NCHERGUI", "123 Rue de la Paix", "12345678901234")

# Afficher les informations de l'entreprise
print(mon_entreprise)

# 4- Utiliser le getter pour printer le nom de l'entreprise
print("Nom:", mon_entreprise.nom)

# 5- Modifier l'attribut SIRET avec le setter
mon_entreprise.siret = "98765432109876"

# Afficher les informations mises à jour
print(mon_entreprise)

# Tests
try:
    mon_entreprise.siret = "invalide123"
except ValueError as e : 
    print(f"Erreur lors de la modification : {e}")

try:
    mon_entreprise.siret = "97887767"
except ValueError as e : 
    print(f"Erreur lors de la modification : {e}")


try:
    mon_entreprise.nom = ""
except ValueError as e : 
    print(f"Erreur lors de la modification : {e}")


try:
    mon_entreprise.adresse = ""
except ValueError as e : 
    print(f"Erreur lors de la modification : {e}")