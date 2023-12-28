from tkiteasy import *
from random import *
from math import *

################################
#-Etablissement des variables global-#
TOUR,NB_TOUR, = 0, 10 
ORIGIN, LON, LAR, CARRE, AGE_P,  = 0, 900, 900, 30, 5, 
ENERGY_PRED, MIAM, EREPRO = 10, 5, 15
NB_CASE_X = NB_CASE_Y = 30
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]
pro_age, pro_obj = {}, {}
pred_energy, pred_obj = {}, {}
ligne, colonne = randint (0,NB_CASE_Y - 1),randint (0, NB_CASE_X - 1)
LARG, HAUT = CARRE * NB_CASE_X, CARRE * NB_CASE_Y
################################

#--Réalisation du terrain--#
def terrain():
    for i in range(ORIGIN,LON,CARRE):
        g.dessinerLigne(ORIGIN,i,LON,i,'grey')
        g.dessinerLigne(i,ORIGIN,i,LAR,'grey')
    

#################################

#--Conversion des cases en pixels, appartition aléatoire des proies--#

def convertPixels(ligne, colonne):
    """
    Fonction permettant de convertir les lignes et colonnes des cases en pixels. Ceci, permettant l'apparition aléatoire des proies
    """
    return ligne * CARRE + CARRE / 2, colonne * CARRE + CARRE / 2

################################

#--Fonction gérant les données de la proies--#

def initDataProie (pro_age, pro_obj):
    """
    Fonction qui permet d'initialiser les données pour les proies 
    Entrée : deux dictionnaires pro_age et pro_obj
    Retour : Dictionnaires initialisées à 0 et à None
    """
    for ligne in range(NB_CASE_X):
        for colonne in range(NB_CASE_Y):
            pro_obj[(ligne,colonne)] = None
            pro_age[(ligne,colonne)] = 0

def suppr_case_pro(pro_age, pro_obj,ligne,colonne):
    """
    Fonction permettant de rendre la case libre pour les autres proies une fois qu'une proie a quitté cette même case, en réinitialisant les données concernant cette case
    """
    g.supprimer(pro_obj[(ligne,colonne)])
    pro_age [(ligne, colonne)] = 0
    pro_obj [(ligne,colonne)] = None 

def naissanceProie (pro_age, pro_obj):
    """
    Fonction permettant de gérer l'apparition de nouvelles proies que ce soit en mémoire ou graphiquement
    Entrée : deux dictionnaires pro_age et pro_obj
    Sortie : apparition de nouvelles proies 
    """
    ligne, colonne = randint (0,NB_CASE_Y - 1),randint (0, NB_CASE_X - 1)
    if pro_obj[(ligne,colonne)] is not None:
        return None
    y,x = convertPixels(ligne,colonne)
    proie = g.dessinerDisque(x, y, CARRE/3, 'green')
    pro_age [(ligne, colonne)] = AGE_P
    pro_obj[(ligne, colonne)] = proie
    return proie


def depla_une_Proie(ligne,colonne, pro_age, pro_obj):
    """
    Fonction permettant de déplacer une seule proie 
    Entrée : deux dictionnaires pro_age et pro_obj 
    Retour : mise à jour des deux dictionnaires ainsi que déplacement graphiquement parlant
    """
    direct = randint(0, len(DIRECTIONS)-1)        
    ligne2, colonne2 = ligne + DIRECTIONS[direct][0],  colonne+DIRECTIONS[direct][1]
    if case_est_valide(ligne2, colonne2) is False:    
        return 
    if pro_obj[(ligne2, colonne2)] is not None:    
        return 
    y1, x1 = convertPixels(ligne, colonne)    
    y2, x2 = convertPixels(ligne2, colonne2)
    dx = x2 - x1
    dy = y2 - y1 
    g.deplacer(pro_obj[(ligne,colonne)], dx, dy)
    pro_age[(ligne2, colonne2)] = pro_age[(ligne,colonne)]
    pro_obj[(ligne2, colonne2)] = pro_obj[(ligne,colonne)]
    pro_age[(ligne,colonne)] = 0
    pro_obj [(ligne,colonne)] = None


def deplaProies(pro_age, pro_obj):
    """
    Fonction permettant de vérifier si les cases peuvent être déplacées. Si oui, la fonction permettant de déplacer une seule proie est appelée
    Entrée : deux dictionnaires pro_age et pro_obj
    Sortie : appel de la fonction 
    """
    for ligne in range(NB_CASE_X):
        for colonne in range(NB_CASE_Y):
            if pro_obj[ligne, colonne] is not None:
                depla_une_Proie(ligne,colonne, pro_age, pro_obj)

def case_est_valide(ligne,colonne):
    """
    Permet d'établir une clôture pour nos proies et nos prédateurs afin qu'elles ne sortent pas de l'écran
    Retour : un booléen correspondant soit à True si la case est disponible et False si la case est prise
    """
    if 0 <= ligne < NB_CASE_Y and 0 <= colonne < NB_CASE_X:
        return True
    else:
        return False

def initDataPred (pred_energy, pred_obj):
    """
    Fonction qui permet d'initialiser les données pour les prédateurs
    Entrée : deux dictionnaires pred_energy et pred_obj
    Retour : Dictionnaires initialisées à 0 et à None
    """
    for ligne in range(NB_CASE_X):
        for colonne in range(NB_CASE_Y):
            pred_obj[(ligne,colonne)] = None
            pred_energy[(ligne,colonne)] = 0

def suppr_case_pred(pred_energy, pred_obj,ligne,colonne):
    """
    Fonction permettant de rendre la case libre une fois qu'un prédateur a quitté cette même case, en réinitialisant les données concernant cette case
    """
    g.supprimer(pred_obj[(ligne,colonne)])
    pred_energy [(ligne, colonne)] = 0
    pred_obj [(ligne,colonne)] = None 

def apparitionPredateur (pred_energy, pred_obj):
    """
    Fonction permettant de gérer l'apparition de nouvelles prédateurs que ce soit en mémoire ou graphiquement
    Entrée : deux dictionnaires pred_energy et pred_obj
    Sortie : apparition de nouvelles prédateurs 
    """
    ligne, colonne = randint (0,NB_CASE_Y - 1),randint (0, NB_CASE_X - 1)
    if pred_obj[(ligne,colonne)] is not None:
        return None
    y,x = convertPixels(ligne,colonne)
    pred = g.dessinerDisque(x, y, CARRE/3, 'red')
    pred_energy [(ligne, colonne)] = ENERGY_PRED
    pred_obj[(ligne, colonne)] = pred
    return pred

def boostEnergyPred(pred_obj, ENERGY_PRED):
    """
    Permet d'ajouter de l'energie si un prédateur mange une proie

    Paramètres : un dictionnaire contenant l'objet graphique du prédateur ainsi que l'énergie actuelle du prédateur
    """
    if pred_obj[(ligne, colonne)] == pro_obj[(ligne,colonne)]:
        g.supprimer(pro_obj[(ligne,colonne)])
        ENERGY_PRED += MIAM

def reproPred(EREPRO, ENERGY_PRED):
    """
    Permet l'apparition de nouveaux prédateurs si leur énergie est suffisante 

    Paramètres : EREPRO (énergie pour la reproduction) et ENERGY_PRED (énergie actuelle du prédateur)
    """
    if ENERGY_PRED >= EREPRO:
        apparitionPredateur(pred_energy, pred_obj)

def depla_un_Pred(ligne,colonne, pred_energy, pred_obj):
    """
    Fonction permettant de déplacer un seul prédateur
    Entrée : deux dictionnaires pred_energy et pred_obj 
    Retour : mise à jour des deux dictionnaires ainsi que déplacement graphiquement parlant
    """
    direct = randint(0, len(DIRECTIONS)-1)        
    ligne2, colonne2 = ligne + DIRECTIONS[direct][0],  colonne+DIRECTIONS[direct][1]
    y1, x1 = convertPixels(ligne, colonne)    
    y2, x2 = convertPixels(ligne2, colonne2)
    dx = x2 - x1
    dy = y2 - y1 
    g.deplacer(pred_obj[(ligne,colonne)], dx, dy)
    pred_energy[(ligne2, colonne2)] = pred_energy[(ligne,colonne)]
    pred_obj[(ligne2, colonne2)] = pred_obj[(ligne,colonne)]
    pred_energy[(ligne,colonne)] = 0
    pred_obj [(ligne,colonne)] = None


def deplaPred(pred_energy, pred_obj):
    """
    Fonction permettant de déplacer les prédateurs
    Entrée : deux dictionnaires pred_energy et pred_obj
    Sortie : appel de la fonction déplacement
    """
    for ligne in range(NB_CASE_X):
        for colonne in range(NB_CASE_Y):
                depla_un_Pred(ligne,colonne, pred_energy, pred_obj)

################################

g = ouvrirFenetre(LARG,HAUT)
initDataProie(pro_age, pro_obj)
terrain()
initDataPred (pred_energy, pred_obj)
print(pro_age)
while TOUR < NB_TOUR :  
    print(naissanceProie(pro_age, pro_obj))  
    g.actualiser()
    deplaProies(pro_age, pro_obj)
    deplaPred(pred_energy, pred_obj)
    g.pause(1)
    g.actualiser()
    case_est_valide(ligne,colonne)
    boostEnergyPred(pro_age,ENERGY_PRED)
    apparitionPredateur(pred_energy, pred_obj)
    TOUR += 1
print(pro_age)

while g.recupererClic() is None:
    continue
g.fermerFenetre()

