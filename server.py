import flask
import json
import os
from flask import request, Response
from flask_pymongo import PyMongo
from dotenv import load_dotenv

import json
from bson import ObjectId

# Models
from Models.dfa import DFA
from Models.enfa import ENFA
from Models.nfa import NFA

# Graphs
import networkx as nx
from matplotlib import pyplot as plt

# Flask CORS Module
from flask_cors import CORS

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


# App Config
load_dotenv()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
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

# Routes


@app.route('/automatas', methods=['GET'])
def api_get_automatas():
    automatas = []
    for x in mongo.db.Automatas.find():
        automatas.append(x)

    json_automatas = JSONEncoder().encode(automatas)

    return Response(json_automatas, mimetype="json")

@app.route('/automatas/<type>', methods=['GET'])
def api_get_automatas_by_type(type):
    automatas = []
    for x in mongo.db.Automatas.find({"type": type}):
        automatas.append(x)

    for automata in automatas:
        automata["img"] = storage.child(path_on_cloud+'graph-'+str(automata['_id'])+'.png').get_url(None)

    json_automatas = JSONEncoder().encode(automatas)

    return Response(json_automatas, mimetype="json")

@app.route('/automata/<id>', methods=['GET'])
def api_get_automata_by_id(id):
    automata = mongo.db.Automatas.find({"_id": ObjectId(id)})[0]
    json_automata = JSONEncoder().encode(automata)

    return Response(json_automata, mimetype="json")


@app.route('/automatas/<evalType>/<automataID>/<expression>', methods=['GET'])
def api_get_evaluation(evalType, automataID, expression):
    if evalType == "dfa":
        dbAutomata = mongo.db.Automatas.find({"_id": ObjectId(automataID)})[0]
        automata = DFA(dbAutomata, set(dbAutomata["accepting_states"]), objectToTupleKeys(dbAutomata["transitions"]))
        return Response(JSONEncoder().encode({'response': automata.evaluate(expression)}), mimetype="json")
    elif (evalType == "enfa"):
        dbAutomata = mongo.db.Automatas.find({"_id": ObjectId(automataID)})[0]
        automata = ENFA(dbAutomata, set(dbAutomata["accepting_states"]), objectToTupleKeys(dbAutomata["transitions"]))
        nfaEquivalent = automata.evaluate(expression)
        dfaEquivalent = nfaEquivalent.evaluate(expression)
        return Response(JSONEncoder().encode({'response': ""}), mimetype="json")
        # dfaEquivalent = nfaEquivalent.evaluate(expression)
        # return Response(JSONEncoder().encode({'response': dfaEquivalent.evaluate(expression)}, mimetype="json"))


    return Response(JSONEncoder().encode({'reponse': 'ERROR'}), mimetype="json")


@app.route('/automata', methods=['POST'])
def api_post_automata():
    mongo.db.Automatas.insert_one(request.json)
    newAutomata = mongo.db.Automatas.find().sort([('_id', -1)])[0]

    # G = nx.DiGraph()
    # for state in newAutomata["states"]:
    #     G.add_node(state)

    # edges = []
    # keys = list(newAutomata["transitions"].keys())
    # transitions = newAutomata["transitions"]
    # for key in keys:
    #     dividedKey = key.split(',')
    #     edges.append(
    #         (dividedKey[0], transitions[key], dividedKey[1].replace(" ", "")))

    # G.add_weighted_edges_from(edges)
    # nx.draw_networkx(G)

    # graphName = "graph-" + str(newAutomata["_id"])+".png"
    # plt.savefig(graphName)

    # storage.child(path_on_cloud+graphName).put(graphName)

    # os.remove(graphName)

    return "ok"


app.run()
