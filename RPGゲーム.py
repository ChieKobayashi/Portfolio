#HERO

import datetime
import sched
import time
import random

flag = 0
Enemy = ""
E_hp = 0
E_at = 0

class Hero :
    def __init__(self,hp = 0, money = 0, atk = 0, num = 0):
        self.hp = hp
        self.money = money
        self.atk = atk
        self.num = num
        
    def rest(self):
        hp_up = random.randint(80, 100)
        Hero.hp += hp_up
        Hero.money -= 10
    
    def levelup(self):
        Hero.hp += random.randint(50,100)
        Hero.money += random.randint(10,30)
        Hero.atk += random.randint(50,100)
        Hero.num += 1

        
    def attack(self):
        print("")
        print(HERO_name,"の攻撃",Hero.atk,"のダメージ！")
        Enemy.hp -= Hero.atk
        print(Enemy_name,"の攻撃",Enemy.atk,"のダメージ！")
        Hero.hp -= Enemy.atk

class Enemy :
    def __init__(self, hp=0, mp=0, atk=0):
        self.hp = hp
        self.atk = atk


HERO_name=input("王：勇者よ、君のお名前は？　名前：")
print("\n王：" + HERO_name +"、君はいまからダンジョンに囚われているプリンセスを救出する▽ ")
input("王：ダンジョンの中には様々なモンスターがおり▽ ")
input("王：ダンジョンには無限にモンスターが湧いてくる▽ ")
input("王：HPが1000を超えたら聖なるパワーが発動し、全てのモンスターは浄化されて、プリンセスを救出できる！▽ ")
input("王：モンスターを倒していくほど、レベルアップしてHPが上がる。▽ ")
input("王：宿で休みを取ったら、10ゴールドは減るが、HPは上がる。適度に休みを取ると良い。▽ ")
input("王：プリンセスを救えるのは勇者だけだ！▽ ")
input("王：では、頼んだぞ！▽ ")

Hero = Hero()
Hero.hp = random.randint(80,150)
Hero.money = random.randint(10,30)
Hero.atk = random.randint(80,120)

enemies=["ドラゴン", "ゴブリン", "ゴースト", "ドラキー", "メタルスライム"]

Enemy = Enemy()
Enemy_name = random.choice(enemies)
Enemy.hp = random.randint(30,150)
Enemy.atk = random.randint(10,100)


#ENEMY

while True:

    if Hero.hp >= 1000: #表示
        input("\nおめでとうございます。HPが1000を超えました！！▽ ")
        input("モンスターが全て浄化されました▽ ")
        input("プリンセスを救出できました▽ ")
        input("勇者はプリンセスに一目惚れをした▽ ")
        input("王：勇者よ。プリンセスを救出してくれてありがとう。▽ ")
        input("王：報酬としてプリンセスと結婚をさせてあげよう。▽")
        input( "その後、勇者とプリンセスは結婚して幸せな毎日を過ごしました。▽ ")
        input("めでたし。めでたし。▽ ")
        print("おしまい。▽ \n")
        time.sleep(5)
        break

    elif Hero.hp <= 0:
        print("G A M E  O V E R")
        time.sleep(5)
        break

    print("\n\nこれからなにをしよう？▽\n\n**********メニュー********** ")
    menu = input("1)ステータス確認 2)休む 3)ダンジョンに進む 9)リタイア　▽\n:"  )
    
    if menu == "1":#ステータス表示
        print("ステータスを表示します \n")
        print("\n勇者", HERO_name, "\nHP", Hero.hp, "\n所持金", Hero.money, "$\n攻撃力", Hero.atk)
        print("\nメニューに戻る▽ ")
        continue

    elif menu == "2": #HP回復
        input("宿泊料金は10ゴールドになります▽ ")
        if Hero.money < 10:
            print()
            input("お金が足りませんでした▽ ")
            continue
        Hero.rest()
        input("HPが上がりました！▽ ")
        continue
 
    elif menu == "3": #ダンジョンに進む
            input("\nモンスターが現れた！▽ ")
            print(Hero.num)
            Enemy_name = random.choice(enemies)
            Enemy.hp = random.randint(30,150)
            Enemy.atk = random.randint(10,100)
            if 3 >= Hero.num >= 2 :
                Enemy.hp += random.randint(50,100)
                Enemy.atk += random.randint(50,100)
            elif Hero.num >= 4 :
                Enemy.hp += random.randint(100,300)
                Enemy.atk += random.randint(100,300)

            while True:
                print("\n君の名前:",HERO_name,"HP:",Hero.hp,"攻撃力:",Hero.atk,"▽ ")
                print("敵の名前:",Enemy_name,"HP:",Enemy.hp,"攻撃力:",Enemy.atk,"▽ ")
                if Hero.hp <= 0:
                    input(HERO_name + "は死んでしまった！▽ ")
                    break
                elif Enemy.hp <= 0:
                    input("\nモンスターを撃破した▽ ")
                    input("経験値をたくさんもらった▽ ")
                    print(HERO_name,"のHPが上がった！▽ ")
                    Hero.levelup()
                    break
                print("\n\n**********バトルメニュー********** ")
                bt=input("1)たたかう 2)逃げる:▽ " )
                
                if bt == "1":
                    Hero.attack()
                    continue
                
                elif bt == "2":
                    print("\n", HERO_name, "は逃げ出した ")
                    break
            
                            
    elif menu == "9":
        print("\n他の勇者がプリンセスを救出しました。", HERO_name, "は田舎へ帰りました。▽ \n")
        print("G A M E  O V E R")
        time.sleep(5)
        break

    else:
        print("\nメニューの数字を入力ください")
        continue

