

import csv

def charger_csv(fichier):
    donnees = []
    with open(fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # ignore empty rows
                donnees.append(float(row[0]))
    return donnees
