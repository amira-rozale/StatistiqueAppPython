from analyzer import Analyseur
from utils import charger_csv
from journal import JournalCalculs
from strategie_factory import StrategieFactory


def main():
    analyseur = Analyseur()
    journal = JournalCalculs()  # Singleton

    while True:
        print("\nChoisissez une méthode statistique (0 pour quitter) :")
        print("1 - Moyenne")
        print("2 - Médiane")
        print("3 - Écart-Type")
        print("4 - Corrélation (2 colonnes)")
        print("5 - Régression Linéaire (2 colonnes)")

        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print(" Veuillez entrer un nombre valide.")
            continue

        if choix == 0:
            print("Fin du programme.")
            break

        # Détermination du nombre de colonnes requis
        colonnes = 2 if choix in [4, 5] else 1

        try:
            donnees = charger_csv("data.csv", colonnes=colonnes)
        except ValueError as e:
            print(f" Erreur dans le fichier CSV : {e}")
            continue

        methode = StrategieFactory.creer_strategie(choix)

        if methode is None:
            print(" Choix invalide.")
            continue

        analyseur.set_methode(methode)

        try:
            resultat = analyseur.analyser(donnees)
        except Exception as e:
            print(f" Erreur lors du calcul : {e}")
            continue

        print(f" Résultat ({methode.get_nom()}) : {resultat}")

    # Affichage du journal à la fin
    print("\n Journal des calculs effectués :")
    journal.afficher_journal()


if __name__ == "__main__":
    main()
