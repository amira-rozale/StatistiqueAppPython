from strategy import Moyenne, Mediane, EcartType, Correlation, RegressionLineaire

class StrategieFactory:
    @staticmethod
    def creer_strategie(type_strategie):
        mapping = {
            1: Moyenne,
            2: Mediane,
            3: EcartType,
            4: Correlation,
            5: RegressionLineaire
        }
        cls = mapping.get(type_strategie, Moyenne)
        return cls()
