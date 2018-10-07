import os

# Probleme 16 ___________________________________

def digitsum(n):
    N=2**n
    c=str(N)
    S=0
    for k in c:
        d=int(k)
        S+=d
    return S

assert (digitsum(15))==26

print (digitsum(1000)) 
#=1366



# Probleme 22 ______________________________________

def valeurlettre(lettre):
    L=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k=0
    while lettre!=L[k]:
            k+=1
    return k 
    print (k)
    
assert (valeurlettre('K'))==11
        
        
    

def nscore():
    os.chdir("/Users/alixrenier/Documents/Mines/Info")
    Names=open('names.txt','r') #'r' permet de lire le fichier, 'w' permet de le modifie
    Stot=0
    for k in Names:
        ch=k
        L=ch.split(',')
        #print(L)
    T=sorted(L) #Liste des noms triés par ordre alphabétique
    #print (T)
    for i in range(len(T)): 
        position=i+1
        nom=str(T[i])
        Si=0
        for j in range(len(nom)):
            valeur=valeurlettre(nom[j])
            Si+=valeur
        Ai=Si*position
        Stot+=Ai
    return Stot
    
print(nscore())
#=87119882
            
            
            
# Probleme 55 _________________________________________

def revadd(n):  #Renverse n et renvoie sa somme avec n 
    N=str(n)
    L=str()
    for k in range(len(N)):
        L=L+N[len(N)-(k+1)]
    l=int(L)
    S=n+l
    return S
    
def estunlychrel (n) :
    S = n
    k = 0
    while k<50 and not palindrome(S) :
        S = revadd(S)
        k+=1
    if k < 50:
        return False
    else :
        return True
    
assert (revadd(47))==121


def palindrome(S): #Détermine si S est un palindrome
    C=str(S)
    k=0
    for i in range(int(len(C)/2)):
        if C[i]==C[len(C)-(i+1)]:
            k+=1
    return k==int(len(C)/2)

assert (palindrome(121))==True
    
    
def estunlychrel (n) :
    S = revadd(n)
    k = 0
    while k<50 and not palindrome(S) :
        S = revadd(S)
        k+=1
    if k < 50:
        return False
    else :
        return True
        
def solve(n) :
    N = 0
    for i in range(n) :
        if estunlychrel(i) :
            N+=1
    return N

#print (solve(10000))
#=249
            
        
        
    

    
        
        
            
        
        
