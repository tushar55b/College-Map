import networkx as nx
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show, from_networkx
from bokeh.io import curdoc
from bokeh.models import Circle, MultiLine, GraphRenderer, Label, Text, Arrow, NormalHead
from bokeh.embed import autoload_static
from bokeh.themes import built_in_themes
from bokeh.resources import CDN
import sys
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://FindDsc:DsC595851@cluster0.3euxl.mongodb.net/FindDscDb?retryWrites=true&w=majority")
db = cluster['FindDscDb']
collection_nodes = db['Nodes']
collection_edges = db['Edges']

results_nodes = collection_nodes.find()
results_edges = collection_edges.find()

G=nx.Graph()
for i in results_nodes:
    G.add_node(i['name'],pos=tuple(i['pos']))

for i in results_edges:
    G.add_edge(i['node1'],i['node2'],weight=i['weight'])
