from strategy import Moyenne, Mediane, EcartType, Correlation, RegressionLineaire
from analyzer import Analyseur
from utils import charger_csv
from journal import JournalCalculs

def main():
    donnees = charger_csv("data.csv")
    analyseur = Analyseur()

    strategies = {
        1: Moyenne(),
        2: Mediane(),
        3: EcartType(),
        4: Correlation(),
        5: RegressionLineaire()
    }

    while True:
        print("\nChoisissez une méthode statistique (0 pour quitter) :")
        for k, v in strategies.items():
            print(f"{k} - {v.get_nom()}")
        choix = int(input("Votre choix : "))
        if choix == 0:
            break
        if choix not in strategies:
            print("Choix invalide !")
            continue

        methode = strategies[choix]
        analyseur.set_methode(methode)
        resultat = analyseur.analyser(donnees)
        print(f"Résultat : {resultat}")

    print("\n Journal des calculs (historique complet) :")
    JournalCalculs().afficher_journal()


if __name__ == "__main__":
    main()
