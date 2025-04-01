"""
Programme du tron
Raimbault Romain
"""
import pygame
from random import *

#constantes de la fenêtre d'affichage
LARGEUR=512       #hauteur de la fenêtre
HAUTEUR=576       #largeur de la fenêtre
ZONEDEPART=100    #taille de la zone de départ recoloriée en noir
ROUGE=(255,0,0)     # définition de couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
BLANC=(255,255,255)
JAUNE=(255,255,0)
NOIR=(0,0,0)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenêtre
accueilTitre = pygame.font.Font('data/TRON.ttf', 64)     #choix de la police de caractères
jeu = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
titres = pygame.font.Font('freesansbold.ttf', 128)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
tempsPartie=0

#Variables de la moto verte
motoVertX=LARGEUR//4
motoVertY=HAUTEUR//2
directionVert = 'haut'
couleurMotoVert=VERT
scoreVert=0
motoVert=[motoVertX,motoVertY,directionVert,couleurMotoVert,scoreVert]

#Variables de la moto blanche
motoBlancX=LARGEUR//4+(2*(LARGEUR//4))
motoBlancY=HAUTEUR//2
couleurMotoBlanc=BLANC
directionBlanc = 'bas'
scoreBlanc=0
motoBlanc=[motoBlancX,motoBlancY,directionBlanc,couleurMotoBlanc,scoreBlanc]

#Variables autres
scores=[]


def dessineAccueil():
    """
    dessine l'accueil
    """
    TRON = accueilTitre.render('Tron', True,BLANC)
    fenetre.blit(TRON, ((LARGEUR/2)-((TRON.get_rect().width)/2),(HAUTEUR)/6))
    Lancer = jeu.render('ESPACE : Lancer une partie', True,BLANC)
    fenetre.blit(Lancer, ((LARGEUR/2)-((Lancer.get_rect().width)/2),((HAUTEUR)/2)-32))
    listeScores = jeu.render('TAB : Scores', True,BLANC)
    fenetre.blit(listeScores, ((LARGEUR/2)-((listeScores.get_rect().width)/2),(HAUTEUR)/2))
    pygame.display.update() #mets à jour la fenêtre graphique
    print("ACTUALISE")

def dessineDecor():
    global scoreBlanc,scoreVert
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1+32, LARGEUR-1, (HAUTEUR-64)-1],1)                            #bordure rouge
    for i in range(15):                                                                                 #boucle pour créer 30 obstacles (15 ronds, 15 carrés)
        pygame.draw.circle(fenetre, JAUNE, (randint(10,(LARGEUR-10)),randint(42,(HAUTEUR-74))), 10)      #cercle plein de rayon 10 à des coordonnées aléatoires
        pygame.draw.rect(fenetre, JAUNE, [randint(10,(LARGEUR-10)),randint(42,(HAUTEUR-74)), 10, 10],0)  #rectangle plein à des coordonnées aléatoires
    pygame.draw.rect(fenetre, NOIR, [(HAUTEUR//4)-(ZONEDEPART//2),(HAUTEUR//2)-(ZONEDEPART//2), ZONEDEPART, ZONEDEPART],0)  #rectangle plein noir aux points de départ
    pygame.draw.rect(fenetre, NOIR, [(LARGEUR//4+(2*(LARGEUR//4)))-(ZONEDEPART//2),(HAUTEUR//2)-(ZONEDEPART//2), ZONEDEPART, ZONEDEPART],0)  #rectangle plein noir aux points de départ

    #partie de l'affichage du score
    scoreVertTemp=str(scoreVert)
    scoreVertAffichage = jeu.render(scoreVertTemp, True,VERT)
    fenetre.blit(scoreVertAffichage, (((LARGEUR/2)-10)-((scoreVertAffichage.get_rect().width)/2),16-((scoreVertAffichage.get_rect().height)/2)))
    scoreBlancTemp=str(scoreBlanc)
    scoreBlancAffichage = jeu.render(scoreBlancTemp, True,BLANC)
    fenetre.blit(scoreBlancAffichage, (((LARGEUR/2)+10)-((scoreBlancAffichage.get_rect().width)/2),16-((scoreBlancAffichage.get_rect().height)/2)))



def dessineScoreTitre():
    """
    dessine le score
    """
    scoreVertTemp=str(scoreVert)
    scoreVertAffichage = titres.render(scoreVertTemp, True,VERT)
    fenetre.blit(scoreVertAffichage, (((LARGEUR/2)-80)-((scoreVertAffichage.get_rect().width)/2),(HAUTEUR//6)))
    scoreBlancTemp=str(scoreBlanc)
    scoreBlancAffichage = titres.render(scoreBlancTemp, True,BLANC)
    fenetre.blit(scoreBlancAffichage, (((LARGEUR/2)+80)-((scoreBlancAffichage.get_rect().width)/2),(HAUTEUR//6)))


def dessineFin(gagnant):
    """
    dessine l'écran de victoire
    """
    dessineScoreTitre()
    couronne = pygame.image.load('data/couronne.png')
    if gagnant=='vert':
        fenetre.blit(couronne, (((LARGEUR/2)-80)-((couronne.get_rect().width)/2),((HAUTEUR//6)-55)))
    else:
        fenetre.blit(couronne, (((LARGEUR/2)+80)-((couronne.get_rect().width)/2),((HAUTEUR//6)-55)))

    affichageGagnantPartie= 'Le joueur ' + gagnant + ' remporte la victoire !'   #variable permettant de créer le message de victoire de partie
    affichageScorePartie = 'Le score de la partie s\'élève à '+ str(tempsPartie) + ' !'
    gagnantPartie = jeu.render(affichageGagnantPartie, True,BLANC)
    scorePartie = jeu.render(affichageScorePartie, True,BLANC)
    fenetre.blit(gagnantPartie, ((LARGEUR/2)-((gagnantPartie.get_rect().width)/2),(HAUTEUR/2)))
    fenetre.blit(scorePartie, ((LARGEUR/2)-((scorePartie.get_rect().width)/2),((HAUTEUR/2)+20)))

    enregistrementScore = jeu.render('ESPACE : enregistrer le score et retourner à l\'accueil', True,BLANC)
    fenetre.blit(enregistrementScore, ((LARGEUR/2)-((enregistrementScore.get_rect().width)/2),((HAUTEUR/2)+60)))
    pygame.display.update() #mets à jour la fenêtre graphique

def dessineTableauScore():
    for i in range(len(scores)):
        temp=("{0:3}  {1:3}   {2:010d}".format((i+1),scores[i][0],scores[i][1]))
        listeScoreTemp = jeu.render(temp, True,BLANC)
        fenetre.blit(listeScoreTemp, ((LARGEUR/2)-((listeScoreTemp.get_rect().width)/2),((i+1)*40)))
    pygame.display.update() #mets à jour la fenêtre graphique
    scoreLoop=True
    while scoreLoop==True:                      #while qui permet de mettre en pause la fonction à la fin d'une manche
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #fermeture de la fenêtre (croix rouge)
                scoreLoop = False
            if event.type == pygame.KEYDOWN:    #une touche a été pressée...laquelle ?
                if event.key == pygame.K_ESCAPE: #touche echap pour quitter
                    scoreLoop = False
                    fenetre.fill((0,0,0))   #efface la fenêtre
                    LanceAccueil()


def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision



def deplacementmoto(moto):
    """
    deplace la moto si c'est possible
    """
    global motoVert,motoBlanc

    motoX=moto[0]
    motoY=moto[1]
    direction=moto[2]
    couleur=moto[3]

    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)

    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y

    fenetre.set_at((x, y), couleur)
    if couleur==VERT:
        motoVert=[motoX,motoY,direction,couleur]
    elif couleur==BLANC:
        motoBlanc=[motoX,motoY,direction,couleur]
    #motoUpdate=[motoX,motoY,direction,couleur]
    return touche          #retourne la variable booleenne touche pour savoir si la partie est terminée

def LancePartie():
    global LARGEUR,HAUTEUR,tempsPartie, accueilLoop,motoBlanc,motoVert,scores,scoreBlanc,scoreVert,motoVertX,motoVertY,directionVert,motoBlancX,motoBlancY,directionBlanc
    manches=[]
    troisManchesLoop=True
    compteManches=0
    while troisManchesLoop==True:
        jeuLoop=True
        dessineDecor()
        itteration=0
        gagnant=''
        while jeuLoop==True:
            itteration+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jeuLoop = False            #fermeture de la fenêtre (croix rouge)
                    troisManchesLoop = False
                if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
                    if event.key == pygame.K_ESCAPE: #touche echap pour quitter
                        jeuLoop = False
                        troisManchesLoop = False
                        fenetre.fill((0,0,0))   #efface la fenêtre
                        LanceAccueil()
                    #fenetre.set_at((200, 200), color)

            keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
            if keys[pygame.K_UP] and motoBlanc[2]!='bas':    #est-ce la touche UP et est-ce la direction opposée
                motoBlanc[2] = 'haut'
            elif keys[pygame.K_DOWN] and motoBlanc[2]!='haut':  #est-ce la touche DOWN et est-ce la direction opposée
                motoBlanc[2] = 'bas'
            elif keys[pygame.K_RIGHT] and motoBlanc[2]!='gauche':  #est-ce la touche RIGHT et est-ce la direction opposée
                motoBlanc[2] = 'droite'
            elif keys[pygame.K_LEFT] and motoBlanc[2]!='droite':  #est-ce la touche LEFT et est-ce la direction opposée
                motoBlanc[2] = 'gauche'

            if keys[pygame.K_e] and motoVert[2]!='bas':
                motoVert[2]='haut'
            elif keys[pygame.K_s] and motoVert[2]!='droite':
                motoVert[2]='gauche'
            elif keys[pygame.K_d] and motoVert[2]!='haut':
                motoVert[2]='bas'
            elif keys[pygame.K_f] and motoVert[2]!='gauche':
                motoVert[2]='droite'


            #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici
            if deplacementmoto(motoVert)==True:
                scoreBlanc+=1
                gagnant='Blanc'
                jeuLoop=False
            if deplacementmoto(motoBlanc)==True:
                scoreVert+=1
                gagnant='Vert'
                jeuLoop=False

            frequence.tick(60)
            pygame.display.update() #mets à jour la fenêtre graphique
            tempsPartie+=1


        compteManches+=1
        if compteManches==3:
            troisManchesLoop=False

        fenetre.fill((0,0,0))   #efface la fenêtre
        affichageGagnantManche= 'Le joueur ' + gagnant + ' a gagné cette manche !'   #variable permettant de créer le message de victoire de manche
        gagnantManche = jeu.render(affichageGagnantManche, True,BLANC)
        fenetre.blit(gagnantManche, ((LARGEUR/2)-((gagnantManche.get_rect().width)/2),(HAUTEUR/2)))
        dessineScoreTitre()
        if compteManches==3:
            resultatsPartie = jeu.render("ESPACE : voir les résultats de la partie", True,BLANC)
            fenetre.blit(resultatsPartie, ((LARGEUR/2)-((resultatsPartie.get_rect().width)/2),((HAUTEUR+62)/2)))


        else:
            mancheSuivante = jeu.render("ESPACE : Manche suivante", True,BLANC)
            fenetre.blit(mancheSuivante, ((LARGEUR/2)-((mancheSuivante.get_rect().width)/2),((HAUTEUR+62)/2)))

        pygame.display.update() #mets à jour la fenêtre graphique


        pauseLoop=True
        while pauseLoop==True:                      #while qui permet de mettre en pause la fonction à la fin d'une manche
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       #fermeture de la fenêtre (croix rouge)
                    pauseLoop = False
                    troisManchesLoop = False
                if event.type == pygame.KEYDOWN:    #une touche a été pressée...laquelle ?
                    if event.key == pygame.K_ESCAPE: #touche echap pour quitter
                       pauseLoop = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:                #si la touche espace est appuyée, alors mettre fin à la pause
                pauseLoop=False


        fenetre.fill((0,0,0))   #efface la fenêtre
        motoVert=[motoVertX,motoVertY,directionVert,couleurMotoVert]        #remise à zéro des variables après avoir effectué une manche
        motoBlanc=[motoBlancX,motoBlancY,directionBlanc,couleurMotoBlanc]


    if scoreVert>scoreBlanc:
        dessineFin('vert')
    else:
        dessineFin('blanc')

    finLoop=True
    while finLoop==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finLoop = False            #fermeture de la fenêtre (croix rouge)

            if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
                if event.key == pygame.K_ESCAPE: #touche echap pour quitter
                    finLoop = False
                if event.key == pygame.K_SPACE:
                    finLoop = False


    critereEnregistrement=False
    while critereEnregistrement==False:
        nomPartie=str(input("Quel nom voulez-vous donner à cette partie ? (3 caractères attendus)"))
        if len(nomPartie)==3:
            critereEnregistrement=True
    scores.append([nomPartie.upper(),tempsPartie])
    fenetre.fill((0,0,0))   #efface la fenêtre
    print("nb itt",itteration)
    print('temps partie',tempsPartie)
    LanceAccueil()


def LanceAccueil():
    global scoreBlanc,scoreVert,scores
    scoreBlanc=0
    scoreVert=0
    dessineAccueil()
    accueilLoop=True
    while accueilLoop==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    accueilLoop = False            #fermeture de la fenêtre (croix rouge)                    
            if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
                if event.key == pygame.K_ESCAPE: #touche echap pour quitter
                    accueilLoop = False

                if event.key == pygame.K_SPACE:
                    accueilLoop=False
                    tempsPartie=0           #remet à 0 le temps de la partie
                    fenetre.fill((0,0,0))   #efface la fenêtre
                    LancePartie()

                elif event.key == pygame.K_TAB:
                    if len(scores)>0:
                        accueilLoop=False
                        fenetre.fill((0,0,0))   #efface la fenêtre
                        dessineTableauScore()
                    else:
                        print("Aucun score enregistré")
    pygame.quit()

LanceAccueil()
