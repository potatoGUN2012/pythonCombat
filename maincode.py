#Replit python game 
#Another combat but not with AI because on python its just dum and breaks everything
#Flashbacks to Another-dum-py :(

#Importing packages
import os
import time
from colorama import Fore

print(Fore.YELLOW+'Hello world!\n\nPowGoWoW:An all new retro pvp game!\n\n\n')
time.sleep(1)
print(Fore.YELLOW + "WowGoE:A small little PVP fighting game! Because those stuff are easy and fun on python\n\n")
print("""
WowGoE:

<Manual>
How to play:
In order to win the opponents health must be under 0. AKA you kill the other guy. There is lots of other stuff too

Controls:
The game has no GUI yet so all gameplay takes place in the console. You have to type what you want to implement on your turn. There will be a set of given options and you have to choose one. Type it in the given area when asked to.

Some Basic Gameplay:

So here are the most essential-ish moves...

[Y] Attack - Base form, Base energy, 10 damage
[H] Heal - Base form, Base energy, 10 health
[B] Block - Base form, Base energy, -10 health
[L] Long ranged - Base form, Medium energy, 10 damage
[M] Magery - Base form, Medium energy, 10 damage

And the most essential-ish other stuff

[P ATTK] - Potion of strentgh. Base x2, doubles your attack
[P DEF] - Potion of protection. Base x2, doubles your defence
[FSH] Cooked Fish. Immediate 25 health. Base x1.
[PLLW] Leather ballsack. Does 30 damage. Base x1

Summary:
Its game where you 1v1 in retro gaming style. Supposed to be based on Undertale. 

Also check out --> https://debean.github.io A very cool game

</Manual>
""")

#All the variables
player1HP = 150
player2HP = 150
player1DMG = 15
player1MG = 10
player2MG = 10
player2DMG = 10
player1HL = 10
player2HL = 15
consit12 = "t"
weakth1 = 0    
usg = 2
trn = 0

time.sleep(1)
#Charater name
name1 = input("What would you like to be your name? Player1: ")
name2 = input("What would you like to be your name? Player2: ")

#The actual game
while consit12 == "t":
  print("FIGHT!")

  #Choosing attack
  attk1 = input("Attack [y/l/m/h] > ")#Attack of player1
  attk2 = input("Attack [y/b/m/h] > ")#Attack of player2

  #Configuring attack
  
  if attk1 == "y":
    
    if weakth1 == 0:
      player2HP = player2HP-player1DMG
      print(f'{name1} Attacks! {name1} deals {player1DMG} damage')
      
    elif weakth1 == 3:
      player2HP = player2HP-(player1DMG-10)
      print(f'{name1} Attacks! {name1} is weakened and cannot!')
      
      weakth1 = 0
       #Attack
  elif attk1 == "h":
    
    player1HP = player1HP+player1HL
    
    print(f'{name1} Heals! {name1} regenerates 10 health')


     #Heal#HEal
  if attk2 == "y":
    
    player1HP = player1HP-player2DMG
    
    print(f'{name2} Attacks! {name2} deals 10 damage')
     #Attack(2)
  elif attk2 == "h":
    
    player2HP = player2HP+player2HL
    
    print(f'{name2} Heals! {name2} regenerates 10 health')
     #Heal(2)
  if attk1 == "m":
    
    energy = input('l/m/n')
    
    eff = 0

    
    if energy == "l":
      eff = 0.5
      
    elif energy == "m":
      eff = 1
      player1HP -= 5
      
    elif energy == "h":
      eff = 2
      player1HP -= 15
      
    else:
      print('Spell cast broken!')

      
    spell = input('Spell: ')
    
    if spell == "w@ter":
      
      ttldmgfr = 10*eff
      player2HP -= ttldmgfr
      
      print(f"{name1} summons waters! Dealing",ttldmgfr, "damage!")

   #Mage
  if attk2 == "m":
    
    energy = input('l/m/h')
    eff = 0 
    if energy == "l":
      eff = 1
      player2HP += 5 
    elif energy == "m":
      eff = 1
      player2HP -= 2
    elif energy == "h":
      eff = 2
      player2HP -= 10
    else:
      print('Spell cast broken!')
    
    spell = input('Spell: ')
    
    if spell == "f!res":
      
      
      ttldmgfr = 15*eff
      player1HP -= ttldmgfr

      
      print(f"{name2} summons fires! Dealing",ttldmgfr, "damage!")
      
    elif spell == "br0ken":
      
      
      ttldmgfr = 30*eff
      player1HP -= ttldmgfr
      
      
      print(f'{name2} summons the curse of brakchen! Dealing',ttldmgfr,"damage")
      
    elif spell == "weak3n":

      
      weakth1 = 3
      
      print(f'{name2} curses the opponent with the bane of sveneth IV! Weakening him by 10 damage')
       #Mage(2)
  if attk1 == "l":
    
    ardmg = 0
    inj = 0
    
    en1 = input("Energy [l/m/h] ")
    
    if en1 == "l":
      
      ardmg = 10
      
      print(f"{name2} Strikes a weak shot, but {name2} still deals {ardmg}")
      
    elif en1 == "m":

      
      ardmg = 20
      inj = 2
      
      print(f"{name2} Strikes a good shot! {name2} deals {ardmg}, but injures himself by {inj}")
      
    elif en1 == "h":

      
      ardmg = 35
      inj = 6
      
      print(f"{name2} Strikes a powerful shot! {name2} deals {ardmg}, but injures himself by {inj}")
      
    elif en1 == "p":
      ardmg = 40
      inj = 15
      print(f"{name2} Strikes a precision shot! {name2} deals {ardmg}, but injures himself by {inj}")
      
      
    player2HP -= ardmg
    player1HP -= inj
     #Long ranged
  if attk2 == "b":
    
    if usg > 0:
      
      hitPRC = input("Precision [l/h/u/p/c] ")
      
      if hitPRC == "l":
        
        player1HP -= 10
        usg -= 1
        
        print(f"{name2} lands some dynamite on the opponent! Dealing 10 damage!")
        
      elif hitPRC == "h":
        
        player1HP -= 15
        usg -= 1
        
        print(f"{name2} lands a C4 on the opponent! Dealing 15 damage!")
        
      elif hitPRC == "u":
        
        player1HP -= 25
        usg -= 2

        
        print(f"{name2} bombs the opponent! Dealing 25 damage!")
    



  #Winning  
         #Bomb (2)

  #Replaying Health  
  print("Player1:",player1HP)
  print("Playet2:",player2HP)
  suprior = "teee"#Checking who has moar health
  #if turn == 1:
    #print("/n/n/nWhat a wonderful beggining to a great match as ")
  if player1HP > player2HP:
    suprior == "Player1"
  elif player2HP > player1HP:
    suprior == "Player2"
  
  if player2HP < 1:
    consit12 = "f"
    print('Player1 wins')
    
  if player1HP < 1:
    consit12 = "f"
    print('Player2 wins')

  #Giving HP



