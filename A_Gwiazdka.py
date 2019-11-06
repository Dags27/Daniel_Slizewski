import math
import sys
def readGrid():
    file = open("grid.txt","r")
    content=file.read()
    file.close()
    return content

def addO():
    var = [0 for i in range(2)]
    return var

def addC():
    var = [5 for i in range(2)]
    return var

def createMap(content,o,c):
    m= [[[0 for i in range(20)]for j in range(20)]for k in range(3)]
    z=0
    for i in range(20):
        for j in range(20):
            if(content[z]=='5'):
                m[0][i][j]='X'
            z+=2
    m[0][c[0]][c[1]]='C'
    m[1]=[[m[0][j][i] for i in range(20)] for j in range(20)]
    m[2]=[[m[0][j][i] for i in range(20)] for j in range(20)]
    m[0][o[0]][o[1]] = 'O'

    return m

def findC(p,m):
    x=p[0]
    y=p[1]
    if x+1<20:
        if m[0][x+1][y]=='C':
            return True
    if x-1<-1:
        if m[0][x-1][y]=='C':
            return True
    if y+1<20:
        if m[0][x][y+1]=='C':
            return True
    if y-1<-1:
        if m[0][x][y-1]=='C':
            return True
    return False

def count(x,y,cx,cy):
    return float(math.sqrt(pow(x-cx,2)+pow(y-cy,2)))

def addCount(p,o,c,m): #Pozycja | Obiekt | Cel | Mapa
    x=p[0]
    y=p[1]
    #print(x,y)
    if x+1<20:
        if m[0][x+1][y]==0:
            m[0][x+1][y]=count(x+1,y,c[0],c[1])
            m[1][x+1][y]=m[1][x][y]+1
            m[2][x+1][y]='O'
    if x-1>-1:
        if m[0][x-1][y]==0:
            m[0][x-1][y]=count(x-1,y,c[0],c[1])
            m[1][x-1][y] = m[1][x][y] + 1
            m[2][x-1][y] = 'O'
    if y+1<20:
        if m[0][x][y+1]==0:
            m[0][x][y+1]=count(x,y+1,c[0],c[1])
            m[1][x][y+1] = m[1][x][y] + 1
            m[2][x][y+1] = 'O'
    if y-1>-1:
        if m[0][x][y-1]==0:
            m[0][x][y-1]=count(x,y-1,c[0],c[1])
            m[1][x][y-1] = m[1][x][y] + 1
            m[2][x][y-1] = 'O'


    m[2][x][y]='X'

def min(m):
     min=float("inf")
     pos=[float("inf") for i in range(2)]
     for i in range(20):
         for j in range(20):
             if m[2][i][j]=='O':
                 if min>m[1][i][j]+m[0][i][j]:
                     min=m[1][i][j]+m[0][i][j]
                     pos[0]=i
                     pos[1]=j
     return pos

def theWay(c,o,m,w): #Cel(Start) Obiekt(Koniec) Mapa
    x=c[0]
    y=c[1]
    min=float("inf")
    while min!=1:
        if x + 1 < 20:
            if m[1][x + 1][y] != 0 and m[1][x + 1][y] != 'X' and m[1][x + 1][y] != 'C':
                if min>m[1][x + 1][y]:
                    x = x + 1
                    min=m[1][x][y]
                    w[x][y]='D'
        if x - 1 > -1:
            if m[1][x - 1][y] != 0 and m[1][x - 1][y] != 'X' and m[1][x - 1][y] != 'C':
                if min>m[1][x - 1][y]:
                    x = x - 1
                    min=m[1][x][y]
                    w[x][y] = 'D'
        if y + 1 <20:
            if m[1][x][y + 1] != 0 and m[1][x][y + 1] != 'X' and m[1][x][y + 1] != 'C':
                if min>m[1][x][y + 1]:
                    y = y + 1
                    min=m[1][x][y]
                    w[x][y] = 'D'
        if y - 1 > -1:
            if m[1][x][y - 1] != 0 and m[1][x][y - 1] != 'X' and m[1][x][y - 1] != 'C':
                if min>m[1][x][y - 1]:
                    y = y - 1
                    min=m[1][x][y]
                    w[x][y] = 'D'

    return w

def wyswietl(x):

   for i in range(3):
        for j in range(20):
            for k in range(20):
                sys.stdout.write(str(x[i][j][k])+" ")
            print('')
        print('')
        print('=============================')
        print('')

def wyswietlWynik(x):
    print('')
    print('Wynik:')
    for j in range(20):
        for k in range(20):
            sys.stdout.write(str(x[j][k]) + " ")
        print('')

def main():
    obiekt=addO()
    cel=addC()
    mapa=createMap(readGrid(),obiekt,cel)
    wynik = [[mapa[0][j][i] for i in range(20)] for j in range(20)]
    addCount(obiekt,obiekt,cel,mapa)
    pozycja = min(mapa)
    while findC(pozycja,mapa)!=True:
        pozycja = min(mapa)
        if pozycja[0]==float('inf'):
            return False
        addCount(pozycja,obiekt,cel,mapa)
    w=theWay(cel,obiekt,mapa,wynik)
    wyswietlWynik(w)
    return True

print(main())