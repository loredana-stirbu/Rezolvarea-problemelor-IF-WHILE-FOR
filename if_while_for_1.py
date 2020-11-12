n=int(input("Dati numarul de zile ale unei luni: "))
if n==28 :
     print("Luna februarie, daca anul nu e bisect")
elif n==29 : 
     print("Luna februarie, daca anul e bisect")
elif n==30 :
     print("Lunile: aprilie","iunie","septembrie","noiembrie",sep=", ")
elif n==31 :
     print("Lunile: ianuarie","martie","mai","iulie","august","octombrie","decembrie",sep=", ")      
elif ((n<28)or(n>31)):
    print("Nu sunt luni cu asa numar de zile")  