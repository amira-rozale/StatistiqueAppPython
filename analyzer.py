class Analyseur:
    def __init__(self):
        self.methode = None

    def set_methode(self, methode):
        self.methode = methode

    def analyser(self, donnees):
        resultat = self.methode.calculer(donnees)
        from journal import JournalCalculs
        JournalCalculs().enregistrer(self.methode.get_nom(), resultat)
        return resultat
