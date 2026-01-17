from datetime import datetime

class JournalCalculs:
    _instance = None

    def __new__(cls, fichier="journal.txt"):
        if cls._instance is None:
            cls._instance = super(JournalCalculs, cls).__new__(cls)
            cls._instance.journal = []
            cls._instance.fichier = fichier
            # Charger l’historique
            try:
                with open(fichier, "r") as f:
                    cls._instance.journal = [line.strip() for line in f]
            except FileNotFoundError:
                pass
        return cls._instance

    def enregistrer(self, methode, resultat):
        ligne = f"{datetime.now()} | {methode} = {resultat}"
        self.journal.append(ligne)
        with open(self.fichier, "a") as f:
            f.write(ligne + "\n")

    def afficher_journal(self):
        for ligne in self.journal:
            print(ligne)
