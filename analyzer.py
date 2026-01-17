class Analyseur:
    def __init__(self):
        self.methode = None

    def set_methode(self, methode):
        self.methode = methode

    def analyser(self, donnees):
        if self.methode is None:
            raise ValueError("Aucune méthode statistique définie")

        # 🔧 NORMALISATION DES DONNÉES
        # Si données à 1 colonne : [[10], [20]] → [10, 20]
        if isinstance(donnees[0], list) and len(donnees[0]) == 1:
            donnees = [x[0] for x in donnees]

        resultat = self.methode.calculer(donnees)
        return resultat
