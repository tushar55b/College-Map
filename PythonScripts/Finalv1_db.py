import networkx as nx
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show, from_networkx
from bokeh.io import curdoc
from bokeh.models import *
from bokeh.embed import autoload_static
from bokeh.themes import built_in_themes
from bokeh.resources import CDN
from bokeh.layouts import column
import sys
import math
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

#--------------------------------------------------------------------------------------#
# source = "BackGate"
# destination  = "Room1004"
source=str(sys.argv[1])
destination=str(sys.argv[2])

#fetching x,y coordinates from Nodes
pos = nx.get_node_attributes(G,'pos')

#Name of node is visible while hovering
hov_tooltips = [("Name","@index")]

#customizing plot
plot = figure(tooltips = hov_tooltips,width=1335,height=650, tools="pan,wheel_zoom,reset,zoom_in,zoom_out", 
            toolbar_location="above")

#best path found by minimizing cost/distance.
path1 = nx.shortest_path(G,source,destination,weight='weight',method='dijkstra')

#simple paths found by minimizing node count.
x = nx.shortest_simple_paths(G,source,destination)
path2 = list(next(x))

#If path1 and path2 are similar then path2 is the next simple path.
if path1 == path2:
    path2 = list(next(x))

#finding path 2
path2_edges = set(zip(path2,path2[1:]))
path2_foredges = path2

#creating bokeh's GraphRenderer from Networkx graph
graph = from_networkx(G, layout_function=pos,center=(0,0))

#Finding and storing x,y values of each node as List of tuples.
path1_xy = []
path2_xy = []   
for i in path1:
    path1_xy.append(pos[i])
    
for i in path2:
    path2_xy.append(pos[i])

#Path2 edges
plot.line(x=[i[0] for i in path2_xy], y=[i[1] for i in path2_xy], line_alpha=1.0, line_color='#88E0EF', line_width=5, name=None,legend_label='Path2')

#Path1 edges
plot.line(x=[i[0] for i in path1_xy], y=[i[1] for i in path1_xy], line_alpha=1.0, line_color='#00b300', line_width=5, name=None,legend_label='Optimal Path')

#starting and end node of path2
plot.circle(x=path2_xy[0][0], y=path2_xy[0][1], size=30, fill_color = '#88E0EF',legend_label='Path2')
plot.circle(x=path2_xy[len(path2_xy)-1][0], y=path2_xy[len(path2_xy)-1][1], size=30, fill_color = '#88E0EF',legend_label='Path2')

#path2
for i in range(1,len(path2_xy)-1):
    x = plot.circle(x=path2_xy[i][0],y=path2_xy[i][1],size=20,fill_color = '#88E0EF', legend_label='Path2')
    labels = LabelSet(x=path2_xy[i][0]-0.18, y=path2_xy[i][1], text=[path2[i]],angle=1,
    text_alpha=0.9, text_font_size={'value': '10pt'})
    plot.add_layout(labels)
    x.js_on_change('visible', CustomJS(args=dict(ls=labels),code="ls.visible = cb_obj.visible;"))

#Starting and end node of path1
plot.circle(x=path1_xy[0][0], y=path1_xy[0][1], size=30, fill_color = '#00b300',legend_label='Optimal Path')
plot.circle(x=path1_xy[len(path1_xy)-1][0], y=path1_xy[len(path1_xy)-1][1], size=30, fill_color = '#00b300',legend_label='Optimal Path')

#path1
for i in range(1,len(path1_xy)-1):
    x = plot.circle(x=path1_xy[i][0],y=path1_xy[i][1], size=20, fill_color = '#00b300', legend_label='Optimal Path')  
    labels = LabelSet(x=path1_xy[i][0]-0.18, y=path1_xy[i][1], text=[path1[i]],angle=1,
    text_alpha=0.9, text_font_size={'value': '10pt'})
    arrows = Arrow(end=NormalHead(size=10),x_start=path1_xy[i-1][0],y_start=path1_xy[i-1][1],
    x_end=path1_xy[i][0],y_end=path1_xy[i][1],line_width=0)
    plot.add_layout(labels)
    plot.add_layout(arrows)
    x.js_on_change('visible', CustomJS(args=dict(ls=labels),code="ls.visible = cb_obj.visible;"))
    x.js_on_change('visible', CustomJS(args=dict(ls=arrows),code="ls.visible = cb_obj.visible;"))

#Text for path 1
plot.text(x=path1_xy[0][0], y=path1_xy[0][1], text=[path1[0]], angle=1, text_alpha=1, text_font_style='bold', text_font_size={'value': '12pt'})
plot.text(x=path1_xy[len(path1_xy)-1][0]-0.18, y=path1_xy[len(path1_xy)-1][1], text=[path1[len(path1_xy)-1]], angle=1, text_alpha=1, text_font_style='bold', text_font_size={'value': '12pt'})

#Global edges and Nodes
graph_renderer = from_networkx(G, layout_function=pos)
graph_renderer.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=0.1, line_width=1)
graph_renderer.node_renderer.glyph = Circle(size=2, fill_color='#FFFDDE',fill_alpha=0.2)
plot.renderers.append(graph_renderer)

#Seprating line
plot.line(x=[0,34], y=[13.5,13.5],line_color='black',line_alpha=0.5, line_width=1.0, line_dash='dotdash')
plot.text(x=31.5, y=12.8, text=["Separator: GF & F1"],text_font_size={'value': '10pt'})
#Seprating line
plot.line(x=[0,34], y=[20.5,20.5],line_color='black',line_alpha=0.5, line_width=1.0, line_dash='dotdash')
plot.text(x=31.5, y=19.8, text=["Separator: F1 & F2"],text_font_size={'value': '10pt'})
#Seprating line
plot.line(x=[0,34], y=[26.5,26.5],line_color='black',line_alpha=0.5, line_width=1.0, line_dash='dotdash')
plot.text(x=31.5, y=25.8, text=["Separator: F2 & F3"],text_font_size={'value': '10pt'})


#Hide x,y axis
plot.xaxis.visible = False
plot.yaxis.visible = False
plot.xgrid.visible = False
plot.ygrid.visible = False

#Legend changes
plot.legend.click_policy="hide"
plot.legend.items = plot.legend.items[::-1]

#Set initial zoom and set bounds
path1_x = []
path2_x = []
path1_y = []
path2_y = []
for i in range(len(path1_xy)):
    path1_x.append(path1_xy[i][0])  
    path1_y.append(path1_xy[i][1])
    
for i in range(len(path2_xy)):
    path2_x.append(path2_xy[i][0])
    path2_y.append(path2_xy[i][1])

y_max = max(max(path1_y),max(path2_y))
y_min = min(min(path1_y),min(path2_y))
x_max = max(max(path1_x),max(path2_x))
x_min = min(min(path1_x),min(path2_x))
plot.y_range = Range1d(y_min -2,y_max +3,bounds=(-3,36))
plot.x_range = Range1d(x_min -2 ,x_max +3,bounds=(-2,37))

print('x_min  : ',x_min)
print('x_max  : ',x_max)
print('y_min  : ',y_min)
print('y_max  : ',y_max)

# height = 
# width = 
#Image
men_wr_xy = []
for i in G.nodes:
    if "MenWR" in i:
        men_wr_xy.append(pos[i])

for i in range(len(men_wr_xy)):
    room = ImageURL(url=["http://www.clipartbest.com/cliparts/jTx/p9B/jTxp9B4Xc.jpeg"],anchor="center",
    x=men_wr_xy[i][0] - 0.5,y=men_wr_xy[i][1] + 0.25,h=1,w=0.8)
    plot.add_glyph(room)


#showing shortest path on terminal
delimiter=' --> '
pathstr=delimiter.join(path1)
#readjusting the output without "\n"

#displaying path on Website
print("<div id='pathstr'> \n<b>Path from",source,"to",destination,":</b><br>")
print("<b>",path1[0],"</b>", end=" --> ") 
for i in range(1, len(path1)-1):
    print(path1[i], end=" --> ")
print("<b>",path1[len(path1)-1],"</b> <br>", end="")


js, tag = autoload_static(plot, CDN, 'graphjs.js')
with open('C:\\xampp\\htdocs\\project\\RunPythonWithPhp\\graphjs.js', 'w') as f1:
    f1.write(js)
with open('C:\\xampp\\htdocs\\project\\RunPythonWithPhp\\tag.TXT', 'w') as f2:
    f2.write(tag)

#show(plot)