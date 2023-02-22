import csv

with open ('baby100.csv', 'r') as f :
    next(f)
    csv_eyes = csv.reader(f)
    baby_names = list(map(tuple, csv_eyes))


def give_names(yorno =True): 
    while (yorno == True):
        names_listed = []
        rank_query = input("rank:  ")
        sex_query = input("\nsex (M or F):  ")

        for i in range(len(baby_names)):
            if (int(rank_query) == int(baby_names[i][5]) and sex_query == (baby_names[i][2])):
                    if baby_names[i][1:3] not in names_listed:
                        names_listed.append(baby_names[i][1:3])

        print(names_listed)          

    
        continu = input("more? (y or n) ")    
        if continu == 'n' :
            yorno = False  
            return yorno


give_names()