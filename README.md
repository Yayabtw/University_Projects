# University_Projects
🇫🇷 Ceci est mon répertoire qui contient tous les projets que j'ai pu réaliser durant mon parcours académique.     
🇬🇧 🇺🇸 This is my repository which contains all the projects that I worked on during my IT scholarship. 

# Création de base de données / Database creation 
🇫🇷  Projet concernant la création d'une base de données pour un site de vidéos en ligne (YouTube est l'exemple pris durant ce projet) :
     ● Conception de la base de données :
        ○ Listage des différents attributs nécessaires dans notre base de données
        ○ Établissement des différentes relations entre les différentes tables
     ● Création de la base de données en SQL (Oracle SQL Developer)

🇬🇧 🇺🇸 Project which consists in doing a database for a website like YouTube :
     ● Database conception 
        ○ Listing of all the attributes that were necessary for our DB 
        ○ Schema of all the relations between the tables
     ● DB creation thanks to Oracle SQL Developer
    
# Projet "Hunt" / "Hunt" Project --> Décembre 2021 / December 2021
🇫🇷 Projet de simulation proies/prédateurs : Python grâce à Tkiteasy (une version simplifiée de Tkinter pour l'interface graphique)
     ● Principe du projet : 
       ○ Les proies doivent survivre dans un terrain quadrillé tout en sachant que les prédateurs veulent les manger pour survivre
       ○ Les proies meurent au bout d'un certain nombre de tours --> nombre initialisé dans une variable globale
       ○ Les prédateurs ont un niveau d'énergie qu'ils doivent empêcher de passer à 0 en mangeant les proies
     ● Création du terrain :
       ○ Création du quadrillage servant de terrain (les numéros de cases sont utilisés pour les coordonnées
       ○ Création d'une "clôture" pour éviter que les proies et les prédateurs ne sortent du terrain 
     ● Création des proies :
        ○ Etablissement de dictionnaires pour stocker les objets graphiques, l'âge et les coordonnées des proies (symbolisés par un cercle vert)
        ○ Création des proies (cercle de couleur vert)
     ● Création des prédateurs : partie pas encore effectuée par manque de temps durant le projet académique
     ● Déplacement :
       ○ Mise à jour des dictionnaires à chaque déplacement pour que le déplacement se fasse en mémoire

🇬🇧 🇺🇸 Prey / Predator simulation proies/prédateurs : Done in Python thanks to Tkiteasy (simplified version of Tkinter for the GUI)
     ● Principal concept of this project : 
       ○ Preys have to survive in a squared field knowing that the predators want to eat them so they can survive
       ○ Preys dies after a certain amount of turns --> number initialized in a global variable
       ○ Predators got a certain amount of energy which decreases, if this amount reaches 0, they dies (they have to eat the preys to gain energy)
     ● Field creation :
       ○ Création of the squared field (30x30)
       ○ Creation of a "fence" so the entities don't go out of the field
     ● Prey creation :
        ○ Creation of dictionnaries to stock the graphical objects, the age and the prey coordinates 
        ○ Création of the prey's graphical objects
     ● Création des prédateurs : Didn't have time to do it when we had to give the project to our professors
     ● Entities movement :
       ○ Update of the dictionnaries when the entities move in order that the system understands that they move 
