import random
import math
# fonction pour generer le questionnaire
def generer_questionnaire():
    # stocker un choix arbitraire entier dans les variables nombre1 et nombre 2
    nombre1 = random.randint(1, 9)
    nombre2 = random.randint(1, 9)
    # choisir au hasard un operateur dans une liste
    operation = random.choice(['+', '-', '*', '/', '%', '//'])
    # afficher la question resultante des nombres et de l'operation choisis aleatoirement
    question = f"{nombre1} {operation} {nombre2}"

    # Calcule la reponse 
    

    if operation == '+':
        reponse_correcte = nombre1 + nombre2
    elif operation == '-':
        reponse_correcte = nombre1 - nombre2
    elif operation == '*':
        reponse_correcte = nombre1 * nombre2
    elif operation == '/':
        reponse_correcte = (nombre1 / nombre2)
    elif operation == '%':
        reponse_correcte = nombre1 % nombre2
    elif operation == '//':
        reponse_correcte = nombre1 // nombre2

    # retourner la question et la reponse correcte pour les utiliser dans la prochaine fonction

    return question, reponse_correcte


def poser_questions(nbq):
    # initialiser le score a 0
    # definir une liste vide pour les mauvaises reponse pour la remplir plus tard
    score = 0
    mauvaises_reponses = []
    #parcourir le nombre de questions saisi par l'utilisateur
    for i in range(1,nbq+1):
        # faire un appel a la fonction precedente et stocker ses valeur retourner dans question et reponse_correcte
        question, reponse_correcte = generer_questionnaire()
        # afficher la questions tire au hasard et sauvgarder la reponse de l'utilisateur
        reponse_utilisateur = float(input(f"Question de mouloud {i} : {question} = "))
        # tester si c'est une reponse correcte par rapport a la valeur retourner par la fonction generer_questionnaire()
        if reponse_utilisateur == reponse_correcte:
            # incrementer la valeur du score si cest une bonne reponse
            score += 1
        else:
            # ajouter les elements suivant : question, reponse_utilisateur, reponse_correcte, pour un affichage optimal
            mauvaises_reponses.append((question, reponse_utilisateur, reponse_correcte))

    # afficher le score
    print(f"Votre score est: {score}\n")
    # tester l'existance de mauvaises reponses
    if mauvaises_reponses:
        # affichage d'un message introductif
        print("voici tes mauvaises reponse:")
        #parcourir les elements de la liste mauvaises_reponse et les afficher
        for question, reponse_utilisateur, reponse_correcte in mauvaises_reponses:
            print(
                f"{question} = {reponse_utilisateur}, mais la bonne reponse est {reponse_correcte : .2f}.")

# fonction qui permet de demander a l'utilisateur de choisir s'il veux continuer une autre partie
def saisir_Choix () :
    x = input(f"Est-ce que tu veux faire un autre questionnaire \n Saisir O (Oui) ou N (Non) : ").upper()
    #tant que la reponse n'est pas un O ou N on reaffiche le message qui l'invite a saisir sa reponse
    while x != "O" and x != "N":
        x = input(f"ReSaisir O (Oui) ou N (Non) : ").upper()
    return x

# programme principal
# initialiser la numerotation des questionnaire a 1
i = 1
# tant que cest vrai
while True:
    # on invite l'utilisateur a saisir le nombre de questions
    print(f"----------Questionnaire {i}----------------------")
    nombre_questions = int(input("Saisir le nombre de questions : "))
    # faire l'appel a la fonction qui prends en parametre le nombre de questions que le user veux
    poser_questions(nombre_questions)
    print(f"----------Fin Questionnaire {i}----------------------")
    # sauvgarder la sortie de la fonction saisir_Choix() dans la variable reponse
    reponse = saisir_Choix()
    # si le user ne veut pas refaire une partie  on break on arrete le programme
    if reponse == "N":
        print("Aurevoir ...")
        break
    else:
        #incrementer la numerotation des questionnaire
        i += 1


