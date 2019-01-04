class Character:
	def __init__(self, name, HP, shield, armor, possessions = []):
		self.name = name
		self.HP = HP
		self.shield = shield
		self.armor = armor
		self.possessions = possessions

class Monster:
	def __init__(self, name, power, weakness):
		self.name = name
		self.power = power
		self.weakness = weakness

class Item:
	def __init__(self, name, ability):
		self.name = name
		self.ability = ability

class Dungeon:
	def __init__(self, monsters, cards = 0):
		self.monsters = monsters
		self.cards = cards
#characters are the Warrior, the Rogue, the Barbarian, and the Mage

#The next 6 items belong to the Warrior
knight_shield = Item('Knight Shield', 'HP + 3')
plate_armor = Item('Plate Armor', 'HP + 5')
torch_knight = Item('Torch', 'Defeat Monsters with strength 3 or less')
holy_grail_warrior = Item('Holy Grail', 'Defeat Monsters with even-numbered strength')
vorpal_sword = Item('Vorpal Sword', 'Defeat one Monster that you choose before entering the Dungeon')
dragon_spear = Item('Dragon Spear', 'Defeat the Dragon')

#The next 6 items belong to the Rogue
buckler = Item('Buckler', 'HP + 3')
mithril_armor = Item('Mithril Armor', 'HP + 5')
invisibility_cloak = Item('Invisibility Cloak', 'Defeat Monsters with strength 6 or more')
healing_potion_rogue = Item('Healing Potion', 'When you die, come back to life with your Adventurer\'s HP(once per Dungeon)')
ring_of_power = Item('Ring of Power', 'Defeat Monsters with strength 2 or less. Add their total strength to your HP')
vorpal_dagger = Item('Vorpal Dagger', 'Defeat one Monster that you choose before entering the Dungeon')

#The next 6 items belong to the Barbarian
leather_shield = Item('Leather Shield', 'HP +3')
chainmail = Item('Chainmail', 'HP +4')
healing_potion_barbarian = Item('Healing Potion', 'When you die, come back to life with your Adventurer\'s HP(Once per Dungeon)')
torch_barbarian = Item('Torch', 'Defeat Monsters with strength 3 or less.')
war_hammer = Item('War Hammer', 'Defeat Golems')
fire_axe = Item('Fire Axe', ' Defeat one Monster after you draw it (Once per Dungeon)')

#the next 6 items belong to the Mage
bracelet_of_protection = Item('Bracelet of Protection', 'HP + 3')
wall_of_fire = Item('Wall of Fire', 'HP + 6')
polymorph = Item('Polymorph', 'Replace one Monster with the next monster from the deck(once per Dungeon)')
demonic_pact = Item('Demonic Pact','Defeat the Demon and the next Monster')
omnipitance = Item('Omnipitance', 'If all the Monsters in the Dungeon are different, you win the round')
holy_grail_mage = Item('Holy Grail', 'Defeat monsters with even-numbered strength')

#The four characters, and their associated items
Warrior = Character('Warrior', 3, knight_shield, plate_armor, [torch_knight, holy_grail_warrior, vorpal_sword, dragon_spear])
Rogue = Character('Rogue', 3, buckler, mithril_armor, [invisibility_cloak, healing_potion_rogue, ring_of_power, vorpal_dagger])
Barbarian = Character('Barbarian', 4, leather_shield, chainmail, [healing_potion_barbarian, torch_barbarian, war_hammer, fire_axe])
Mage = Character('Mage', 2, bracelet_of_protection, wall_of_fire, [polymorph, demonic_pact, omnipitance, holy_grail_mage])

characters = [Warrior, Rogue, Barbarian, Mage]

goblin1 = Monster('Goblin', 1, ['Torch', 'Ring of Power'])
goblin2 = Monster('Goblin', 1, ['Torch', 'Ring of Power'])
skeleton1 = Monster('Skeleton', 2, ['Torch', 'Holy Grail', 'Ring of Power'])
skeleton2 = Monster('Skeleton', 2, ['Torch', 'Holy Grail', 'Ring of Power'])
orc1 = Monster('Orc', 3, 'Torch')
orc2 = Monster('Orc', 3, 'Torch')
vampire1 = Monster('Vampire', 4, 'Holy Grail')
vampire2 = Monster('Vampire', 4, 'Holy Grail')
golem1 = Monster('Golem', 5, 'War Hammer')
golem2 = Monster('Golem', 5, 'War Hammer')
lich = Monster('Lich', 6, ['Holy Grail', 'Invisibility Cloak'])
demon = Monster('Demon', 7, ['Invisibility Cloak', 'Demonic Pact'])
dragon = Monster('Dragon', 9, ['Invisibility Cloak', 'Dragon Spear'])

deck = [goblin1, goblin2, skeleton1, skeleton2, orc1, orc2, vampire1, vampire2, golem1, golem2, lich, demon, dragon]


print('Welcome to the Dungeon!')
print()
print()
print('I do not own the rights to this game. This is simply an educational exercise to develop my programming skills.')
print()
print()

print('The four heroes are:')
for character in characters:
	print('\t {}'.format(character.name))

#select a hero
selection = input("Select a hero to learn more about them. ")

#clear the screen

#print the information about the hero
print('{}, HP {}'.format(selection.name, selection.HP))
print()

#see the hero's items
#pass or draw?
#draw a monster
#decide whether to put the monster in the dungeon or remove an item
#next player


#once one player is left, establish the hero's HP & what items they have
#