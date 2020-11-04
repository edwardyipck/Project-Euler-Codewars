import math
import numpy as np

alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
num = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20,21,22,23]
def queens(position, size):
    if size == 1:
        return "a1"
    pos_step = []
    
    #making the board
    board = np.empty([size,size],dtype=object)
    global fullboard
    fullboard = np.empty([size,size],dtype=object)
    for i in range(size):
        for j in range(size):
            fullboard[i,j] = str(str(alph[j])+str(num[:size][-i-1]))
            board[i,j] = "  "
    board_states = []

    #position coordinates
    pos = list(np.where(fullboard == position))
    if len(pos[0]) == 0:
        return None

    # first queen
    new_queen(position,size,board,board_states,pos_step) 
    board_states.append(np.copy(board))
    

    col_steps = [[i for i in range(size) if i != pos[1]]]
    
    find_spot(size,board,board_states,pos_step,col_steps)
    output = (str(",".join(sorted(pos_step))))
    if len(col_steps) ==0:
        return "There is no solution"
    print(board_states[-1])
    return output
    
def new_queen(new_position,size,board,board_states,pos_step):
    pos_step.append(new_position)
    pos = list(np.where(fullboard == new_position))

    #row
    for i in range(size):
        board[i,pos[1]]="- "
    
    #column
    for i in range(size):
        board[pos[0],i]="- "
     
    #diagonal1
    if pos[1]-pos[0] >=0:
        np.fill_diagonal(board[:,int(pos[1]-pos[0]):], "- ")
    else:
        np.fill_diagonal(board[int(pos[0]-pos[1]):], "- ")
    #diagonal2
    if pos[0]+pos[1]>=size:
        np.fill_diagonal(board[int(pos[1]-(size-pos[0])+1):,::-1], "- ")
    else:
        np.fill_diagonal(np.fliplr(board[:,:int(pos[1]+pos[0]+1)]), "- ")
    
    board[tuple(pos)]= new_position
    board_states.append(np.copy(board))
    
def find_spot(size,board,board_states,pos_step,col_steps):
    fill = 0
    i = col_steps[-1][0]
    for j in range(size):
        if board[j,i] != "  ":
            continue
        pos_found = str(str(alph[i])+str(num[:size][-j-1]))
        new_queen(pos_found,size,board,board_states,pos_step)
        fill = 1
        break
        
    if fill == 1:
        if len(pos_step)!=size:
            col_next = [a for a in col_steps[-1] if a !=i]
            col_steps.append(col_next)
            find_spot(size,board,board_states,pos_step,col_steps)
            return
        
    else:
        del board_states[-1]
        del col_steps[-1]
        board = np.copy(board_states[-1])
        if len(col_steps)==0:
            return
        d_spot = list(np.where(fullboard == pos_step[-1]))
        board[d_spot[0],d_spot[1]]= "# "
        del board_states[-1]
        board_states.append(np.copy(board))
        del pos_step[-1]
        find_spot(size,board,board_states,pos_step,col_steps)
        return
    
