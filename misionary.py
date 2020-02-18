flag = "true"
visit=[]

def dfs(M,C,m,c):
    global flag
    if (M < 0 or C < 0 or m < 0 or c < 0):
        return False
    if ((M and C > M) or (m and c > m)):
        return False

    if (flag=="false" and M == 0 and C == 0 or (flag=="false" and m == 0 and c == 0)):
        return True

    if (flag=="false") :
        s=[M,C,m,c,"left"]
    else:
        s=[m,c,M,C,"right"]

    st= str(s)
    for i in visit:
        if (i == st):
            return False

    visit.append(st);
    if flag=="true":
        flag = "false"
    else:
        flag = "true"

    if (dfs(m + 2, c, M - 2, C)==True):
        print("2,0",'\n')
        print(s, '\n')
        return True

    elif (dfs(m, c + 2, M, C - 2)):
        print("0,2", '\n')
        print(s, '\n')
        return True

    elif (dfs(m + 1, c + 1, M - 1, C - 1)):
        print("1,1", '\n')
        print(s, '\n')
        return True

    elif (dfs(m + 1, c, M - 1, C)):
        print("1,0", '\n')
        print(s, '\n')
        return True

    elif (dfs(m, c+1, M, C-1)):
        print("0,1", '\n')
        print(s, '\n')
        return True

    if flag=="true":
        flag = "false"
    else:
        flag = "true"
    visit.pop()
    return False

M = 3
C = 3
m = 0
c = 0
zy= [M,C,m,c,"left"]
if (dfs(M, C, 0, 0)== False):
    print("Can not find the solution.")