from flask import Flask, jsonify, request
from flask_cors import CORS  # Omogočimo CORS
import random


app = Flask(__name__)
CORS(app)  # Omogoči CORS za celotno aplikacijo

# Seznam vprašanj in odgovorov
questions = [
    {"question": "Katero edinstveno značilnost ima Trinucleus goldfussi?", 
     "options": ["Perforirano obrobje na glavi", "Dve glavi", "Širok rep", "Dolga oklepna struktura"], "correct": 0},
    {"question": "Kje najdemo fosile Trinucleus goldfussi?", 
     "options": ["V ordovicijskih slojih po Evropi", "V devonskih slojih v Ameriki", "V silurskih slojih v Avstraliji", "V kambrijskih slojih v Afriki"], "correct": 0},
    {"question": "Kaj je podpiralo čutilne dlačice pri Trinucleus goldfussi?", 
     "options": ["Perforirano obrobje na glavi", "Majhne oči", "Lepi oklep", "Repni oklep"], "correct": 0},
    {"question": "Kako se je Trinucleus goldfussi zanašal na čutila?", 
     "options": ["Z razmeroma majhnimi očmi", "S pomožnimi čutnimi organi", "Z večjim telesom", "Z dvema glavama"], "correct": 0},
    {"question": "Kaj je pomagal Trinucleus goldfussi ohraniti stabilnost?", 
     "options": ["Široka glava", "Majhne oči", "Podolgovato telo", "Prožno telo"], "correct": 0},
    {"question": "Katera vrsta trilobita je ena najbolj prepoznavnih iz ordovicijskega obdobja?", 
     "options": ["Trinucleus goldfussi", "Illaenus dalmanni", "Olenus truncatus", "Olenellus kjerfuli"], "correct": 0},

    {"question": "Kdaj je živel Olenellus kjerulfi?", 
     "options": ["Zgodnji kambrij", "Pozni devon", "Srednji kambrij", "Pozni silur"], "correct": 0},
    {"question": "Kje pogosto najdemo fosile vrste Olenellus kjerulfi?", 
     "options": ["V Severni Ameriki in Evropi", "V Afriki", "V Avstraliji", "V Aziji"], "correct": 0},
    {"question": "Kaj je bila posebnost repa vrste Olenellus kjerulfi?", 
     "options": ["Ni bil zraščen", "Bil je razvejan", "Bil je dolg in tanek", "Imel je bodice"], "correct": 0},
    {"question": "Kaj je vrsta Olenellus kjerulfi iskala na morskem dnu?", 
     "options": ["Organski material", "Voda", "Ogljik", "Mikroorganizme"], "correct": 0},
    {"question": "Kakšna je bila pomembnost vrste Olenellus kjerulfi v evoluciji?", 
     "options": ["Igra ključni vlogo pri razumevanju evolucije členonožcev", "Odpira vrata za morske vrste", "Je bila začetnica oklepnih živali", "Pospešila je razvoj kril"], "correct": 0},
    {"question": "Zakaj so fosili trilobitov tako pogosti?", 
     "options": ["Ker so odvrgli oklep, ko so rasli", "Ker so se pogosto premikali skozi trda tla", "Ker so se spremenili v fosile takoj po smrti", "Ker so živeli v tropih"], "correct": 0},

    {"question": "Kje je živel Olenus truncatus?", 
     "options": ["V morskih okoljih z malo kisika", "V plitvih rekah", "V tropskih vodah", "Na globokem morju"], "correct": 0},
    {"question": "Katero prilagoditev je imel Olenus truncatus za življenje v anoksičnih razmerah?", 
     "options": ["Dolgo, tanko telo", "Velike oči", "Svetel oklep", "Počasno premikanje"], "correct": 0},
    {"question": "Kje najdemo fosile vrste Olenus truncatus?", 
     "options": ["Na Švedskem in v Veliki Britaniji", "V Južni Ameriki", "Na Islandiji", "V Afriki"], "correct": 0},
    {"question": "Kakšen je bil način življenja vrste Olenus truncatus?", 
     "options": ["Plazenje skozi blatne substratke", "Skakanje po tleh", "Zrakoplovno letenje", "Preživetje na vegetaciji"], "correct": 0},
    {"question": "Kaj so imeli trilobiti, kot je Olenus truncatus, prilagodljivo?", 
     "options": ["Segmentirana srednja regija", "Povečane oči", "Večji repi", "Jasna obroba oklepa"], "correct": 0},
    {"question": "V katerem okolju so fosili Olenus truncatus pogosto ohranjeni?", 
     "options": ["V črnem skrilavcu", "V glinenih plasteh", "V peščenih slojih", "V mešanih vodah"], "correct": 0},

    {"question": "Kakšen je bil videz telesa Illaenus dalmanni?", 
     "options": ["Gladko in zaobljeno", "Ostranjeno z ostrimi robovi", "Pohabljeno in zračeno", "Z velikimi udarci na oklepu"], "correct": 0},
    {"question": "Kje se pogosto najdejo fosili Illaenus dalmanni?", 
     "options": ["V ordovicijskih kamninah v Evropi", "V morjih v Severni Ameriki", "V devonskih slojih v Aziji", "Na Avstralskem kontinentu"], "correct": 0},
    {"question": "Kakšen način življenja je imel Illaenus dalmanni?", 
     "options": ["Zakopavanje v sediment ali plazenje po dnu", "Plavanje", "Letenje z majhnimi krili", "Jedo na morju"], "correct": 0},
    {"question": "Kaj je omogočalo Illaenus dalmanni učinkovito gibanje po blatu?", 
     "options": ["Minimalistična oblika", "Velike noge", "Hitrost plavanja", "Majhne oči"], "correct": 0},
    {"question": "Kako so bile oči Illaenus dalmanni?", 
     "options": ["Majhne, ovalne", "Velike, okrogle", "Ostre in podolgovate", "Ni jih imel"], "correct": 0},
    {"question": "Kaj je nudilo dodatno zaščito Illaenus dalmanni?", 
     "options": ["Velika glava", "Mali rep", "Vezan oklep", "Izbočeno telo"], "correct": 0},

    {"question": "Kaj je bilo značilno za rep Encrinurus punctatus?", 
     "options": ["Imel je izbokline in bodice", "Bil je dolg in gladek", "Bil je brez oblike", "Zelo širok"], "correct": 0},
    {"question": "Kdaj je živel Encrinurus punctatus?", 
     "options": ["Med silurjem, pred približno 435-420 milijoni let", "V srednjem kambriju", "Med obdobjem devona", "V zgodnjem triasu"], "correct": 0},
    {"question": "Kje pogosto najdemo fosile Encrinurus punctatus?", 
     "options": ["V Angliji in Walesu", "Na Madžarskem", "V Rusiji", "Na Islandiji"], "correct": 0},
    {"question": "Kaj je pomagal Encrinurus punctatus pri preživetju?", 
     "options": ["Močan oklep za obrambo pred plenilci", "Večje oči", "Daljši rep", "Zaobljen oklep"], "correct": 0},
    {"question": "Kaj je bilo življenjski slog Encrinurus punctatus?", 
     "options": ["Bentoski mrhovinar", "Plavajoči plenilec", "Plenilski herbivore", "Skakalec"], "correct": 0},
    {"question": "Kakšen je bil način vida pri trilobitih kot je Encrinurus punctatus?", 
     "options": ["Skoraj 360-stopinjski vid", "Samo sprednji vid", "Vidni organski okus", "Samo naključna zaznava"], "correct": 0},

]

@app.route('/quiz', methods=['GET'])
def get_quiz():
    try:
        num_questions = int(request.args.get('num', 10))  # privzeto na 10
        selected_questions = random.sample(questions, min(num_questions, len(questions)))
        return jsonify(selected_questions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



