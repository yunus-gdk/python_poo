class Voiture:

    def __init__(self):
        self.essence = 100
	
    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence !")
		
    def roule(self, km):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        self.essence -= (km * 5)/100
        
        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
        
        self.afficher_reservoir()

    def faire_le_plein(self):
        if self.essence == 100:
            print("Vous avez déjà le plein; inutile de passer à la station essence !!!")
            return

        self.essence = 100
        print(f"Vous pouvez repartir !")
        self.afficher_reservoir()

