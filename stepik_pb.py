P = "((P > (Q * (S > T ))))" # propozitie
contor_paranteze = 0
resultat = 1

for i in range(len(P)):
    print(P[i], end='')

    if P[i] == "(":
        contor_paranteze += 1
    if P[i] == ")":
        contor_paranteze -= 1

for i in range(len(P)-1):

    # (= || (+   ... 
    if P[i] == "(":
        if P[i+1] == "=" or  P[i+1] == ">" or  P[i+1] == "+" or  P[i+1] == "*":
            resultat = 0
            break

    
    # ~
    if P[i] == "~":
        if P[i+1].isalpha() == True or P[i+1] == "(":
            resultat = 1
        else:
            resultat = 0
            break



    # B( || )B
    if P[i].isalpha() == True and P[i+1] == "(":
        resultat = 0
        break
 
    if P[i] == ")" and P[i+1].isalpha() == True:
        resultat = 0
        break

   

  
        





print()
print(contor_paranteze, end='\n')
if contor_paranteze != 0 or resultat == 0:
    print("Sirul NU este formula bine formata")         # afisare rezultat
else:
    print( "Sirul ESTE formula bine formata" )