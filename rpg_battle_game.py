import random

class color:
    BLUE ='\033[94m'

    GREEN='\033[92m'

    YELLOW ='\033[93m'

    FAIL = '\033[91m'

    END ='\033[0m'

    BOLD = '\033[1m'

    UNDERLINE ='\033[4M'

player_hp=500

enemy_hp=1000

bar_hp=25

bar1_hp=50

time=0

coins=100

run =True
bar=(color.GREEN+color.BOLD+"█"*bar_hp+color.END+color.BOLD+"Player HP"+color.END)
print(bar)

bar1=(color.FAIL+color.BOLD+"█"*bar1_hp+color.END+color.BOLD+"Enemy HP"+color.END)
print(bar1)
while run:
   
    enemy_spell=random.randint(1,9)
    if enemy_spell==1:
        enemy_hp=enemy_hp+200

        print(color.FAIL+"The enemy just healted for 200 HP\n Enemy HP now equals to "+str(enemy_hp)+color.END)

        bar1_hp_now=enemy_hp/20
        bars=round(bar1_hp_now)
        bar1=(color.FAIL+color.BOLD+"█"*bars+color.END+color.BOLD+"Enemy HP"+color.END)
        print(bar1)
       
   

    if enemy_spell==2:
        enemy_hp=enemy_hp+400

        print(color.FAIL+"The enemy just healted for 400 HP\n Enemy HP now equals to "+str(enemy_hp)+color.END)

        bar1_hp_now=enemy_hp/20
        bars=round(bar1_hp_now)
        bar1=(color.FAIL+color.BOLD+"█"*bars+color.END+color.BOLD+"Enemy HP"+color.END)
        print(bar1)


    if enemy_spell==3:
        enemy_hp=enemy_hp+50

        print(color.FAIL+"The enemy just healted for 50 HP\n Enemy HP now equals to "+str(enemy_hp)+color.END)

        bar1_hp_now=enemy_hp/20
        bars=round(bar1_hp_now)
        bar1=(color.FAIL+color.BOLD+"█"*bars+color.END+color.BOLD+"Enemy HP"+color.END)
        print(bar1)

    option =input(color.BOLD+"What do you want to do?\n"+color.BLUE+"1.Attack\n2.Spell")

    if option==str(1):
        if enemy_hp<0:
            enemy_hp=0
            exit("Well Done!! You defeated the enemy...")

    time=time+1

    enemy_hp=enemy_hp+random.randint(1,10)

    player_attack=random.randint(100,200)

    enemy_attack=random.randint(50,100)

    attack=player_hp-enemy_attack

    if attack<0:
        print(color.FAIL+color.BOLD+"Enemy attacked for "+str(enemy_attack)+color.END)
        print(color.GREEN+color.BOLD+"Player HP is now 0"+color.END)
        exit("You Lose")

    print(color.FAIL+color.BOLD+"Enemy attacked for "+str(enemy_attack)+color.END)

    print(color.GREEN+color.BOLD+"Player HP now equals to "+str(attack)+color.END)
    player_hp=attack

    attacks=enemy_hp-player_attack

    if attacks<0:
        exit("Well Done you defeated the enemy")

    print(color.GREEN+color.BOLD+"Player attacked for "+str(player_attack)+color.END)

    print(color.FAIL+color.BOLD+"Enemy HP now equals to "+str(attacks)+color.END)

    enemy_hp=attacks

    bar_hp_now=attack/20
    bar_hp=round(bar_hp_now)

    bar1_hp_now=attacks/20

    bar1_hp=round(bar1_hp_now)

    bar=(color.GREEN+color.BOLD+"█"*bar_hp+color.END+color.BOLD+"Player HP"+color.END)
    print(bar)

    bar1=(color.FAIL+color.BOLD+"█"*bar1_hp+color.END+color.BOLD+"Enemy HP"+color.END)
    print(bar1)

    if option==str(2):
        enemy_hp=enemy_hp+random.randint(1,30)

        choice_spell=input(color.BOLD+"what spell do you want to use?\n"+color.BLUE+"1)Curer-15\n2)Small Shield-10\n3)Big Shield-25\n4)Grenade-15\n5)C4-30\n6)Bomb-10\n"+color.END)

        if choice_spell==str(1):
            if coins<15:
                print(color.BOLD+"Not enough coins")
                continue
            player_hp=player_hp+100
            print(color.GREEN+color.BOLD+"Player HP now equals to "+str(player_hp)+color.END)
            coins-=15

            print("You have "+color.BOLD+str(coins)+"left")

            bar_hp_now=player_hp/20
            bars=round(bar1_hp_now)

            print(bar)
        

        if choice_spell==str(2):
            if coins<10:
                print(color.BOLD+"Not enough coins")
                continue
            player_hp=player_hp+50
            print(color.GREEN+color.BOLD+"Player HP now equals to "+str(player_hp)+color.END)
            coins-=10

            print("You have "+color.BOLD+str(coins)+"left")

            bar_hp_now=player_hp/20
            bars=round(bar1_hp_now)

            print(bar)
            
        if choice_spell==str(3):
            if coins<25:
                print(color.BOLD+"Not enough coins")
                continue
            player_hp=player_hp+20050
            print(color.GREEN+color.BOLD+"Player HP now equals to "+str(player_hp)+color.END)
            coins-=25

            print("You have "+color.BOLD+str(coins)+"left")

            bar_hp_now=player_hp/20
            bars=round(bar1_hp_now)

            print(bar)
        if choice_spell==str(4):
            if coins<15:
                print(color.BOLD+"Not enough coins")
                continue
            enemy_hp=enemy_hp-200
            if enemy_hp<0:
                enemy_hp=0
                exit("Well Done you defeated the enemy")

            print(color.FAIL+color.BOLD+"Enemy HP now equals to "+str(enemy_hp)+color.END)
            coins-=15

            print("You have "+color.BOLD+str(coins)+"left")

            bar1_hp_now=enemy_hp/20
            bars=round(bar1_hp_now)
            bar1=(color.FAIL+color.BOLD+"█"*bar1_hp+color.END+color.BOLD+"Enemy HP"+color.END)
            print(bar1)

        if choice_spell==str(5):
            if coins<30:
                print(color.BOLD+"Not enough coins")
                continue
            enemy_hp=enemy_hp-200
            if enemy_hp<0:
                enemy_hp=0
                exit("Well Done you defeated the enemy")

            print(color.FAIL+color.BOLD+"Enemy HP now equals to "+str(enemy_hp)+color.END)
            coins-=30

            print("You have "+color.BOLD+str(coins)+"left")

            bar1_hp_now=enemy_hp/20
            bars=round(bar1_hp_now)
            bar1=(color.FAIL+color.BOLD+"█"*bar1_hp+color.END+color.BOLD+"Enemy HP"+color.END)
            print(bar1)
        if choice_spell==str(6):
            if coins<10:
                print(color.BOLD+"Not enough coins")
                continue
            enemy_hp=enemy_hp-25
            if enemy_hp<0:
                enemy_hp=0
                exit("Well Done you defeated the enemy")

            print(color.FAIL+color.BOLD+"Enemy HP now equals to "+str(enemy_hp)+color.END)
            coins-=10

            print("You have "+color.BOLD+str(coins)+"left")

            bar1_hp_now=enemy_hp/20
            bars=round(bar1_hp_now)
            bar1=(color.FAIL+color.BOLD+"█"*bar1_hp+color.END+color.BOLD+"Enemy HP"+color.END)
            print(bar1)

            
            