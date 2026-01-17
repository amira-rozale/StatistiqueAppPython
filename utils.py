import csv

import csv

def charger_csv(fichier, colonnes=1):
    donnees = []

    with open(fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for ligne_num, row in enumerate(reader, start=1):

            if len(row) < colonnes:
                raise ValueError(
                    f"Ligne {ligne_num} invalide : "
                    f"{colonnes} colonnes requises, {len(row)} trouvée(s)"
                )

            try:
                donnees.append([float(row[i]) for i in range(colonnes)])
            except ValueError:
                raise ValueError(f"Ligne {ligne_num} contient des valeurs non numériques")

    return donnees
