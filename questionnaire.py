# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json

import sys
class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromJsonData(data):
        # ....Transforme les données choix tuple (titre,bool "bonne réponse") -> [choix, choix2.....]
        choix=[ i[0] for i in data["choix"] ]
        # Trouve le bon choix en fonction du bool "bonne réponse"
        bonne_reponse=[ i[0] for i in data["choix"] if i[1]]
        # Si aucune bonne réponse réponse ou plusieurs bonnes réponses -> Anomalie dans les données
        if len(bonne_reponse)!=1:
            return None
        q = Question(data["titre"],choix, bonne_reponse[0])
        return q

    def poser(self,num,nb_questions):
        print("QUESTION "+str(num)+"/"+str(nb_questions))
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions,categorie,titre,difficulte):
        self.questions = questions
        self.categorie=categorie
        self.titre=titre
        self.difficulte=difficulte

    def fromJsonData(data):
        questionnaire_data_questions=data["questions"]
        questions=[ Question.FromJsonData(i) for i in questionnaire_data_questions  ]
        #Supprime les questions None (qui n'ont pas pu etre crée)
        questions=[i for i in questions if i]


        return Questionnaire(questions,data["categorie"],data["titre"],data["difficulte"])

    def fromJsonfilename(filename):
        try:
            file = open(filename, "r")
            json_data = file.read()
            file.close()
            questionnaire_data = json.loads(json_data)
        except:
            print("Exception lors de la lecture ou l'ouverture du fichier")
            return None
        return Questionnaire.fromJsonData(questionnaire_data)


    def lancer(self):
        score = 0
        print("-------------")
        print("Questionaire : "+self.titre)
        print(" Categorie : " + self.categorie)
        print(" Difficulte : " + self.difficulte)
        print(" Nbr questions : " + str(len(self.questions)))
        print("-------------")
        print()
        for i in range(len(self.questions)):
            if self.questions[i].poser(i+1,len(self.questions)):
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score
"""

Questionnaire.fromJsonfilename("cinema_alien_expert.json").lancer()

"""
if len(sys.argv)<2:
    print("vous devez specifier le nom du fichier json a charger")
    exit(0)

filename=sys.argv[1]

questionnaire=Questionnaire.fromJsonfilename(filename)
if questionnaire:
    questionnaire.lancer()