
"""Corrections des exercices"""

#afficher un mot à l'envers 
 
mot = input() 
 
for i in range(len(mot)) : 
   index = len(mot) - i -1 
   index = -1-i # calcul équivalent 
   print(mot[index],end="") 
    
>> ESCARGOT 
>> TOGRACSE 

# Calculer la valeur du polynôme 3x2 + 5x + 1 
 
for k in range(3) : 
 print("Entrez une valeur pour x :") 
 x = float(input()) 
 
 valeur = 3 * x * x + 5 * x + 1 
  
 print("f(x) =",valeur) 
  


# additionner n premiers entiers 
print("Entrez le nombre n : ") 
n = int(input()) 
 
somme = 0 
for i in range(n+1):    # piège : pensez à écrire n+1 
 somme = somme + i 
 
print ("Somme :",somme) 



# L'infiniment petit 
 
val = 1 
 
print("XX" + "0123456789" * 5) 
for i in range(50): 
 val = val / 2 
 print("{0:51.50f}".format(val)) 

# Compter les nombres à deux chiffres contenant le chiffre 7 
 
nb = 0 
 
for i in range(10,99) : 
 dizaine = i // 10 
 unite = i - 10 * dizaine 
 
 if dizaine == 7 or unite == 7 : 
   nb = nb + 1 
 
print("Réponse : ",nb) 

#Compter les consommes dans un mot 
 
print("Entrez un mot") 
mot = input() 
mot = mot.upper() 
 
nb_voyelles = 0 
nb_lettres = len(mot) 
 
for i in range(nb_lettres) : 
   lettre = mot[i] 
    
   if lettre == "A" or lettre == "E" or lettre == "I" or 
      lettre == "O" or lettre == "U" or lettre == "Y" : 
        nb_voyelles = nb_voyelles + 1 
         
nb_consonnes = nb_lettres - nb_voyelles 
 
print ("Nombre de consommes : ", nb_consonnes ) 



# Encoder et décrypter un nom 
print("Entrez le nom à coder : ") 
nom = input() 
nom = nom.upper() 
 
SECRET = "" 
 
for i in range(len(nom)): 
 ascii = ord(nom[i]) 
 code = ascii + 3 
 if code > ord('Z') : 
     code -= 26 
 SECRET += chr(code) 
  
print("CODE : ",SECRET) 
 
print("\n----------") 
 
print("Entrez le nom à décoder : ") 
nom = input() 
nom = nom.upper() 
 
DECODE = "" 
 
for i in range(len(nom)): 
 ascii = ord(nom[i]) 
 code = ascii - 3 
 if code < ord('A') : 
     code += 26 
 DECODE += chr(code) 
  
print("EN CLAIR : ",DECODE) 
 


#afficher les balises d'une page HTML 
 
CodePageWeb = "<html><head><title>Mon Titre</title></head><body>Texte sur la page</body></html>" 
 
print(CodePageWeb) 
 
for i in range(len(CodePageWeb)): 
 if CodePageWeb[i] == "<" : 
   ifin = CodePageWeb.find(">", I) 
   print(CodePageWeb[i+1:ifin]) 

# afficher le calendrier du mois 
 
print("Entrez le nombre de jours dans le mois : ") 
nbjours = int(input()) 
print("Entrez le premier jour du mois : 1 pour lundi, 7 pour dimanche") 
ColDepart = int(input()) 
 
print("LUN MAR MER JEU VEN SAM DIM") 
 
NbColVides = ColDepart - 1 
LargeurCol = 4 
print( " " * LargeurCol *  NbColVides, end="") 
ColCourante = ColDepart # 1 col du lundi, 7 col du dimanche 
 
for i in range(nbjours) : 
 print("{0:3d} ".format(i+1), end="") 
 ColCourante = ColCourante + 1 
 if ColCourante == 8 :  
   print() # une nouvelle ligne commence 
   ColCourante = 1 

# Statistiques avec pile ou face 
import random 
 
print("Donnez le nombre de tirages") 
nb = int(input()) 
 
nbPile = 0 
nbFace = 0 
for i in range(nb) : 
 PileFace = random.randint(0,1) 
 if PileFace == 0 : 
   nbPile += 1 
 else : 
   nbFace += 1 
 
pcPile = nbPile/nb*100 
pcFace = nbFace/nb*100 
print("Tirages Pile {0} : {1:2.0f} %".format(nbPile, pcPile) ) 
print("Tirages Face {0} : {1:2.0f} %".format(nbFace, pcFace) ) 
 

 

