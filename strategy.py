from abc import ABC, abstractmethod
import statistics
import math

class MethodeStatistique(ABC):
    @abstractmethod
    def calculer(self, donnees):
        pass

    @abstractmethod
    def get_nom(self):
        pass

# Concrete strategies
class Moyenne(MethodeStatistique):
    def calculer(self, donnees):
        return sum(donnees) / len(donnees) if donnees else 0

    def get_nom(self):
        return "Moyenne"

class Mediane(MethodeStatistique):
    def calculer(self, donnees):
        return statistics.median(donnees)

    def get_nom(self):
        return "Médiane"

class EcartType(MethodeStatistique):
    def calculer(self, donnees):
        return statistics.stdev(donnees) if len(donnees) > 1 else 0

    def get_nom(self):
        return "Écart-Type"

class Correlation(MethodeStatistique):
    def calculer(self, donnees):
        # Dummy correlation for example
        return 0.85

    def get_nom(self):
        return "Corrélation"

class RegressionLineaire(MethodeStatistique):
    def calculer(self, donnees):
        # Dummy linear regression example
        return 1.23

    def get_nom(self):
        return "Régression Linéaire"
