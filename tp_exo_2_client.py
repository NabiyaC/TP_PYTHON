class Client:
    def __init__(self, nom : str, prenom : str, adresse : str, nir : str):
        self.nom = nom  
        self.prenom = prenom  
        self.adresse = adresse  
        self.nir = nir  # Passe par le setter pour validation

    @property
    def nir(self):
        return self._nir

    @nir.setter
    def nir(self, value):
    
        if not value.isdigit():
            raise ValueError("Le NIR doit contenir uniquement des chiffres.")
        if len(value) != 15:
            raise ValueError("Le NIR doit contenir exactement 15 chiffres.")
        self._nir = value

    def __str__(self):
        return f"{self.prenom} {self.nom}, habitant au {self.adresse}, NIR : {self.nir}"
    
# Test 1 : Création d'un client valide
try:
    client_valide = Client("Dupont", "Jean", "10 Rue des Lilas", "123456789012345")
    print(client_valide)
except ValueError as e:
    print(f"Erreur : {e}")

# Test 2 : NIR avec lettres
try:
    client_invalide = Client("Martin", "Sophie", "20 Avenue des Fleurs", "12345ABCDE67890")
except ValueError as e:
    print(f"Erreur : {e}")

# Test 3 : NIR trop court
try:
    client_invalide = Client("Durand", "Paul", "30 Boulevard des Roses", "1234")
except ValueError as e:
    print(f"Erreur : {e}")



