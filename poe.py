#Choose a primary skill
#Choose an ascendancy
#Choose a keystone
#Choose a weapon setup
#choose a unique

#To Do:
#   Check list of weapons/spells
#   implement tkinter?
#   add optional weights? ex heavy strike more likely to roll 2h or spells less likely to roll non-staff, wand, mace, or dagger

#Non-functional rolls to remove?:
#   Resolute Technique and any non-melee
#   Point Blank and non-projectile
#   Necromanic Aegis w/o 1h and Shield - removed NA from keystone pool
#   The Goddes Bound series (shows as 1h sword)


#Program should choose 1 main skill to use, 1 ascendancy class, 1 keystone, a weapon type, and a unique.
    #If the unique rolls as a weapon, it should check the allowed weapons of the main skill and roll a unique that fits the type
    #Program should use choice(attack.AllowedWeapons) and then check against a list of uniques of that type, ex Mace = []

from random import randint
from random import choice
import re
import sys
import os
import requests

allWeps = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff", "Claw", "Dagger", "Wand", "Bow"]

allMelee = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff", "Claw", "Dagger"]

nonDag = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff"]

all1h = ["1h Axe", "1h Mace", "1h Sword", "Claw", "Dagger"]

all2h = ["2h Axe", "2h Mace", "2h Sword", "Staff"]

allRanged = ["Wand", "Bow"]


class Attack(object):
    AllowedWeapons = []
    DualWield = 0
    TwoHander = 0
    Shield = 0
    Bow = 0
    Attack = 1
    Spell = 0

class AncestralProtector(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class AncestralWarchief(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class BladeFlurry(Attack):
    AllowedWeapons = ["Dagger", "1h Sword", "Claw"]
    DualWield = 1
    Shield = 1

class Cleave(Attack):
    AllowedWeapons = ["1h Axe", "2h Axe", "1h Sword", "2h Sword"]
    DualWield = 1
    TwoHander = 1

class DominatingBlow(Attack):
    AllowedWeapons = allMelee
    DualWeild = 1
    TwoHander = 1
    Shield = 1

class Earthquake(Attack):
    AllowedWeapons = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "Staff"]
    DualWield = 1
    TwoHander = 1

class GlacialHammer(Attack):
    AllowedWeapons = ["1h Mace", "2h Mace", "Staff"]
    DualWield = 1
    TwoHander = 1
    Shield = 1

class GroundSlam(Attack):
    AllowedWeapons = ["1h Mace", "2h Mace", "Staff"]
    DualWield = 1
    TwoHander = 1
    Shield = 1

class HeavyStrike(Attack):
    AllowedWeapons = nonDag
    DualWield = 1
    TwoHander = 1
    Shield = 1

class IceCrash(Attack):
    AllowedWeapons = nonDag
    DualWield = 1
    TwoHander = 1
    Shield = 1

class InfernalBlow(Attack):
    AllowedWeapons = nonDag
    DualWield = 1
    TwoHander = 1
    Shield = 1

class LeapSlam(Attack):
    AllowedWeapons = nonDag
    DualWield = 1
    TwoHander = 1
    Shield = 1

class MoltenStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class ShieldCharge(Attack):
    AllowedWeapons = all1h
    Shield = 1

class StaticStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class Sunder(Attack):
    AllowedWeapons = ["1h Mace", "2h Mace", "1h Axe", "2h Axe", "Staff"]
    DualWield = 1
    TwoHander = 1
    Shield = 1

class Sweep(Attack):
    AllowedWeapons = all2h
    DualWield = 1
    TwoHander = 1
    Shield = 1

class VigilantStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class Barrage(Attack):
    AllowedWeapons = allRanged
    DualWield = 1
    Shield = 1
    Bow = 1

class BlastRain(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class BurningArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class CausticArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class Cyclone(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class DoubleStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class DualStrike(Attack):
    AllowedWeapons = all1h
    DualWield = 1

class ElementalHit(Attack):
    AllowedWeapons = allWeps
    DualWield = 1
    TwoHander = 1
    Shield = 1
    Bow = 1

class ExplosiveArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class FlickerStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class Frenzy(Attack):
    AllowedWeapons = allWeps
    DualWield = 1
    TwoHander = 1
    Shield = 1
    Bow = 1

class FrostBlades(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    Shield = 1

class IceShot(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class Lacerate(Attack):
    AllowedWeapons = []
    DualWield = 1

class LightningArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class LightningStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class MirrorArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class Puncture(Attack):
    AllowedWeapons = ["Bow", "Dagger", "Claw", "1h Sword", "2h Sword"]
    DualWield = 1
    TwoHander = 1
    Shield = 1
    Bow = 1

class RainOfArrows(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class Reave(Attack):
    AllowedWeapons = ["Dagger", "Claw", "1h Sword"]
    DualWield = 1

class ShrapnelShot(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class SiegeBallista(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class SpectralThrow(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1
    Bow = 1

class SplitArrow(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class TornadoShot(Attack):
    AllowedWeapons = ["Bow"]
    Bow = 1

class ViperStrike(Attack):
    AllowedWeapons = ["Dagger", "Claw", "1h Sword", "2h Sword"]
    DualWield = 1
    TwoHander = 1
    Shield = 1

class WhirlingBlades(Attack):
    AllowedWeapons = ["1h Sword", "Dagger", "Claw"]
    DualWield = 1
    Shield = 1

class WildStrike(Attack):
    AllowedWeapons = allMelee
    DualWield = 1
    TwoHander = 1
    Shield = 1

class KineticBlast(Attack):
    AllowedWeapons = ["Wand"]
    DualWield = 1
    Shield = 1
    Bow = 1

class PowerSiphon(Attack):
    AllowedWeapons = ["Wand"]
    DualWield = 1
    Shield = 1
    Bow = 1

class Spell(object):
    AllowedWeapons = allWeps
    DualWield = 1
    TwoHander = 1
    Shield = 1
    Bow = 1
    Spell = 1
    Attack = 0

class AnimateGuardian(Spell):
    pass

class FlameTotem(Spell):
    pass

class SearingBond(Spell):
    pass

class ShockwaveTotem(Spell):
    pass

class SummonFlameGolem(Spell):
    pass

class SummonStoneGolem(Spell):
    pass

class AnimateWeapon(Spell):
    pass

class BladeVortex(Spell):
    pass

class Bladefall(Spell):
    pass

class Desecrate(Spell):
    pass

class EtherealKnives(Spell):
    pass

class FireTrap(Spell):
    pass

class FreezeMine(Spell):
    pass

class IceTrap(Spell):
    pass

class SummonIceGolem(Spell):
    pass

class Arc(Spell):
    pass

class ArcticBreath(Spell):
    pass

class BallLightning(Spell):
    pass

class ColdSnap(Spell):
    pass

class ConversionTrap(Spell):
    pass

class Discharge(Spell):
    pass

class EssenceDrain(Spell):
    pass

class FireNovaMine(Spell):
    pass

class Fireball(Spell):
    pass

class Firestorm(Spell):
    pass

class FlameDash(Spell):
    pass

class Flameblast(Spell):
    pass

class FreezingPulse(Spell):
    pass

class FrostBomb(Spell):
    pass

class Frostbolt(Spell):
    pass

class GlacialCascade(Spell):
    pass

class IceNova(Spell):
    pass

class IceSpear(Spell):
    pass

class Incinerate(Spell):
    pass

class LightningTendrils(Spell):
    pass

class LightningWarp(Spell):
    pass

class MagmaOrb(Spell):
    pass

class OrbOfStorms(Spell):
    pass

class RaiseSpectre(Spell):
    pass

class RaiseZombie(Spell):
    pass

class RighteousFire(Spell):
    pass

class ShockNova(Spell):
    pass

class Spark(Spell):
    pass

class StormCall(Spell):
    pass

class SummonChaosGolem(Spell):
    pass

class SummonLightningGolem(Spell):
    pass

class SummonRagingSpirit(Spell):
    pass

class SummonSkeletons(Spell):
    pass

class Vortex(Spell):
    pass

class Blight(Spell):
    pass

class ScorchingRay(Spell):
    pass

ascendancy = ["Ascendant", "Ascendant", "Ascendant", "Gladiator", "Slayer", "Champion",
                  "Juggernaut", "Berserker", "Chieftan", "Pathfinder", "Deadeye", "Raider",
                  "Assassin", "Saboteur", "Trickster", "Elementalist", "Necromancer", "Occultist",
                  "Inquisitor", "Heirophant", "Guardian"]

keystone = ["Acrobatics", "Ancestral Bond", "Arrow Dancing", "Avatar of Fire", "Blood Magic",
            "Chaos Inoculation", "Eldritch Battery", "Elemental Equilibrium", "Elemental Overload",
            "Ghost Reaver", "Iron Grip", "Iron Reflexes", "Mind Over Matter", "Pain Attunement",
            "Point Blank", "Resolute Technique", "Unwavering Stance", "Vaal Pact", "Zealot's Oath"]

slots = ["helmets", "amulets", "belts", "rings", "body_armours", "boots", "gloves", "weapon"]


def attacks():
    return Attack.__subclasses__()

def spells():
    return Spell.__subclasses__()


def mainpick(attacks, spells):
    atorsp = randint(1, 2)
    if atorsp == 1:
        atorsp = choice(attacks)
    else:
        atorsp = choice(spells)
    return atorsp

def weppick(attack):
    weapon = []
    if attack.DualWield == 1:
        weapon.append("Dual Wield")
    if attack.TwoHander == 1:
        weapon.append("Two Hander")
    if attack.Shield == 1:
        weapon.append("1h and Shield")
    if attack.Bow == 1:
        weapon.append("Bow")
    return weapon

def keystonepick(attack, weapon):
    while True:
        poekeystone = choice(keystone)
        if attack.Spell == 1 and poekeystone != "Resolute Technique":
            return poekeystone
        elif attack.Spell == 0:
            return poekeystone

def uniquepick(attack, weapon):
    selection = choice(slots)
    newselection = []
    print(selection)  
    
    if selection == "weapon":
        if weapon == "Two Hander":
            selection = attack.AllowedWeapons
            for s in selection:
                if "2h" in s or s == "Staff":
                    newselection.append(s)
        elif weapon == "1h and Shield" or weapon == "Dual Wield":
            selection = attack.AllowedWeapons
            for s in selection:
                if "1h" in s or s == "Dagger" or s == "Claw" or s == "Wand":
                    newselection.append(s)
        elif weapon == "Bow":
            newselection.append("Bow")

        selection1 = [i for i in newselection if i in attack.AllowedWeapons]
        selection = choice(selection1)
          
        if selection == "1h Axe":
            selection = "one_hand_axes"
        elif selection == "2h Axe":
            selection = "two_hand_axes"
        elif selection == "Staff":
            selection = "staves"
        elif selection == "Claw":
            selection = "claws"
        elif selection == "Dagger":
            selection = "daggers"
        elif selection == "Wand":
            selection = "wands"
        elif selection == "1h Sword":
            selection = choice(["one_hand_swords", "thrusting_one_hand_swords"])
        elif selection == "2h Sword":
            selection = "two_hand_swords"
        elif selection == "1h Mace":
            selection = choice(["one_hand_maces", "sceptres"])
        elif selection == "2h Mace":
            selection = "two_hand_maces"
        elif selection == "Bow":
            selection = "bows"
  
    url = "http://pathofexile.gamepedia.com/List_of_unique_{}".format(selection)
    r = requests.get(url)
    r_html = r.text
    
    first = re.findall(r'<span class="inline-infobox-container"><a href="/\w*" title="(\w*\s?\w*\s?\w*\s?\w*\s?\w*)', r_html)
    try:
        unique = choice(first)
    except IndexError:
        print("List empty!")
    return unique

if __name__=="__main__":
    print("Welcome to Path of Exile Ultimate Bravery!")
    print("Type 'new' to generate a new build, or type 'exit' to close")
    counter = 0
    while True:
        if counter < 1:
            while True:
                user = input("Option: ")
                if user.lower() == "new":
                    break
                elif user.lower() == "exit":
                    sys.exit()
        else:
            pass
        print("\n" * 3)
        
        poeclass = choice(ascendancy)
        print(poeclass)

        attack = mainpick(attacks(), spells())
        attackname = re.findall('[A-Z][^A-Z]*', attack.__name__)
        modattackname = ""
        for word in attackname:
            modattackname = modattackname + word + " "
        print(modattackname)

        weapon = choice(weppick(attack))
        print(weapon)
        
        poekeystone = keystonepick(attack, weapon)
        print(poekeystone)

        unique = uniquepick(attack, weapon)
        print(unique)
                
        print("\nType 'save' to save this build as a .txt, 'new' to generate a new build, or 'exit' to close.")
        counter = 1
        while True:
            user = input("Option: ")
            if user.lower() == "new":
                break
            elif user.lower() == "exit":
                sys.exit()
            elif user.lower() == "save":
                file = input("Name the file: ")
                file = file + ".txt"
                with open(file, 'w') as f:
                    f.write("Path of Exile Ultimate Bravery Build:\n\n")
                    f.write(poeclass + "\n")
                    f.write(modattackname + "\n")
                    f.write(weapon + "\n")
                    f.write(poekeystone + "\n")
                    f.write(unique)
                print("File saved: " + os.path.abspath(file))
