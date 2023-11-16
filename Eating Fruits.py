'''
The Packman Problem
AI lab
'''    

import copy 

""" Helper functions for checking operator's conditions """
   
def can_eat(state):
    for j in range(4):
        for i in range(len(state)):
            if state[j][i][0]=='p' and state[j][i][1]=='f':  
                return 1

def can_move_right(state):
    for j in range(4):
        for i in range(len(state)):
            if i == 3:
                return 0
            else:
                return not state[j][len(state)-1][0]=='p'

def can_move_left(state):
    for j in range(4):
        for i in range(len(state)):
            if i == 0:
                return not state[j][i][0]=='p'
            else:
                return
    
def can_move_up(state):
    for i in range(len(state)):
        for k in range(2):
            for j in range(1,4):
                return not state[j][i][k]=='p'
                
                    
def can_move_down(state):
    for i in range(len(state)):
        for k in range(2):
            for j in range(3):
                if j == 3:
                    return 0
                else:
                    return not state[j][i][k]=='p'
                

""" Operator function: eat, move right, move left """

def eat(state):
    if can_eat(state):
        for j in range(4):
            for i in range(len(state)):
                if state[j][i][0]=='p' and state[j][i][1]=='f':  
                    state[j][i][1]=''
                    return state
            

def move_right(state):
    if can_move_right(state):
        for j in range(4):
            for i in range(len(state)):
                if state[j][i][0]=='p':
                    state[j][i][0]=''
                    state[j][i+1][0]='p'
                    return state
    else: 
        return



         
def move_left(state):
    if can_move_left(state):
        for j in range(4):
            for i in range(len(state)):
                if state[j][i][0]=='p':
                    state[j][i][0]=''
                    state[j][i-1][0]='p'
                    return state
    else:
        return
        
        
        
def move_up(state):
    if can_move_up(state):
        for j in range(1,4):
            for i in range(len(state)):
                if state[j][i][0]=='p':
                    state[j][i][0]=''
                    state[j-1][i][0]='p'
                    return state
    else:
        return state

def move_down(state):
    if can_move_down(state):
        for j in range(0,3):
            for i in range(len(state)):
                if state[j][i][0]=='p':
                    state[j][i][0]=''
                    state[j+1][i][0]='p'
                    return state
    else:
        return state




inty = [
    [['',''],['','f'],['',''],['','f']],
    [['',''],['p','f'],['',''],['','f']],
    [['','f'],['','f'],['','f'],['','f']],
    [['',''],['','f'],['','f'],['','f']],
    ]


#initial_state=[initial_state1, initial_state2, initial_state3, initial_state4]

print(inty) 
print('\n')

print(eat(inty))
print('\n')

print(move_up(inty))
print('\n')

print(eat(inty))
print('\n')

print(move_left(inty))
print('\n')
print(move_left(inty))
print('\n')
print(move_up(inty))
print('\n')
print(move_left(inty))
print('\n')
print(move_right(inty))
print('\n')
print(move_right(inty))
print('\n')
print(move_right(inty))
print('\n')
print(move_right(inty))
print('\n')
print(eat(inty))
print('\n')
print(move_down(inty))
print('\n')
print(eat(inty))
print('\n')

