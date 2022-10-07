#main.py

#use list as a graph for now, eventually read from file or (interactive pygame UI?)


#convert pattern to grid of 1's and 0's 
#1's indicate point that will need to be used
#grid len and wid is +1 of pattern
#pattern coord = top left grid coord (pygame coordinate system)
#pattern = (0,2)
#corresponding grid points around it are (0,2) (1,2) (0,3) (1,3)

#start with given pattern, return path to stitch all colours together
#case where all colour is connected
def pattern_to_grid(pattern):
    grid=[]
    return grid

def flood(pos:tuple,pattern:list[list[str]],col:str,seen:list[tuple]):
    x=pos[0]
    y=pos[1]
    seen.append((x,y))

#start with given pattern, return path to stitch all colours together
#case where all colour is connected
def stitch_path(pattern:list[list[str]],col:str):
    seen=[]
    for x in range(len(pattern)):
        for y in range(len(pattern[x])):
            
            if((x,y) in seen or pattern[x][y] != col):
                continue
            flood((x,y),pattern,col,seen)




pattern = [['w','w','w','w'],
            ['w','r','r','w'],
            ['w','r','r','w'],
            ['w','w','w','w']]

grid = [[0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
        ]

