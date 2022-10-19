
# Tic Tac Toe ou "Jeu du morpion" in french
#
# [[_,_,_]
#  [_,_,_]
#  [_,_,_]]
#
#
#
def checkLines(m:list):
    i=0
    for l in m:
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != "_":
            return (True, i, m[i][0])
        i+=1
    return (False, None, None)

def checkColumns(m:list):
    i=0
    for c in m:
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != "_":
            return (True, i, m[0][i])
        i+=1
    return (False, None, None)

def checkDiagonals(m:list):
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != "_":
            return (True, "Diagonale", m[0][0])
    if m[0][2] == m[1][1] == m[2][0] and m[0][0] != "_":
            return (True, "Diagonale", m[0][2])



matrix = [["_","_","_"],["_","_","_"],["_","_","_"]]
print(matrix[0])
print(matrix[1])
print(matrix[2])

