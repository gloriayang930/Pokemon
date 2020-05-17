class Pokemon:
  def __init__(self,name,level,types,is_knocked_out):
    self.name = name
    self.level = level
    self.type = types
    self.max_health = level*5
    self.health = self.max_health
    self.is_knocked_out = is_knocked_out
    self.exp = 0

  def lose_health(self,health):
    if self.health > health:
      self.health -= health
      print("{0} now has {1} health".format(self.name,self.health))
    else:
      self.health = 0
      self.is_knocked_out()
      print("{0} is knocked out!".format(self.name))

  def gain_health(self,health):
    self.health += health
    if self.health > self.max_health:
      self.health = self.max_health
    print("{0} now has {1} health".format(self.name,self.health))
    return self.health

  def knock_out(self):
    if self.is_knocked_out:
      print("{name} is already knocked out.".format(name = self.name))
    else:
      self.is_knocked_out = True
      print("{name} is knocked out!".format(name = self.name))

  def revive(self):
    if self.is_knocked_out:
      self.is_knocked_out = False
      self.health = self.max_health/2
      print("{name} has been revived with {health} health!".format(name = self.name, health = self.health))
    else:
      print("{name} is not knocked out.".format(name = self.name))

  def attack(self,other_pokemon):
    all_types = ["Water","Fire","Grass"]
    if self.knock_out():
      damage = 0
    for i in range(len(all_types)):
      if self.type == all_types[i-1] and other_pokemon.type == all_types[i]:
        damage = self.level * 0.5
        print("It's not very effective!")
        other_pokemon.lose_health(damage)
      elif self.type == all_types[i] and other_pokemon.type == all_types[i-1]:
        damage = self.level * 2
        print("Wonderful!")
        other_pokemon.lose_health(damage)
      elif self.type == all_types[i] and other_pokemon.type == all_types[i]:
        damage = self.level      
        other_pokemon.lose_health(damage)
    print("{0} has attacked {1} and {1} now has {2} health".format(self.name,other_pokemon.name,other_pokemon.health))
    
    def gain_exp(self,exp):
      self.exp += exp
      print("{0} has gained {1} exp!".format(self.name,exp))

    def level_up(self):
      self.exp = 0
      self.level += 1
      self.max_health += 1
      self.health = self.max_health     
      print("{} leveled up to level {}! Max health now is {}. Health fully regenerated.\n".format(self.name, self.level, self.max_health))

class Trainer:
  def __init__(self,name,pokemons,total_potions,current_pokemon):
    self.pokemons = pokemons[:6] if len(pokemons) > 6 else pokemons
    self.potions = total_potions
    self.current_pokemon = current_pokemon
    self.name = name

  def __repr__(self):
    print("Currently {0} has the following pokemons: ".format(self.name))
    for pokemon in self.pokemons:
      print(pokemon)

  def attack_other_trainer(self,other_trainer):
    self.current_pokemon.attack(other_trainer.current_pokemon)
    print("Your {0} has attacked {1}'s {2}\n".format(self.current_pokemon.name,other_trainer.name,other_trainer.current_pokemon.name))

  def heal(self):
    my_pokemon = self.current_pokemon
    my_pokemon.health = my_pokemon.max_health
    self.potions -= 1
    print("You have healed {0} and you now have {1} potions\n".format(my_pokemon.name,self.potions))

  def switch(self,switch_pokemon):
    if not switch_pokemon.knock_out():
      self.current_pokemon = switch_pokemon
      print("You have successfully switched to {0}\n".format(switch_pokemon.name))
    else:
      print("Oops! Please choose another one\n")
    return self.current_pokemon

class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out):
    super().__init__(name, level, type, is_knocked_out)

  def destroy(self, other):
    other.lose_health(other.health)
    print("{} totally destroyed {}!".format(self.current_pokemon.name, other.name))

#Let's play!
pikachu = Pokemon("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
squirtle = Pokemon("Squirtle", 3, "Water", False)
charmander = Charmander("Charmander", 3, "Fire", False)
#Trainers
gloria = Trainer('Gloria', [pikachu, charmander], 2, pikachu)
han = Trainer('Han', [bulbasaur, squirtle], 2, bulbasaur)

gloria.attack_other_trainer(han)

