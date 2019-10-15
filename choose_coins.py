"""
Name: Choo Jun Yi
Student ID: 30219396
Date: 6/9/2019
"""

def best_score(pile1,pile2):
    n1 = len(pile1)+1
    n2 = len(pile2)+1
    decision_array = []
    memo =[]   # create memoization table
    for i in range(n2):
        memo.append([(0,0)]*(n1))
    memo[0][0] = (0,0)

    # consider boundary cases
    if len(pile1) ==0 and len(pile2) == 0:
        return (0,[])
    elif len(pile1)==0:
        memo[1][0] = (pile2[0], 0)
    elif len(pile2)==0:
        memo[0][1] = (pile1[0], 0)
    else:
        memo[0][1] = (pile1[0],0)
        memo[1][0] = (pile2[0],0)

    # Constructing base case for the first row
    for i in range(2,len(pile1)+1):
        memo[0][i] = ((pile1[i-1]+memo[0][i-2][0]),memo[0][i-1][0])

    # Constructing base case for the first column
    for j in range(2,len(pile2)+1):
        memo[j][0] = ((pile2[j-1]+memo[j-2][0][0]),memo[j-1][0][0])

    for j in range(1,n2):
        for i in range(1,n1):
            if (pile1[i-1]+memo[j][i-1][1])>=(pile2[j-1]+memo[j-1][i][1]):
                memo[j][i] = (pile1[i-1]+memo[j][i-1][1],memo[j][i-1][0])
            else:
                memo[j][i] = (pile2[j-1]+memo[j-1][i][1],memo[j-1][i][0])

    # backtracking process
    a = len(pile1)
    b = len(pile2)
    for k in range(a + b):
        if b>0 and memo[b][a][0]-pile2[b-1] == memo[b-1][a][1]:
            decision_array.append(2)
            b-=1
        elif a>0 and memo[b][a][0]-pile1[a-1] == memo[b][a-1][1]:
            decision_array.append(1)
            a-=1

    return (memo[-1][-1][0],decision_array)


if __name__ == "__main__":
    best_score([5,8,2,4,1,10,2], [6,2,4,5,6,9,8])
