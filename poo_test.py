class Voiture:
	def __init__(self, marque, couleur):
		self.marque = marque
		self.couleur = couleur

	def afficher(self):
		print(f"La {self.marque} est de couleur {self.couleur} !")

voiture01 = Voiture("Peugeot", "rouge")
voiture02 = Voiture("Seat", "noir")

voiture01.afficher()
voiture02.afficher()

