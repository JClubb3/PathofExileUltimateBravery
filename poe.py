"""
Choose a primary skill
Choose an ascendancy
Choose a keystone
Choose a weapon setup
choose a unique

To Do:
   Check list of weapons/spells
   implement tkinter?
   add optional weights? ex heavy strike more likely to roll 2h or spells less likely to roll non-staff, wand, mace, or dagger
   allow optional number of keystones and uniques

Non-functional rolls to remove?:
   Resolute Technique and any non-melee - currently does not roll if main skill is a spell
   Point Blank and non-projectile
   Necromanic Aegis w/o 1h and Shield - removed NA from keystone pool
   The Goddes Bound series (shows as 1h sword)


Program should choose 1 main skill to use, 1 ascendancy class, 1 keystone, a weapon type, and a unique.
    If the unique rolls as a weapon, it should check the allowed weapons of the main skill and roll a unique that fits the type
    Program should use choice(attack.AllowedWeapons) and then check against a list of uniques of that type, ex Mace = []
"""

from random import randint
from random import choice
import re
import sys
import os
import requests

#These lists are simply shorthands for the below classes to pull from, and also for reference.

allWeps = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff", "Claw", "Dagger", "Wand", "Bow"]

allMelee = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff", "Claw", "Dagger"]

nonDag = ["1h Axe", "2h Axe", "1h Mace", "2h Mace", "1h Sword", "2h Sword", "Staff"]

all1h = ["1h Axe", "1h Mace", "1h Sword", "Claw", "Dagger"]

all2h = ["2h Axe", "2h Mace", "2h Sword", "Staff"]

allRanged = ["Wand", "Bow"]


class Attack(object):
    """
    Setup simple binary tags for other classes to inheret.
    
    Each of the below tags simply helps the rest of the program 
    determine valid targets for random assignments, and are based
    on the rules governing the skills in Path of Exile iteslf.
    
    Each attack should seperate words based on capitalization, and
    should indicate what weapons are allowed with it, as well as what
    weapon setups can be used.
    """
    
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
    """
    Setup simple binary tags for other classes to inheret.
    
    Just like the Attack base class above, this sets up rules
    for other spells to inheret to control the logic later
    in the script. Generally spells do not modify any of these
    rules, unlike Attacks, so most (if not all) class will have
    no values apart from what they inheret and will simply pass.
    """
    
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

"""These are all the Ascendancy classes in PoE, with Ascendant represented three times
in order to give Scion an equal roll chance compared to the other classes."""
ascendancy = ["Ascendant", "Ascendant", "Ascendant", "Gladiator", "Slayer", "Champion",
                  "Juggernaut", "Berserker", "Chieftan", "Pathfinder", "Deadeye", "Raider",
                  "Assassin", "Saboteur", "Trickster", "Elementalist", "Necromancer", "Occultist",
                  "Inquisitor", "Heirophant", "Guardian"]

"""The keystones, minus Conduit and Necromantic Aegis for irritating compatability reasons."""
keystone = ["Acrobatics", "Ancestral Bond", "Arrow Dancing", "Avatar of Fire", "Blood Magic",
            "Chaos Inoculation", "Eldritch Battery", "Elemental Equilibrium", "Elemental Overload",
            "Ghost Reaver", "Iron Grip", "Iron Reflexes", "Mind Over Matter", "Pain Attunement",
            "Point Blank", "Resolute Technique", "Unwavering Stance", "Vaal Pact", "Zealot's Oath"]

"""This list is used to roll the unique."""
slots = ["helmets", "amulets", "belts", "rings", "body_armours", "boots", "gloves", "weapon"]


def attacks():
    """Return a list of all the classes inhereting from Attack."""
    return Attack.__subclasses__()

def spells():
    """Return a list of all the classes inhereting from Spell."""
    return Spell.__subclasses__()


def mainpick(attacks, spells):
    """
    Return a main attack of spell for the build.
    
    attacks and spells will be the attacks() and spells()
    functions, which are themselves lists of all subclasses of
    Attack and Spell.
    """
    atorsp = randint(1, 2)
    if atorsp == 1:
        atorsp = choice(attacks)
    else:
        atorsp = choice(spells)
    return atorsp

def weppick(attack):
    """
    Determine the pool of allowable weapon setups.
    
    For whatever reason the actual choice is made in main.
    I don't know why I did this but whatever. This uses if
    and not elif chains because many times multiple setups
    will be valid choices and should be in the pool.
    
    attack is the main skill chosen by mainpick()
    An attack setup improperly will return an empty
    list, while an improperly setup spell will return a list
    of all weapons, assuming the object inherents from Attack 
    or Spell properly.
    """
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
    """
    Return a chosen keystone to be used by the build.
    
    Ultimately this will have checks for nonsensical rolls. Currently
    the only one is that Resolute Technique will not roll for any main
    skill inhereted from Spell, but more checks should be added.
    
    attack is the main skill detemined by mainpick().
    weapon is currently unused but should be used later for logic
    checks with keystones.
    """
    #A loop to ensure re-rolls on nonsensical results
    while True:
        poekeystone = choice(keystone)
        #Currently the only nonsense check, more should be added later.
        if attack.Spell == 1 and poekeystone != "Resolute Technique":
            return poekeystone
        elif attack.Spell == 0:
            return poekeystone

def uniquepick(attack, weapon):
    """
    Return a unique item for the build, pulled from the PoE wiki.
    
    attack is the main skill chosen by mainpick().
    weapon is the chosen weapon setup as chosen by weppick().
    This function will roll a class of items from the slots class,
    and then for any non-weapon roll will connected to
    pathofexile.gamepedia.com (using requests), and then preform a 
    regular expression search within the obtained HTML to find the
    names of all items of that class, and then choose one from
    among them. For a weapon roll, the function will create a new
    list based on the choice made by weppick() and the weapons the
    skill can used as defined by attack.AllowedWeapons.
    """
    selection = choice(slots)
    #Initialize a list used for the weapon comprhension
    newselection = []  
    
    #Begin the chain for choosing an appropriate weapon
    #if a weapon roll occurs.
    if selection == "weapon":
        #Check what setup rolled, and then apply the appropriate logic.
        if weapon == "Two Hander":
            #Check what weapons the skill supports
            selection = attack.AllowedWeapons
            #Then iterate through the list and add all valids ones to a new list.
            for s in selection:
                if "2h" in s or s == "Staff":
                    newselection.append(s)
        elif weapon == "1h and Shield" or weapon == "Dual Wield":
            #Check what weapons the skill supports
            selection = attack.AllowedWeapons
            #Then iterate through the list and add all valids ones to a new list.
            for s in selection:
                if "1h" in s or s == "Dagger" or s == "Claw" or s == "Wand":
                    newselection.append(s)
        #A bow roll requires little logic since bow is the only bow class.
        elif weapon == "Bow":
            newselection.append("Bow")

        #construct a third list, comprised of overlap between AllowedWeapons and
        #the weapons the chosen setup can use.
        selection1 = [i for i in newselection if i in attack.AllowedWeapons]
        #Finally, chose an item class from the comprehension above.
        selection = choice(selection1)
        
        #Converts the weapon identifier to the useable end of the URL.
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
        #The 1h Sword class has two subclasses that must be picked from.
        elif selection == "1h Sword":
            selection = choice(["one_hand_swords", "thrusting_one_hand_swords"])
        elif selection == "2h Sword":
            selection = "two_hand_swords"
        #The 1h Mace class also has two subclasses that must be picked from.
        elif selection == "1h Mace":
            selection = choice(["one_hand_maces", "sceptres"])
        elif selection == "2h Mace":
            selection = "two_hand_maces"
        elif selection == "Bow":
            selection = "bows"
  
    #Generate and retrieve the appropriate URL.
    #The wiki has nice pages with just, for example, a list of one-handed unique swords.
    url = "http://pathofexile.gamepedia.com/List_of_unique_{}".format(selection)
    r = requests.get(url)
    r_html = r.text
    
    #This regular expression will find all the item names in the HTML. The HTML has 
    #each item in a table, and each table row has the name of the item included. 
    #This will find that name, allowing for optional white space in the case of 
    #many-word item names.
    first = re.findall(r'<span class="inline-infobox-container"><a href="/\w*" title="(\w*\s?\w*\s?\w*\s?\w*\s?\w*)', r_html)
    #Attempts to make a choice of all the valid items. An empty list will fail 
    #the choice and raise an exception.
    try:
        unique = choice(first)
    except IndexError:
        print("List empty!")
    return unique

if __name__=="__main__":
    """
    Determine an Ultimate Bravery Build for Path of Exile.
    
    First this will welcome the user, and then prompt them.
    A new build will first choose and ascendancy, then a main
    damage skill (usually referred to as attack, though the skill
    may also be a spell). Then it will choose a valid weapon setup,
    and finally will choose a unique for the build, rolling from a
    list of all possible uniques by first choosing a slot and then
    pulling all the uniques for that slot and choosing one.
    
    Finally, the user will have the option to save the build and
    name the .txt file to which it will be saved (the program adds
    the file extension explicity), or to generate a new build or
    exit the program.
    """
    print("Welcome to Path of Exile Ultimate Bravery!")
    print("Type 'new' to generate a new build, or type 'exit' to close")
    #Initialize a variable and chain to control first iteration.
    #The counter variable prevents repeating the Option: input if the
    #user chooses to create a new build after creating the first.
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
                    print("Please make a valid choice.")
        else:
            pass
        print("\n" * 3)
        
        #Choose an ascendancy.
        poeclass = choice(ascendancy)
        print(poeclass)

        #Choose a main skill.
        attack = mainpick(attacks(), spells())
        #Grab the main skill's name and break it into a list based on capitilaztion.
        attackname = re.findall('[A-Z][^A-Z]*', attack.__name__)
        #Append each item of the list to a new string, adding spaces between words.
        modattackname = ""
        for word in attackname:
            modattackname = modattackname + word + " "
        print(modattackname)

        #Choose a weapon setup.
        weapon = choice(weppick(attack))
        print(weapon)
        
        #Choose a keystone.
        poekeystone = keystonepick(attack, weapon)
        print(poekeystone)

        #Choose a unique.
        unique = uniquepick(attack, weapon)
        print(unique)
                
        #Prompt the user and set counter to > 0, otherwise the Option: input will repeat and
        #the user will need to specify their desired action twice.
        print("\nType 'save' to save this build as a .txt, 'new' to generate a new build, or 'exit' to close.")
        counter = 1
        while True:
            user = input("Option: ")
            #If user chooses new, will loop back to the beginning of main
            if user.lower() == "new":
                break
            #Exits the script if users so desires.
            elif user.lower() == "exit":
                sys.exit()
            #Saves the build as a .txt.
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
                #Obtain the absolute file path for the created file and present it to the user.
                print("File saved: " + os.path.abspath(file))
            else:
                print("Please choose a valid option.")
