from random import randint

# class Player:
#     def __init__(self):
#         self.health = 50

class User:
    def __init__(self):
        self.health = 50
        self.potion = 3
        self.skip_turn = False

    @property
    def damage(self):
        return randint(5, 10)
    
    @property
    def health_potion(self):
        return randint(15, 50)
    
    def __str__(self):
        return f"Il vous reste {self.health} points de vie."
    
    def attack(self, ennemi: "Ennemi"):
        damage_inflicted = self.damage
        ennemi.health -= damage_inflicted
        print(f"Vous avez infligé {damage_inflicted} points de dégats à l'ennemi ⚔️")

    def take_potion(self):
        health_given = self.potion
        user.health += health_given
        user.potion -= 1
        user.skip_turn = True
        print(f"Vous récupérez {health_given} points de vie ❤️ !!! ({self.potion} restantes)")

class Ennemi:
    def __init__(self):
        self.health = 50

    @property
    def damage(self):
        return randint(5, 15)
    
    def __str__(self):
        return f"Il reste {self.health} points de vie à l'ennemi."
    
    def attack(self, user: "User"):
        damage_inflicted = self.damage
        user.health -= damage_inflicted
        print(f"L'ennemi vous a infligé {damage_inflicted} points de dégats.")

def create_players():
    user = User()
    ennemi = Ennemi()
    return user, ennemi

def game(user: User, ennemi: Ennemi):
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
                user.attack(ennemi)

            elif user_choice == "2" and user.potion > 0:  # Potion
                user.take_potion()
            else:
                print("Vous n'avez plus de potions...")
                continue

        if ennemi.health <= 0:
            print("Tu as gagné !!!")
            break

        # Attaque de l'ennemi
        ennemi.attack(user)

        if user.health <= 0:
            print("Tu as perdu !!!")
            break

        # Stats
        print(user)
        print(ennemi)        
        print("-" * 50)

    print("Fin du jeu.")

if __name__ == '__main__':
    user, ennemi = create_players()
    game(user, ennemi)
