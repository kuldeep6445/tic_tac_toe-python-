import os
import sys


num = ['1','2','3','4','5','6','7','8','9']
turn = 1

def display():
    os.system('cls')
    print( num[0] , " | " , num[1] , " | " , num[2])
    print("   |     |")
    print("--------------")
    print( num[3] , " | " , num[4] , " | " , num[5])
    print("   |     |")
    print("--------------")
    print( num[6] , " | " , num[7] , " | " , num[8])
    print("   |     |")
    print(f"\t\t player {turn}'s turn\n")

def win():
    os.system('cls')
    print(f"!!!!!!!PLAYER {turn} WINS!!!!!!!! ")
    sys.exit()

def wincheck():
    for i in range(0,7,3):
        if num[i]==num[i+1] and num[i] == num[i+2]:
            win()

    for j in range(3):
        if num[j] == num[j+3] and num[j] == num[j+6]:
            win()

    if num[0] == num[4] and num[0] == num[8]:
        win()
    elif num[2] == num[4] and num[2] == num[6]:
        win()

while(True):
    
    
    display()
    a = int(input())
    if turn%2==1:
        num[a-1] = 'X'
        wincheck()
        turn =2

    else:
        num[a-1] = 'O'
        wincheck()
        turn =1

    
    
    