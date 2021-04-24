#!/usr/bin/env python
# coding: utf-8
import random

total_matches=int(input('Total Matches >>'))

player_1_wins = 0

player_2_wins =0

game={0:'Rock',1:'Scissor',2:'Paper'}

def game_rule(one,two,rule=game):
    if one ==0: 
        if two == 1:
            return 'one_win'
        elif two==2:
            return 'two_win'
        elif  two == 0:
            return 'draw'
            
    if one ==1: 
        if two == 1:
            return 'draw'
        elif two==2:
            return 'one_win'
        elif  two == 0:
            return 'two_win'
        
    if one ==2: 
        if two == 1:
            return 'two_win'
        elif two==2:
            return 'draw'
        elif  two == 0:
            return 'one_win'

for i in range(total_matches):
    player_1 = random.randint(0,2)
    player_2 = random.randint(0,2)
    gam = game_rule(player_1,player_2)  
    if gam=='one_win':
        player_1_wins=player_1_wins+1
        print(f'Round {i} --> player_1 choose {game[player_1].center(10)}, player_2 choose {game[player_2].center(10)}====player_1 won')
    elif gam=='two_win':
        player_2_wins=player_2_wins+1
        print(f'Round {i} --> player_1 choose {game[player_1].center(10)}, player_2 choose {game[player_2].center(10)}====player_2 won')
    else:
        draw = total_matches-player_1_wins-player_2_wins
        print(f'Round {i} :-->player_1 choose {game[player_1].center(10)}, player_2 choose {game[player_2].center(10)}====Its Draw')

if (player_1_wins>player_2_wins):
    print('--------------player_1 won the round------------')
    print(f'---------------Total draws {draw}-----------------')
    print(f'---------------Total Wins {player_1_wins}-----------------')
elif(player_1_wins<player_2_wins):
    print('--------------player_2 won the round------------')
    print(f'---------------Total draws {draw}-----------------')
    print(f'---------------Total Wins {player_2_wins}-----------------')
else:
    print("======ITS draw======")