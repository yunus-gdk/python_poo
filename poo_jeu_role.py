from random import randint

class Player:
    def __init__(self):
        self.health = 50

class User:
    def __init__(self):
        self.health = 50
        self.potion = 3
        self.skip_turn = False
        self._damage = randint(5, 10)
        self._health_potion = randint(15, 50)

    @property
    def damage(self):
        return self._damage
    
    def display_attack(self):
        print(f"Vous avez infligé {self._damage} points de dégats à l'ennemi ⚔️")

    def display_health_after_potion(self):
        print(f"Vous récupérez {self._health_potion} points de vie ❤️ ({self.potion} restantes)")

class Ennemi:
    def __init__(self):
        self.health = 50
        self._damage = randint(5, 10)

    @property
    def damage(self):
        return self._damage
    
    def display_attack(self):
        print(f"L'ennemi vous a infligé {self._damage} points de dégats.")

user = User()
ennemi = Ennemi()

while True:
    # Jeu du joueur
    if user.skip_turn:
        print("Vous passez votre tour...")
        user.skip_turn = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice == "1":  # Attaque
            ennemi.health -= user.damage
            user.display_attack()

        elif user_choice == "2" and user.potion > 0:  # Potion
            user.health += user._health_potion
            user.potion -= 1
            user.skip_turn = True

            user.display_health_after_potion()
        else:
            print("Vous n'avez plus de potions...")
            continue

    if ennemi.health <= 0:
        print("Tu as gagné !!!")
        break

    # Attaque de l'ennemi
    user.health -= ennemi.damage
    ennemi.display_attack()

    if user.health <= 0:
        print("Tu as perdu ?")
        break

    # Stats
    print(f"Il vous reste {user.health} points de vie.")
    print(f"Il reste {ennemi.health} points de vie à l'ennemi.")
    print("-" * 50)

print("Fin du jeu.")