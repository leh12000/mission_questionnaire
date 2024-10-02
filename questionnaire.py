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


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromJsonData(data):
        # ....
        choix=[ i[0] for i in data["choix"] ]
        bonne_reponse=[ i[0] for i in data["choix"] if i[1]]
        if len(bonne_reponse)!=1:
            return None
        q = Question(data["titre"],choix, bonne_reponse[0])
        return q

    def poser(self):
        print("QUESTION")
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
        questions=[ Question.FromJsonData(i) for i in questionnaire_data_questions ]


        return Questionnaire(questions,data["categorie"],data["titre"],data["difficulte"])


    def lancer(self):
        score = 0
        print("-------------")
        print("Questionaire : "+self.titre)
        print(" Categorie : " + self.categorie)
        print(" Difficulte : " + self.difficulte)
        print(" Nbr questions : " + str(len(self.questions)))
        print("-------------")
        print()
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score




filename="cinema_starwars_debutant.json"
file=open(filename,"r")
json_data=file.read()
file.close()
questionnaire_data=json.loads(json_data)



Questionnaire.fromJsonData(questionnaire_data).lancer()