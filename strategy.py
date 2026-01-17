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
    # Suppose CSV avec 2 colonnes
    def calculer(self, donnees):
        if not donnees or len(donnees[0]) < 2:
            return 0
        x = [row[0] for row in donnees]
        y = [row[1] for row in donnees]
        n = len(x)
        mean_x = sum(x)/n
        mean_y = sum(y)/n
        cov = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n)) / (n-1)
        stdev_x = statistics.stdev(x)
        stdev_y = statistics.stdev(y)
        return cov / (stdev_x*stdev_y) if stdev_x*stdev_y != 0 else 0

    def get_nom(self):
        return "Corrélation"

class RegressionLineaire(MethodeStatistique):
    # Simple regression y = a*x + b sur 2 colonnes
    def calculer(self, donnees):
        if not donnees or not isinstance(donnees[0], list):
              raise ValueError("La régression linéaire nécessite des données à 2 colonnes")

        x = [row[0] for row in donnees]
        y = [row[1] for row in donnees]
        n = len(x)
        mean_x = sum(x)/n
        mean_y = sum(y)/n
        cov = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
        var = sum((x[i]-mean_x)**2 for i in range(n))
        a = cov / var if var != 0 else 0
        b = mean_y - a*mean_x
        return (a, b)  # retourne les coefficients

    def get_nom(self):
        return "Régression Linéaire"
