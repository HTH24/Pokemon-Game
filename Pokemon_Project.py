# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:45:10 2020

@author: HTH
"""

# In this Pokemon game, we only assume Fire, Grass, and Water type Pokemons. 

class Pokemon():
    def __init__(self, name, level, kind, current_health):
        self.name = name
        self.level = level
        self.type = kind # avoid using type as a keyword argument
        self.max_health = level * 10
        # the max health is determined by the current level
        self.current_health = current_health
        # self.is_knocked_out = is_knocked_out
        
    def __repr__(self):
        return "Pokemon {}: type {}, level {}, current_health is {}.".format(
            self.name, self.type, self.level, self.current_health)
        
    # both the lose and gain health methods have an argument that determines how much health is lost or gained
    def lose_health(self, health_lost):
          # the Pokemon is not knocked out yet, so it can still lose health
        message = ""
        if self.current_health == 0:
            message = "this Pokemon is knocked out already ! It cannot lose health anymore."
            print(message)
        else:
            if health_lost >= self.current_health:
                message = "The Pokemon cannot lose more than its current health! It is knocked out now."
                print(message)
                health_lost = self.current_health
                self.current_health -= health_lost
            else:
                self.current_health -= health_lost
        return "Pokemon {}'s current health is {}".format(self.name, self.current_health)
            
    def gain_health(self, health_gained):
        message = ""
        if health_gained < 0:
            message = "Enter a positive number. The Pokemon is gaining health !"
        elif self.current_health == 0:
            message = "This Pokemon is knocked out ! It needs to be revived first."
        elif (self.current_health > 0) & (health_gained <= self.max_health) & (health_gained > 0):
            self.current_health += health_gained
            if self.current_health > self.max_health:
                self.current_health = self.max_health
                message = "You cannot breach the maximum health level! Current health is {}".format(self.current_health)
            else:
                message = "The current health after gaining {} is {}".format(health_gained, self.current_health)
        return message
           
    def knock_out_Pokemon(self):
        if self.current_health == 0:
            return 'Pokemon {} is knocked out !'.format(self.name)
        else:
            return 'Pokemon {} is still alive ! Current health is {}'.format(self.name, self.current_health)
        
    def revive_Pokemon(self):
        message = ""
        if self.current_health != 0:
            message = 'Hey, the Pokemon is not knocked out yet !'
            
        while True:
            try:
                health_choice = int(input("How much health do you want to give the Pokemon? \\\
                                              Enter an integer between 1 and {}: ".format(self.max_health)))
            except ValueError:
                print('Please enter an integer !')
                continue
            
        # to check if the number entered is positive yet does not exceed maximum health
            if (health_choice <= self.max_health) & (health_choice >= 1):
                self.current_health += health_choice
                message = 'This Pokemon is now revived ! It now has a health of {}'.format(self.current_health)     
                break
            elif health_choice <= 1:
                print('The number you enter must be greater than or equal to 1.')
                continue
            else:
                print('You cannot exceed the maximum health of this Pokemon and ')
                continue
        return message
            
    def attack(self, other_pokemon):
        # this method takes another Pokeman as an argument and deals damage to that Pokemon
        # the amount of damage dealt depends on the type of the Pokemons. 

        damage = 0
        if self.type == 'fire':
            if other_pokemon.type == 'grass':
                damage = 2 * self.level
            elif other_pokemon.type == 'water':
                damage = self.level / 2
            else:
                damage = self.level
        elif self.type == 'water':
            if other_pokemon.type == 'fire':
                damage = 2 * self.level
            elif other_pokemon.type == 'grass':
                damage = self.level / 2
            else:
                damage = self.level
        elif self.type == 'grass':
            if other_pokemon.type == 'water':
                damage = 2 * self.level
            elif other_pokemon.type == 'fire':
                damage = self.level / 2
            else:
                damage = self.level
                
        other_pokemon.lose_health(damage)
        return "Pokemon {} has dealt {} damage to Pokemon {}, which now has health {}".format(
            self.name, damage, other_pokemon.name, other_pokemon.current_health)
                
p1 = Pokemon('H1', 1, 'water', 10)
p2 = Pokemon('H2', 2, 'water', 20)
p3 = Pokemon('H3', 3, 'water', 30)
p4 = Pokemon('H4', 4, 'water', 40)
p5 = Pokemon('H5', 5, 'water', 50)
p6 = Pokemon('H6', 6, 'water', 60)

p7 = Pokemon('H7', 1, 'fire', 10)
p8 = Pokemon('H8', 2, 'water', 20)
p9 = Pokemon('H9', 3, 'water', 30)
p10 = Pokemon('H10', 4, 'water', 40)
p11 = Pokemon('H11', 5, 'water', 50)
p12 = Pokemon('H12', 6, 'water', 60)
# p2 = Pokemon('Lai', 20, 'grass', 20)
# print(p2)
# # print(p1.knock_out_Pokemon())
# # print(p1.is_knocked_out)
# # print(p1.lose_health(2))
# print(p1.gain_health(21))
# # print(p1.revive_Pokemon())


poke_list_1 = [p1, p2, p3, p4, p5, p6]
poke_list_2 = [p7, p8, p9, p10, p11, p12]

class Trainer():
    # a trainer can have up to 6 pokemons, which we store in a list
    # can use a potion, attack another trainer, and switch the current pokemon. 3 methods.
    def __init__(self, name, pokemons, current_pokemon, potions):
        self.name = name
        self.potions = potions # can use them to heal pokemons
        self.current_pokemon = current_pokemon # the current active pokemon
        self.pokemons = pokemons # a list of pokemons
        
    def __repr__(self):
        return "Trainer {}: current pokemon is {}. {} potions left".format(
            self.name, self.current_pokemon, self.potions)
    
    def heal_pokemon(self, heal_amount):
        if self.potions != 0:
        # the heal amount is customizable
            if self.current_pokemon.current_health == self.current_pokemon.max_health:
                print('Your pokemon does not need any healing. It is at maximum health.')
                
            elif self.current_pokemon.current_health <= self.current_pokemon.max_health:
                self.potions -= 1
                self.current_pokemon.gain_health(heal_amount)
                if self.current_pokemon.current_health > self.current_pokemon.max_health:
                    self.current_pokemon.current_health = self.current_pokemon.max_health
        else:
            print('You have run out of potions.')
            
        return "The current health of Pokemon {} is now {}".format(
            self.current_pokemon, self.current_pokemon.current_health)
    
    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.current_pokemon
        self.current_pokemon.attack(their_pokemon)
        return "Your {} just attacked trainer {}'s Pokemon {}. {}!".format(
            self.current_pokemon, other_trainer.name, their_pokemon.name, self.current_pokemon.attack(other_trainer.current_pokemon))
        
    def switch_pokemon(self, backup):
        self.current_pokemon = backup
        print('The current active Pokemon is now {}'.format(self.current_pokemon))
    
t1 = Trainer('HTH', poke_list_1, p1, 5)
t2 = Trainer('MZH', poke_list_2, p7, 5)
# print(t1)
# print(t1.heal_pokemon(5))
# print(p2)
# print(p1.attack(p2))

# print(t1.heal_pokemon(1))

# print(t1)
# t1.switch_pokemon(p2)   
# print(p12.attack(p1))

# print(t1)
# print(p12.attack(p1))
# print(p1)
# print(p12.attack(p1))
# print(p1)
# print(p1.revive_Pokemon())
# print(t1.heal_pokemon(5))

print(t1.attack_other_trainer(t2))
