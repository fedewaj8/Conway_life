import matplotlib.pyplot as plt
import numpy as np

def conway(board):
    '''
    Iterates Conway's Game of Life once
    '''
    new_board = np.copy(board)
    for y in range(0,len(board[0,:])-1):
        for x in range(0,len(board[:,0])-1):
            neigh = board[y,x+1] + board[y,x-1] + board[y+1,x] + board[y-1,x] + board[y+1,x+1] + board[y+1,x-1] + board[y-1,x+1] + board[y-1,x-1]
#             print(y,x,neigh)
            if board[y,x] == 1:
                if neigh < 2:
                    new_board[y,x] = 0
                if neigh > 3:
                    new_board[y,x] = 0
            if board[y,x] == 0 and neigh == 3:
                new_board[y,x] = 1
    return new_board



def conway_iter(board,N_iter,t_pause=0.01,saveimgs=False,figsize=(5,5)):
    '''
    Iterates Conway's Game of Life using given board N_iter times
    '''
    i=0
    for i in range(N_iter):
        
        plt.figure(figsize=figsize)
        plt.axis('off')
        plt.imshow(board,interpolation='nearest')
        
        if saveimgs == True:
            plt.axis('off')
            plt.savefig('conway_{:0>3}'.format(i))
            i+=1
        plt.pause(t_pause)
        board = conway(board)
        
    plt.show()
    
    