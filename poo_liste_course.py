choix_menu = ["1", "2", "3", "4", "5"]

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

class Course:
    def __init__(self):
        self._liste = []

    @property
    def liste(self):
        return self._liste

    def ajouter(self):
        element = input("Entrer le nom d'un élèment à ajouter à la liste de courses: ")
        self._liste.append(element)
        print("\n")
        print("_"*50)
        print(f"L'élèment {self._liste[-1]} a été ajouté à la liste.")
    
    def retirer(self):
        if len(self._liste) == 0:
            print("La liste est déjà vide !!!")
        else:
            element = input("Entrer le nom d'un élèment à retirer de la liste de courses: ")
            if element in self._liste:
                self._liste.remove(element)
                print(f"L'élèment {element} a bien été supprimé de la liste.")
            else: 
                print(f"L'élèment {element} n'est pas dans la liste.")
    
    def afficher(self):
        if self._liste:
            print(f"Voici le contenu de votre liste : ")
            for i, element in enumerate(self._liste, 1):
                print(f"{i}. {element}")
        else:
            print("Votre liste ne contient aucun élèment.")
    
    def vider(self):
        if self._liste:
           self._liste.clear()
           print("La liste a été vidée de son contenu !")
        else:
            print("La liste est déjà vide !!!")

courses = Course()

while True:
    print("_"*50)
    choix = input(MENU)

    print("\n")
    if choix not in choix_menu:
        print("Veuillez choisir une option valide: 1, 2, 3, 4 ou 5")
        continue

    if choix == "1":
        courses.ajouter()
        
    elif choix == "2":
        courses.retirer()
        
    elif choix == "3":
        courses.afficher()
        
    elif choix == "4":
        courses.vider()
        
    elif choix == "5":
        print("A bientôt !!!")
        break
