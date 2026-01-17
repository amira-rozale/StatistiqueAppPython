#Bibliothèque d’Analyse Statistique – Python

#Objectifs pédagogiques

Ce projet a pour objectif de concevoir une bibliothèque d’analyse statistique réutilisable en appliquant les principes de la programmation orientée objet et des patrons de conception. Le travail met en pratique le patron Stratégie pour le choix dynamique des méthodes statistiques et le patron Singleton pour la gestion centralisée du journal des calculs. Une attention particulière est portée à la modularité et à la robustesse du code.

#Démarche et évolution du projet

Le projet a débuté par une version simple permettant de charger des données numériques depuis un fichier CSV et d’appliquer une seule méthode statistique. Cette première approche était fonctionnelle mais rigide, car le changement de méthode nécessitait une modification directe du code et aucun historique des calculs n’était conservé.

Afin d’améliorer la flexibilité, le patron de conception Stratégie a été introduit. Une interface commune définit une méthode de calcul, et chaque méthode statistique est implémentée dans une classe indépendante. Cette approche permet de changer dynamiquement la méthode utilisée sans modifier le client et facilite l’ajout de nouvelles stratégies.

Un journal des calculs a ensuite été ajouté en utilisant le patron Singleton. Ce choix garantit l’existence d’une seule instance du journal dans toute l’application et permet d’enregistrer de manière cohérente chaque calcul effectué, avec la date, la méthode utilisée et le résultat obtenu.

#Gestion des données et robustesse

Le système prend en compte le fait que certaines méthodes statistiques nécessitent des données à une seule colonne, tandis que d’autres, comme la corrélation et la régression linéaire, nécessitent deux colonnes. Le chargement des données depuis le fichier CSV est donc adapté dynamiquement selon la méthode choisie par l’utilisateur.

Des mécanismes de validation ont été intégrés afin de détecter les erreurs de format ou de contenu dans le fichier CSV. Les erreurs sont gérées proprement et des messages explicites sont affichés, ce qui améliore la robustesse et l’aspect pédagogique du programme.

Afin d’éviter les incohérences entre le format des données et les méthodes statistiques, une étape de normalisation des données est réalisée dans la classe Analyseur. Cette approche garantit que chaque stratégie reçoit exactement le type de données attendu, tout en conservant des stratégies simples et indépendantes.

#Architecture du projet

Le projet est organisé de manière modulaire. Le client gère l’interaction avec l’utilisateur, l’analyseur orchestre l’application des stratégies, les méthodes statistiques sont regroupées dans des classes dédiées, le journal des calculs est isolé dans une classe Singleton, et les fonctions utilitaires s’occupent du chargement et de la validation des données. Cette séparation claire des responsabilités améliore la lisibilité et la maintenabilité du code.

#Fonctionnalités principales

L’application permet de charger des données depuis un fichier CSV, de choisir dynamiquement une méthode statistique, de calculer et afficher le résultat, et de conserver un historique complet des calculs effectués. L’ajout de nouvelles méthodes statistiques est simple et ne nécessite aucune modification du code existant du client.

#Points forts de la solution

Par rapport à des solutions classiques, ce projet se distingue par l’utilisation explicite de plusieurs patrons de conception, une forte modularité et une gestion rigoureuse des erreurs. Le code est conçu pour être réutilisable et extensible, ce qui le rapproche d’une approche professionnelle plutôt que d’un simple exercice .

#Conclusion

Ce projet démontre une application concrète des principes de la programmation orientée objet et des patrons de conception dans le cadre d’une bibliothèque d’analyse statistique. La solution proposée est robuste, évolutive et pédagogique, et constitue une base solide pour des extensions futures telles qu’une interface graphique ou l’ajout de nouvelles méthodes d’analyse.
