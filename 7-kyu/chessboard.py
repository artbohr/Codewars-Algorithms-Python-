'''
A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

Making a digital chessboard I think is an interesting way of visualising how loops can work together.

Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

So chessBoard(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]

'''

def chess_board(rows, columns):
    result = []
    
    for x in range(rows):
        result.append([])
        if len(result[x])==0 and x%2==0:
            result[x].append("O")
        else:
            result[x].append("X")
            
        while len(result[x])!=columns:
            if result[x][-1]==("X"):
                result[x].append("O")
            else:
                result[x].append("X")
                     
    return result
    
print (chess_board(3,7))
# Outputs:

#[
# ["O","X","O","X","O","X","O"],
# ["X","O","X","O","X","O","X"],
# ["O","X","O","X","O","X","O"]
#]
