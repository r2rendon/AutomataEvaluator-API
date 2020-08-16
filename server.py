import flask
import json
import os
from flask import request, Response
from flask_pymongo import PyMongo

import json
from bson import ObjectId

# Graphs
import networkx as nx
from matplotlib import pyplot as plt

# Firebase
import pyrebase

# Firebase config
config = {
    "apiKey": "AIzaSyDdKRfNx47GbMB8Wwda43I0nCqfzSrpAIE",
    "authDomain": "automataproject-1d04b.firebaseapp.com",
    "databaseURL": "https://automataproject-1d04b.firebaseio.com",
    "projectId": "automataproject-1d04b",
    "storageBucket": "automataproject-1d04b.appspot.com",
    "messagingSenderId": "561854169181",
    "appId": "1:561854169181:web:4259d1278cc1c88c3ccdb4",
    "measurementId": "G-CLEDM4528N"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_on_cloud = "automataImages/"


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Config de la aplicacion
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb+srv://r2Admin:5PuWyaH2lcomqtCx@cluster0-lt7z4.mongodb.net/TeoriaCompuDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

# API Functions

# This function creates the tuple keys for the dictionary in the transitions key


def objectToTupleKeys(obj):
    keys = list(obj.keys())
    tupleObj = dict()

    for k in keys:
        dividedTupleElements = k.split(',')
        tupleObj[(dividedTupleElements[0],
                  dividedTupleElements[1].replace(" ", ""))] = obj[k]

    return tupleObj

# This is the DFA evaluator


def dfa_evaluate(automata, expression):
    initial_state = automata["initial_state"]
    accepting_states = automata["accepting_states"]
    transitions = automata["transitions"]

    current_state = initial_state

    transition_exists = True

    for char_index in range(len(expression)):
        current_char = expression[char_index]

        if ((current_state, current_char) not in transitions):
            transition_exists = False
            break
        next_state = transitions[(current_state, current_char)]
        # print(current_state, current_char, next_state) This format can be used to return the evaluation process in the automata
        current_state = next_state

    # If the transition exists and the current state is an accepting state, then the expression belongs to the automata
    return (transition_exists and current_state in accepting_states)

# Routes


@app.route('/automatas', methods=['GET'])
def api_get_automatas():
    automatas = []
    for x in mongo.db.Automatas.find():
        automatas.append(x)

    json_automatas = JSONEncoder().encode(automatas)

    return Response(json_automatas, mimetype="json").status_code(200)


@app.route('/automatas/<id>', methods=['GET'])
def api_get_automata_by_id(id):
    automata = mongo.db.Automatas.find({"_id": ObjectId(id)})[0]
    json_automata = JSONEncoder().encode(automata)

    return Response(json_automata, mimetype="json").status_code(200)


@app.route('/automatas/<evalType>/<automataID>/<expression>', methods=['GET'])
def api_get_evaluation(evalType, automataID, expression):
    if evalType == "dfa":
        dbAutomata = mongo.db.Automatas.find({"_id": ObjectId(automataID)})[0]
        automata = {
            'initial_state': dbAutomata["initial_state"],
            'accepting_states': set(dbAutomata["accepting_states"]),
            'transitions': objectToTupleKeys(dbAutomata["transitions"])
        }
        return Response(JSONEncoder().encode({'response': dfa_evaluate(automata, expression)}), mimetype="json").status_code(200)

    return "ERROR"


@app.route('/automata', methods=['POST'])
def api_post_automata():
    mongo.db.Automatas.insert_one(request.json)
    newAutomata = mongo.db.Automatas.find().sort([('_id', -1)])[0]

    G = nx.DiGraph()
    for state in newAutomata["states"]:
        G.add_node(state)

    edges = []
    keys = list(newAutomata["transitions"].keys())
    transitions = newAutomata["transitions"]
    for key in keys:
        dividedKey = key.split(',')
        edges.append(
            (dividedKey[0], transitions[key], dividedKey[1].replace(" ", "")))

    G.add_weighted_edges_from(edges)
    nx.draw_networkx(G, with_label=True)

    graphName = "graph-" + str(newAutomata["_id"])+".png"
    plt.savefig(graphName)

    storage.child(path_on_cloud+graphName).put(graphName)

    os.remove(graphName)

    return "ok"


app.run()
