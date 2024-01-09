import random

numero_de_tour = 0    # l'incrementer quand on fait la premier distribution , then , l'incrimenter dans la fonction tour joueur 
                      # utiliser le mot global dans la fonction pour utiliser ce valeur 

""" cree une fonction pour incrementer cette valeur """
def numTour ():
    global numero_de_tour
    numero_de_tour +=1 
    return ("le numero de tour est: ",numero_de_tour)

################################################# (partie A1) #######################################################################################


def paquet ():
    ### initialisation des cartes du jeu###
    ### retourne le nom de tous les cartes ###
    model = ["pique", "coeur", "trefle", "carreau"]
    carte_vaut_dix = ['valet', 'dame', 'roi']
    cartes= []
 
    for i in model:           
        for j in range(2,11):           # bboucle pour cree les cartes avec les numeros 
            carte = str(j)+' '+ i
            cartes.append(carte)
        
        for j in range (1):             # bboucle pour cree tous les as 
                carte = 'as '+i
                cartes.append(carte)

        for k in carte_vaut_dix :       # boucle pour cree les cartes qui vaut dix 
            carte = k+' '+ i 
            cartes.append(carte)

    return cartes

#print (paquet())



def valeurCarte (carte):
    c = ' '.join(carte)
    
    valeur_carte = 0
    
    if c.startswith(('valet', 'dame', 'roi')):
        valeur_carte = 10

    if c.startswith(('2','3','4','5','6','7','8','9','10')) :
        valeur_carte = int(c[0])

    if c.startswith('as'):  
        while True:
            ## controle de a valeur AS
            demande_User = int (input("vous voulais que votre AS vaut {1} ou {11}"))
            if demande_User == 1 :
                valeur_carte = 1
                break
            elif demande_User == 11:
                valeur_carte = 11
                break
            else : 
                print ("entrer une valeur valable")

    return valeur_carte

#print (valeurCarte('valet'))


def initPioche(n): # n : nbrs de joueurs
    """  fonction pour melanger les carte """
    C_total = paquet()*n
    cartes_melanger = random.sample(C_total , len(C_total))

    return cartes_melanger


#print(initPioche(2))


def piocheCarte (p , X =1 ):  
    """ fonction qui prend en paramettres tous les cartes du jeux melanger et tire la derniere carte
        en modifier la liste de tout les carte en supprimant la carte piocher 
        p : liste de tous les cartes melanges    (var cartes_jeu)
        X :le nbr des cartes a piocher 
    """                 
    print("cartes restant par les quelles on peutt piocher ",len(p))                                                         #"""puisse passer une fonction comme paramettre pour avoir ce qu elle retourne en paramettre""" 
    carte_piocher = []
    for i in range (X):
        #k = len(p ) - 1     # le dernier index de la liste des cartes
        piocher = p[-1]
        carte_piocher.append(piocher)
        p.pop(len(p)-1)

    #print (len(p))
    return carte_piocher

"""
print('*'*100)
a = initPioche(2)
print(piocheCarte(a))
print('*'*100)
"""
################################################# (partie A2) #######################################################################################

def intiJoueur (n):
    """ n : est le nbrs de joueurs
        demande a chaque joueurs son noms 
        retourne une liste avec les noms de tous les joueurs"""
    num = 1
    liste_noms = []
    for i in range (n):
        nom = input(f"entrer le nom du joueur {num} : \n") 
        num += 1 
        liste_noms.append(nom)

    return liste_noms

#############  Vars necessaire pour le teste de fonctionnement du programme #############   
nbr_joueurs = int(input("entrer le nombre de joueurs \n"))
cartes_Jeu = initPioche(nbr_joueurs)
joueurs = intiJoueur(nbr_joueurs)

# ************************************************************************************* #

def initScores(joueurs, v = 0): # joueurs :  la liste des joueurs
    """ fonction cree le dic qui contient les noms de joueurs avec le score initialiser a '0' 
        joueurs = liste de tous les joueurs renvoyer par initJoueur"""

    joueurs_scores = {}
    for i in joueurs:
        joueurs_scores [i] = v

    return joueurs_scores

#############################
scores = initScores(joueurs)     # variable global qui sera modifier a chaque pioche 
#############################

def premierTour (joueurs , cartes_Jeu , scores):
    """ donne a chaque joueurs les deux cartes de depart et calcule les scores
        renvoie le dic avec les nouveaux scorex du premier tour """

    print(numTour())  # incrementer le num de la tour et l'afficher 

    """ c'est a voir pour que apres le joueur decidra s'il va miser ou va sortir du jeu """
    #caf = {}   # les cartes recus pour chaque joueur lors du premier tour
    
    for i in joueurs :
        carte_piocher = piocheCarte(cartes_Jeu , 2) # picher deux carte de tous les cartes_restant   (par le haut) # cartes_Jeu!!!

        score_carte_piocher = 0 
        for j in carte_piocher :     #print(j) : pour verifier les cartes piocher 
            score_carte_piocher += valeurCarte(j)
            #caf[i] = j
            
        scores [i] = score_carte_piocher   # refrechir les scores de chaque joueur apres la distribution des cartes 
    
    return scores 

def gagnant (scores):  
    """ fonction qui retourn le nom du gagnant apres compareson du plus haut score
        scores : parametre = le dictionnaire retourner apres chaque tours avec les scores """

    list_score = list(scores.items())  # => renvoie une liste de tuples (joueurs , score) voir exemple ci dessous
    print (list_score)
    gagnant = list_score[0][0]
    score_gagnant = list_score[0][1]
    for i in range(1 , len(list_score)) :
        if list_score[i][1] > score_gagnant :    # faire la comparaison par le score
            score_gagnant = list_score[i][1]
            gagnant = list_score[i][0]

            # retourner le tuple qui conttient le nom et le score du joueur gagnant

    print(f"le gagnat est: <{gagnant}> avec un score de <{score_gagnant}>")
    return gagnant



################################################# (partie B1 - Tour d'un joueur) #######################################################################################

def continu ():
    rejouer = ['oui','yes']
    stop = ['non','no']
    rep = input("vous voulais rejouez si oui tapez (oui) or (yes) sinon tapez (non)or(no)") 
    while (rep not in rejouer) or (rep not in stop) :
        if rep in rejouer :
            return True
        elif rep in stop :
            return False
        else :
            print("reponse invaide (oui/yes , no/non)")
            rep = input("vous voulais rejouez si oui tapez (oui) or (yes) sinon tapez (non)or(no)")


def Tourjoueur(j , scores , joueurs , cartes_Jeu):  # le nom d'un joueur
    """ fonction qui retourne le nbr de tour fait et demande a l'utilisateur s'il veut piocher une feuille 
        s'il repond par oui il pioche une feuille et reinitialise les scores (voir s'il est gagnant ou perdant)
        , sinon (il repond non) : il perd et il sort du jeu
        j : parametre :  le joueur qui a son tour
    """

    print(numTour())  # incrementer le num de la tour et l'afficher 
    print(f"c'est le tour de: {joueurs[joueurs.index(j)]} votre score et de {scores[j]}")

    continuer = continu()
    if continuer == True :
        nv_carte = piocheCarte(cartes_Jeu)
        
        val_nv_carte = valeurCarte(nv_carte)
        scores [j] += val_nv_carte    # calcule  le nv score du jour apres voirr s'il > 21  on affiche t'as perdu et on la retir de la liste
                                             
        if scores[j] > 21 :
            print(f" {j} vous avec perdu , votre score depasse les 21 points" , "votre score il est de : {score[j]}")  #  pourquoi il m'affiche le score du tour 1 meme apres que je tape oui pour rejouer et que je pioche une carte
            del joueurs[joueurs.index(j)]
            del scores[j]
            
        else :
            print (f" {j} votre nouveau score apres avoir piocher une carte est de",scores[j])

    else :                         # si le joueur ne veux plus jouer on le retir de la liste 
        print(joueurs[joueurs.index(j)] , "vous voulez arretez, avez perdu , vous sorter du jeu")
        del joueurs[joueurs.index(j)]
        del scores[j]
        
    return scores     # apres que j'ai supprimer le joueurs de la liste de joueurs dois je ref le dic des joueurs-scores aussi en meme temps             


################################################# (partie B2 - Une partie complete) #######################################################################################

# le paramettre joeurs sera  la liste des joeurs qui sont encore en jeu  (il sera le dic aveec les score )
def tourComplet(joueurs , scores , cartes_Jeu):  
    """ fonction qui donne un tour de jeu a chacun des joueurs encore en jeu dans la partie courante.
        joueurs : paramettres == la liste des joeurs qu'ils sont encorre en jeu 
        *modifie la liste des joueurs si ca necessite (evidament la liste des scores  """


    for j in joueurs :
        print (f"################ tour joueurr {j} ##############")
        Tourjoueur(j, scores, joueurs, cartes_Jeu)
        

    return scores      #=> retourne le dictionnaire des joueurs restant a la fin du tour avec leurs scores

def partieFinie(scores,joueurs):    # si la liste ou le dic des joueurs il en reste qu'un alors en affiche le vincqueur 

    """ prend en parametre la liste des scores si cette dernier contient qu'un seul joeur
        alors la partie et fini et renvoie le vainqueur avec son score 
        renvoie une resultat bool vrai ou faux si la partie est finie ou pas"""
    
    if len(scores) == 1:      # si dans la liste de score il reste qu'un joueur alors ce dernier joueur et le gagnant 
        return True
    
    # boucle pour verifier si un joueurs a un score de 21 donc on finie la partie et ce joueur gagne
    else :    
        for j in joueurs :
            if scores[j] == 21:
                print(f"{j} votre score est de 21 vous avez gagner")
                return True
            return False

################################################# (partie B4 - les mises ) #######################################################################################

def kopecs_depart(joueurs):
    """ fonction initialise le nbr de jetons de chaque joueurs 
        return un dic  joueur : 100 jetons"""
    
    kopecs = {}
    for j in joueurs :
        kopecs [j] = 100

    return kopecs

###################   init kopecs     ####################
kopecs = kopecs_depart(joueurs)
print("kopecs de depart ", kopecs)
les_mise_desJooeurs = {}
##########################################################

def miser ( j, kopecs ): #le joueur qui va mise
    """ fonction de mande au joueur le montant qu'il va miser
        apres qu'il mise le montant sera retirer de son argent """

    print(f"{j} est ce que vous allez miser \n")
    decision_mise = input('(oui,yes) // (non,no) \n')sq
    
    if decision_mise == 'yes' or decision_mise == 'oui':
        mise = int(input ("combien vous voulez misez ?"))
        
        while mise <= 0  or mise > kopecs [j]:
            if mise <= 0 :
                print (" entrer une valeur positive ")
                mise = int(input ("combien vous voulez misez ?"))
            elif mise > kopecs [j] :
                print("vous misez avec une somme superieur a votre argent ")
                mise = int(input ("combien vous voulez misez ?"))
            else :
                print(" je comprend pas votre decision")   # si le joueur entre des chaine de caracteres
                mise = int(input ("combien vous voulez misez ?"))
        les_mise_desJooeurs[j] = mise        
        a = kopecs[j]
        kopecs[j] = a-mise     # retirer la mise de l'argent du joueur
        
    else :             
        print(f"{j} vous voulez pas miser vous etes eleminer du jeu")
        # supprimer le joueur de (la liste des joueurs , scores , ) {on le laisse dans kopecs pour les prochain tour }
        del joueurs[joueurs.index(j)]
        del scores [j]
        
                          
            
             
    print("la mise de chaque joueur est: ",les_mise_desJooeurs )   
    return les_mise_desJooeurs 

########################################################################################################################""







#  Option: proposer aux joueurs de quitter la table entre les parties (donc partir avec les kopecs gagnes jusque la).








########################################################################################################################"" 

def victoire(joueurs):
    """ fonction initialise le nbr de victoire de chaque joueur
        retourn   joueur : 0  """
        
    victoires = {}
    for j in joueurs :
        victoires[j] = 0
        
    return victoires 

######  init dic victoires ######
victoires = victoire(joueurs)
#################################





def verifier_acces(joueurs , kopecs):
    """ fonction verifie si le joueurs a encore de l'argent pour rejouer le prochain tour ou pas
        s'il n'a plus de soux il est eliminer  """

    for j in joueurs :
        if kopecs[j] == 0 :
            print(f" {j} vous avez plus de d'argent a miser vous pouvez plus jouer")
            del scores[j]
            del joueurs[joueurs.index(j)]
    print("les joueurs qui sont encore en jeu sont: ", joueurs)
    
    

########################################    CROUPIER     ################################################## 

def ajout_croupier (joueurs,scores,kopecs,victoires):
    c = 'croupier'
    joueurs.append(c) 
    scores[c] = 0
    kopecs [c] = 0
    victoires[c]=0
    kopecs[c]=100

    return joueurs , scores , kopecs
#ca marche

#pour la partie graphique mettre une boutton pour (amis/croupier) et amis croupier 





def incrementer_score_croupier(scores , cartes_Jeu):
    carte_piocher = piocheCarte(cartes_Jeu)  # fonc piocher une carte
    print(carte_piocher)
    scores['croupier'] += valeurCarte(carte_piocher) # incrementer le score du croupier
    
    return scores

##################          methodes de pioches         ######################## 

# croupier niveau 1
def piocher_hasard_croupier (scores , cartes_Jeu):
    """ difficulte normal le  croupier prend le risque a 50%  
        il y a la possibilite de 50% qu'il pioche et 50% qu'il s'arrete"""
        
    pioche = random.randint(0,1)
    if pioche == 1 :
        incrementer_score_croupier(scores, cartes_Jeu)
        
    """ else : il faut supprimer le croupier retirer du jeu il perd comme les joueurs
        s'ils piochent pas ils perdent """
    
    return scores 
#ca marche comme ca    


# pour suivre le principe de la fonction continue mais puisque on va pas demande ou croupier 
# mais c'est  la prob qui va decider donc  ==>  il faut que cette fonc renvoie True s'il pioche
# return  False s'il pioche pas 
# comment il faut le mettre dans le code pricipale avec les joueurs pour quand il perd il sort 
# il gagner on arrete le jeu et il prends tous les kopecs




# croupier niveau 2 
def piocher_carte_niveau_normal(scores, cartes_Jeu):
    """ le croupier calcle le risque et prend la decision en se basant sur ca """

    if scores['croupier'] < 10 : 
        incrementer_score_croupier(scores, cartes_Jeu)

        return scores    
        
    else : 
        piocher_hasard_croupier(scores)
    
        return scores
#ca marche


# croupier niveau 3
def piocher_carte_niveau_difficile(scores , cartes_Jeu):
    """ le croupier calcle le risque et prend la decision en se basant sur ca """

    a = random.randint(1,10)
# les cas pour les quels on va varier la probabilite de pioche avec le module random
    if scores['croupier'] <= 11 :
        incrementer_score_croupier(scores, cartes_Jeu)   # probabilite de 90% qu'il pioche
   
    if scores['croupier'] == 12 :
        if a >2 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 13 :
        if a >3 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 14 :
        if a >4 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 15 :
        if a >5 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 16 :
        if a >6 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 17 :
        if a >7 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 18 :
        if a >8 :
            incrementer_score_croupier(scores, cartes_Jeu)
    if scores['croupier'] == 19 :
        if a> 9 :
            incrementer_score_croupier(scores, cartes_Jeu)

    if  scores['croupier'] == 20 :
        if a> 9 :
            incrementer_score_croupier(scores, cartes_Jeu)

    return scores

# il faut faire else pour chaque cas afin de supprimer le croupier s'il pioche pas y a t il une autre methode pour simplifier ??


# il faut faire la verification si le score du croupier depasse 21 affiche un msg d'erreur    
#  ==>  faire une fonction complet tour croupier 
    



########################            methodes de mise croupier               ########################

les_mise_desJooeurs = {}
    
def mise_croupier_normal (kopecs):
    """ miser une pourentage de la somme restant"""
    
    pourcentage_de_mise = int(input(" entre la pourcentage de la mise \n"))
    somme_restant = kopecs['croupier']
    les_mise_desJooeurs['croupier'] = somme_restant * (pourcentage_de_mise/100)    

    kopecs['croupier'] = somme_restant - (somme_restant * (pourcentage_de_mise/100)  )    # retirer la mise de l'argent du croupier
    
    return kopecs
#ca marche

    

def mise_croupier_risque (kopecs):
    """ miser selon les risque"""
    
    kopecs_restant = kopecs['croupier']
    
    prob = random.randint(1,3)
    if prob == 1:
        les_mise_desJooeurs['croupier'] = kopecs_restant
        kopecs['croupier'] = 0
        
    if prob == 2: 
        les_mise_desJooeurs['croupier'] = kopecs_restant * 0.5
        kopecs['croupier'] -= (kopecs_restant * 0.5 ) 
    
    if prob == 3:
        les_mise_desJooeurs['croupier'] = kopecs_restant * 0.1
        kopecs['croupier'] -= (kopecs_restant * 0.1 )
    
    return kopecs
#ca marche     



def mise_croupier_2Premiers_Cartes(scores , kopecs):
    """ miser selon son score et la prob de gagner"""
    
    score_croupier = scores['croupier']
    if score_croupier <= 11 :
        les_mise_desJooeurs['croupier'] = kopecs['croupier']
        kopecs['croupier'] = 0
    
    if score_croupier in [12,13]:
        les_mise_desJooeurs['croupier'] = kopecs['croupier'] * 0.8
        kopecs['croupier'] -= kopecs['croupier'] * 0.8
    
    if score_croupier in [14,15]:
        les_mise_desJooeurs['croupier'] = kopecs['croupier'] * 0.6
        kopecs['croupier'] -= kopecs['croupier'] * 0.6
        
    if score_croupier in [16,17]:
        les_mise_desJooeurs['croupier'] = kopecs['croupier'] * 0.4
        kopecs['croupier'] -= kopecs['croupier'] * 0.4
        
    if score_croupier in [18,19]:
        les_mise_desJooeurs['croupier'] = kopecs['croupier'] * 0.2
        kopecs['croupier'] -= kopecs['croupier'] * 0.2
    
    if score_croupier == 20:
        les_mise_desJooeurs['croupier'] = kopecs['croupier'] * 0.1
        kopecs['croupier'] -= kopecs['croupier'] * 0.1
    
    return kopecs
#ca marche    
    
    
    












def mise_croupier (methode_mise_croupier):
    """ miser pour le croupier par rapport a la methode choisie"""
    
    if methode_mise_croupier == 'normal':
        mise_croupier_normal(kopecs)
    if methode_mise_croupier == 'risquer' : 
        mise_croupier_risque(kopecs)
    if methode_mise_croupier == 'cartes' :
        mise_croupier_2Premiers_Cartes (scores, kopecs)


def jeu_croupier (methode_jeu_croupier):
    # a son tour le croupier doit piocher une carte par rapport a la methode choisie 
    pass


def PartieComplet(victoires , scores , joueurs , cartes_Jeu):   #victoires le dic de nbr de vic de chaque joueurs
    """ comment puisse utiliser une valeur renvoie d'une fonction quand cette dernier renvoie plusieurs"""
    
    croupier = input("voulez jouez avec le croupier (oui / non)")
    if croupier == 'non' :
        
        # verifier l'accees des joueurs (s'ils ont des kopecs a miser ou pas)
        verifier_acces(joueurs, kopecs) 
        
        print ("le score de chaque jour apres le premier tour est :" ,premierTour(joueurs , cartes_Jeu ,scores))


        # faire une boucle pour tous les joueurs pour demander leurs mises   (on peut cree une fonction)
        for j in joueurs :
            les_mises_des_joueurs = miser(j,kopecs)
            
            
                            
    

     
        while not partieFinie(scores,joueurs) :
            tourComplet(joueurs , scores , cartes_Jeu)
    
        vainqueur = gagnant(scores)  # le nom du vainqueur retourner par la fonction gagnant
        
        victoires[vainqueur] += 1   # incrementer le nbr de victoire pour le vainqueur par 1
    
        return (victoires)       #on peut ajouter son score
    
    
    #  avec  croupier 
    else : 
        ajout_croupier(joueurs, scores, kopecs, victoires)
        methode_jeu_croupier = input("quelle methode voulez que le croupier utilise : la methode piocher_hasard_croupier : taper hazard , methode piocher_carte_niveau_normal: taper normal , piocher_carte_niveau_difficile : tapez difficile")
        methode_mise_croupier = input("quelle methode de mise le croupier utilisera : la methode mise_croupier_normal : taper normal , methode mise_croupier_risque : taper risquer , methode mise_croupier_2Premiers_Cartes : tapez cartes ")

        verifier_acces(joueurs, kopecs)
        
        print ("le score de chaque jour apres le premier tour est :" ,premierTour(joueurs , cartes_Jeu ,scores))
        
        for j in joueurs:
            # faire une condition si le joueur c'est le croupier donc il faut faire appelle au fontion qui pioche et qui mise 
            if j == 'croupier' :
                mise_croupier(methode_mise_croupier)
            else :
                les_mises_des_joueurs = miser(j,kopecs)


        """
        while not partieFinie(scores,joueurs) :
            tourComplet(joueurs , scores , cartes_Jeu)
    
        vainqueur = gagnant(scores)  # le nom du vainqueur retourner par la fonction gagnant
        
        victoires[vainqueur] += 1   # incrementer le nbr de victoire pour le vainqueur par 1
    
        return (victoires)       #on peut ajouter son score        
        """

# commme faire la fonction de mise du croupier dans la boucle de mise des joueurs 
# comme dans la partie du tour complet elle fait appelle au tour joueur et celle ci utilise la fonction continue pour la pioche ??
# je fait une autre fonction au liu de celle ci Tourjour_avec_croupier dans la quelle j'ajoute les condition en prennant en compte le croupier 
        
                


print(PartieComplet(victoires, scores, joueurs, cartes_Jeu))




""" parfois un joueurs commence par un score de 0   ( je fais pas appelle a premiere partie  ?? PQ
    affichage de score quand le joueur perd ne s'affiche pas 
    
    * pour quoi quand je fais une partie complet ca me fait piocher deux fois la premier partie qui fait piocher deux cartes pour chaque joueurs
    
    ==> sinon le programme marche nickel"""
    









##############################          QUESTIONS               ##############################
 
"""comment puisse utiliser une valeur renvoie d'une fonction quand cette dernier renvoie plusieurs"""
# => partiecomplet



###############################################################################################