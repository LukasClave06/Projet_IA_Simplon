# Calculer la somme des éléments d'une liste 
L = [1, 2, 3, 4, 5, 6 ] 
 
somme = 0 
for i in range(len(L)) : 
  somme += L[i] 
 
print("Somme totale : " , somme) 
 
>> Somme totale : 28 

# Répartir les nombres impairs et pairs dans deux listes 
 
L      = [ 4 , 7, 9, 8, 66, 33, 21, 42 ] 
IMPAIR = [] 
PAIR   = [] 
 
for v in L : 
   if v%2 == 0 : 
       PAIR.append(v) 
   else: 
       IMPAIR.append(v) 
        
print("PAIR   : ",PAIR) 
print("IMPAIR : ",IMPAIR) 

# Compter les occurrences de chaque nombre dans une liste 
 
L = [ 0, 5, 8, 0, 5, 4, 4, 0, 0, 5, 0 ] 
 
comptage = [0] * 10 
 
for v in L : 
 comptage[v] += 1 
 
for v in range(10) : 
 if comptage[v] > 0 : 
   print("Chiffre {0} apparaît {1} fois".format(v,comptage[v])) 
 



# Faire apparaître une texture de grillage 
 
for i in range(10) : 
   for j in range (40) : 
       if (i+j) % 2 == 0 : 
           print ("X",end="") 
       else : 
           print( " ", end="") 
   print("") 

# Calculer les racines d'un polynome du 2nd degré 
import math 
 
print("Entrez a,b et c : ax2+bx+c=0") 
coefs = input() 
 
abc = coefs.split(" ") 
a = float(abc[0]) 
b = float(abc[1]) 
c = float(abc[2]) 
 
delta = b**2 - 4 * a * c 
 
if delta < 0 : 
   print("Aucune racine") 
else : 
   rdelta = math.sqrt(delta) 
   if rdelta == 0 : 
       print("1 racine : ", -b/(2*a)) 
   else: 
       r1 = (-b-rdelta)/ (2*a) 
       r2 = (-b+rdelta)/ (2*a) 
                
       print("2 racines : ", r1, r2) 
 
 


 
print("Nombres premiers trouvés : ") 
 
for k in range(1,100) : 
   premier = True 
   for v in range(2,k) : 
       if k%v == 0 : 
           premier = False 
   if premier : 
        print(k,end=" ") 
 


# Vérifier si une liste est triée 
L = [1,5,11,19,8,50,77] 
 
for i in range(len(L) - 1): # -1 pour ne pas traiter le dernier 
  v1 = L[i] 
  v2 = L[i+1] 
  if v2 < v1 : 
     print("Erreur ",v1,v2, "dans le mauvais ordre.") 



# décaler une liste 
L = [ 0, 1, 2, 3, 4, 5, 6, 7] 
 
print(L) 
for i in range(len(L)) : 
 element = L.pop() 
 L.insert(0,element) 
 print(L) 
 


# Construire un tableau de comparaison 
 
L1 = [ 5,15,20,77,98] 
L2 = [ 1,15, 18,55,60,65,77,80,85,93,99] 
 
print(" ",end='') 
for v2 in L2 : 
 print("{0:3}".format(v2), end = '') 
print() 
 
for v1 in L1 : 
 print("{0:3}".format(v1),end='') 
 
 for v2 in L2 : 
   if v1 < v2  : print(" <",end='') 
   if v1 == v2 : print(" =",end='') 
   if v1 > v2  : print(" >",end='') 
 print() 
 
 

# fusionner deux listes triées 
L1 = [ 1, 17, 22, 53, 75, 89] 
L2 = [ 0, 5, 7, 20, 25, 30, 58, 71, 80, 98, 99] 
 
R = [] 
i = 0 
j = 0 
nb1 = len(L1) 
nb2 = len(L2) 
 
while i<nb1 and j<nb2 : #il reste des éléments dans les 2 listes 
   if L1[i] < L2[j] :  # on traite l'élément de L1 et on avance 
       R.append(L1[i]) 
       i += 1 
   else :              # on traite l'élément de L2 et on avance 
       R.append(L2[j]) 
       j += 1 
        
while i < nb1 :   # on traite les éléments restants dans L1 
   R.append(L1[i]) 
   i += 1 
 
while j < nb2 :   # on traite les éléments restants dans L2 
   R.append(L2[j]) 
   j += 1 
    
print(R) 