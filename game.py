import requests
import wordGen
import random

print('[RPGIO] Wait apporximately 15 seconds before the bot will start.')
print('[RPGIO] You can disable these messages, only leaving error logs by editing config.json')
print('[RPGIO] Loading lists..')

adjectives = requests.get('https://raw.githack.com/taikuukaits/SimpleWordlists/master/Wordlist-Adjectives-All.txt').text
adjectives = adjectives.split('\n')

nouns = requests.get('https://raw.githubusercontent.com/taikuukaits/SimpleWordlists/master/Wordlist-Nouns-All.txt').text
nouns = nouns.split('\n')

rarities = {1: 'foolish', 2: 'common', 3: 'uncommon', 4: 'cool', 5: 'epic', 6: 'menacing', 7: 'unstoppable', 8: 'void', 9: 'holly', 10: 'godly'}

print('[RPGIO] Done!')

def percentOf(percent, whole):
    """Get percent of a whole"""
    return int((float(f'0.{percent}'))*(whole))

class Entity:
    def __init__(self, name, protection, hp):
        self.name = name
        self.protection = protection
        self.hp = hp
        self.state = 1
    def receiveDamage(self, dmg):
        try:
            if abs(self.protection - dmg) >= self.hp:
                self.state = 0
                self.hp = 0
            else:
                self.hp -= abs(self.protection - dmg)
        except Exception as e:
            print('[RPGIO] Error occured during calculating dealt damage to an entity')
            print(e)
    def addHp(self, heal):
        try:
            self.hp += heal
        except Exception as e:
            print('[RPGIO] Error occuring during calculating entity\'s healing.')
            print(e)
    

class Ore:
    """Ore is a main material"""
    """Armor and weapons are made of it"""
    def __init__(self, name, meta_rarity, value, melt_temp):
        self.name = name
        self.meta_rarity = meta_rarity
        self.value = value
        self.melt_temp = melt_temp

class ArmorSet:
    """The thing player can wear"""
    def __init__(self, name, protection, on_savage, rarity, value, ore):
        self.name = name
        self.protection = protection
        self.on_savage = on_savage
        self.value = value
        self.ore = ore
    def getHelmet(self):
        self.helm = self
        self.helm.name = wordGen.genWord(random.randint(1, 4)) + ' ' + random.choice(adjectives) + ' helmet of ' + random.choice(nouns)
        self.helm.protection = percentOf(20, self.helm.protection)
        return self.helm
    def getChestplate(self):
        self.chpt = self
        self.chpt.name = wordGen.genWord(random.randint(1, 4)) + ' ' + random.choice(adjectives) + ' chestplate of ' + random.choice(nouns)
        self.chpt.protection = percentOf(50, self.chpt.protection)
        return self.chpt
    def getLeggins(self):
        self.leg = self
        self.leg.name = wordGen.genWord(random.randint(1, 4)) + ' ' + random.choice(adjectives) + ' leggins of ' + random.choice(nouns)
        self.leg.protection = percentOf(30, self.leg.protection)
        return self.leg

class Weapon:
    """The thing player can protect himself with"""
    def __init__(self, name, dmg, rarity, level):
        self.name = name
        self.dmg = dmg
        self.rarity = rarity
        self.level = level

def randWeapon(factor):
    rarityKey = random.randint(1, factor)
    rarity = rarities[rarityKey]
    weapon = Weapon(rarity + ' ' + wordGen.genWord(random.randint(1,4))+' of ' + random.choice(adjectives) + ' ' + random.choice(nouns), random.randint(rarityKey*10, rarityKey*10 + percentOf(50, rarityKey)), rarity, random.randint(rarityKey-1, percentOf(10, rarityKey)))
    return weapon


class Player(Entity):
    """Meta-entity representing the discord user currently playing."""
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inv = []
        self.equippedArmor = None
        self.level = 0
        self.exp = 0
        self.prestige = 0
        self.state = 1
        self.protection = 0
        self.equippedWeapon = None

    def addExp(self, amount):
        requiredExp = pow(self.level, 2)
        if self.exp + amount >= requiredExp:
            residue = requiredExp - (self.exp + amount)
            self.level += 1
            self.addExp(residue)
        else:
            self.exp += amount

    def addPrestige(self):
        self.inv = []
        self.equippedArmor = None
        self.level = 0
        self.exp = 0
        self.prestige += 1

class Enemy(Entity):
    """Basic entity that has an ability to deal damage to the player."""
    def __init__(self, name, damage, hp, protection):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.protection = protection
        self.state = 1

def fight(player, enemy):
    while player.state and enemy.state:
        try:
            enemy.receiveDamage(player.equippedWeapon.dmg)
            player.receiveDamage(enemy.damage)
        except:
            continue

print(randWeapon(2).name)
print('[RPGIO] Done loading game module')
