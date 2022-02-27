import networkx as nx
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show, from_networkx
from bokeh.io import curdoc
from bokeh.models import Circle, MultiLine, GraphRenderer, Label, Text, Arrow, NormalHead
from bokeh.embed import autoload_static
from bokeh.themes import built_in_themes
from bokeh.resources import CDN
import sys

G=nx.Graph()

G.add_node("MainGate",pos=(1,-4))
G.add_node("OutdoorOffice",pos=(2,-3.5))
G.add_node("T-section",pos=(1,-3))
G.add_node("T-Section2",pos=(7,-3))
G.add_node("T-section3",pos=(-5,-1.5))
G.add_node("CollegeGarden",pos=(3,-2))
G.add_node("MainEntrance",pos=(0,-1))
G.add_node("NCCGround1",pos=(-0.5,-2))
G.add_node("NCCGround2",pos=(-9,-1.5))
G.add_node("NCCGround",pos=(-5,-3))
G.add_node("PrincipalsOffice",pos=(1,0))
G.add_node("AdminOffice",pos=(-1,0))
G.add_node("Stairs1GF",pos=(0,1))
G.add_node("DyalSinghStatue",pos=(0,0))
G.add_node("NSBEntrance",pos=(1,1))
G.add_node("Stairs2GF",pos=(0.5,2))
G.add_node("PhyLab3",pos=(0.5,3))
G.add_node("CSHoDOffice",pos=(1,3))
G.add_node("Stairs3GF",pos=(1.5,3))
G.add_node("CSLab1",pos=(0.5,4))
G.add_node("CSLab2",pos=(1,4))
G.add_node("MensWashroom3",pos=(2,4))
G.add_node("Room1",pos=(-2,0))
G.add_node("Room2",pos=(-3,0))
G.add_node("Room3",pos=(-4,0))
G.add_node("DisconnectedLobby",pos=(-5,0))
G.add_node("MensWashroom2",pos=(-4,1))
G.add_node("Library",pos=(-5,3))
G.add_node("Amphitheatre",pos=(-1.5,3))
G.add_node("Stairs5GF",pos=(-4.5,-0.5))
G.add_node("ChemLab1",pos=(2,0))
G.add_node("ChemLab2",pos=(3,0))
G.add_node("PhyLab1",pos=(4,0))
G.add_node("PhyLab2",pos=(5,0))
G.add_node("MensWashroom1",pos=(4,1))
G.add_node("WomensWashroom1",pos=(5,1))
G.add_node("Stairs4GF",pos=(6,-0.5))

#new nodes
G.add_node("BasketballCourt",pos=(10,0))
G.add_node("RoseGarden",pos=(9.5,-3.5))
G.add_node("BRLobby",pos=(7.5,0))
G.add_node("BRoom1",pos=(7.5,-1))
G.add_node("BRoom2",pos=(7.5,-0.5))
G.add_node("BRoom3",pos=(7.5,0.5))
G.add_node("BRoom4",pos=(7.5,1.2))
G.add_node("BRoom5",pos=(7.5,2))
G.add_node("BRoom6",pos=(7.5,2.8))
G.add_node("Parking",pos=(4.5,-3))


G.add_node("GreenLobby",pos=(-3.5,2))
G.add_node("ConferenceHall",pos=(-6.5,1))
G.add_node("FoyerRoom",pos=(-6,-1))
G.add_node("MedicalRoom",pos=(-7,-1))
G.add_node("Stairs6GF",pos=(-8,-0.5))
G.add_node("CanteenEntrance",pos=(-9,0))
G.add_node("Canteen",pos=(-10,0))
G.add_node("DSCEve",pos=(-9,3))
G.add_node("CollegePlayground",pos=(-12,2.5))
G.add_node("BackGate",pos=(-14,0))


#main gate
G.add_edge("MainGate","OutdoorOffice",weight=31)
G.add_edge("MainGate","T-section",weight=42)

#outdoor Office
G.add_edge("OutdoorOffice","T-section",weight=36)
G.add_edge("OutdoorOffice","Parking",weight=39)

#T-section
G.add_edge("T-section","CollegeGarden",weight=13)
G.add_edge("T-section","MainEntrance",weight=45)
G.add_edge("T-section","Parking",weight=18)

#main entrance
G.add_edge("MainEntrance","NCCGround1",weight=12)
G.add_edge("MainEntrance","DyalSinghStatue",weight=8.5)
#G.add_edge("MainEntrance","AdminOffice",weight=1)
#G.add_edge("MainEntrance","Stairs1GF",weight=1)
#G.add_edge("MainEntrance","PrincipalsOffice",weight=1)

#T-section3
G.add_edge("T-section3","MainEntrance",weight=74)
G.add_edge("T-section3","DisconnectedLobby",weight=11.5)
G.add_edge("T-section3","NCCGround2",weight=38)

#Statue
G.add_edge("DyalSinghStatue","Stairs1GF",weight=5)
G.add_edge("DyalSinghStatue","AdminOffice",weight=15)
G.add_edge("DyalSinghStatue","PrincipalsOffice",weight=13)

#NCC Ground
G.add_edge("NCCGround","NCCGround1",weight=77)
G.add_edge("NCCGround","NCCGround2",weight=48)

#Admin Office
#G.add_edge("AdminOffice","Stairs1GF",weight=1)
#G.add_edge("AdminOffice","PrincipalsOffice",weight=1)
G.add_edge("AdminOffice","Amphitheatre",weight=30)
G.add_edge("AdminOffice","Room1",weight=20)

#PrincipalsOffice
#G.add_edge("PrincipalsOffice","Stairs1GF",weight=1)
G.add_edge("PrincipalsOffice","ChemLab1",weight=15.6)
G.add_edge("PrincipalsOffice","NSBEntrance",weight=15)

#ChemLab1
G.add_edge("ChemLab1","ChemLab2",weight=15.6)

#ChemLab2
G.add_edge("ChemLab2","PhyLab1",weight=15.6)

#PhyLab1
G.add_edge("PhyLab1","MensWashroom1",weight=5)
G.add_edge("PhyLab1","PhyLab2",weight=15.6)

#PhyLab2
G.add_edge("PhyLab2","Stairs4GF",weight=15.6)
G.add_edge("PhyLab2","WomensWashroom1",weight=5)

#MensWashroom1
#G.add_edge("MensWashroom1","WomensWashroom1",weight=15.6)

#NSBEntrance
G.add_edge("NSBEntrance","Stairs2GF",weight=10)
G.add_edge("NSBEntrance","CSHoDOffice",weight=22)
G.add_edge("NSBEntrance","PhyLab3",weight=17)

#Stairs2GF
#G.add_edge("Stairs2GF","PhyLab3",weight=1)
#G.add_edge("Stairs2GF","CSHoDOffice",weight=1)

#PhyLab3
G.add_edge("PhyLab3","CSHoDOffice",weight=7)
G.add_edge("PhyLab3","CSLab1",weight=5)
#G.add_edge("PhyLab3","CSLab2",weight=1)
#G.add_edge("PhyLab3","MensWashroom3",weight=1)
#G.add_edge("PhyLab3","Stairs3GF",weight=1)

#CSLab1
G.add_edge("CSLab1","CSLab2",weight=5)
#G.add_edge("CSLab1","Stairs3GF",weight=1)
G.add_edge("CSLab1","CSHoDOffice",weight=5)

#CSLab2
#G.add_edge("CSLab2","Stairs3GF",weight=1)
G.add_edge("CSLab2","CSHoDOffice",weight=5)
#G.add_edge("CSLab2","MensWashroom3",weight=1)

#MensWashroom3
G.add_edge("MensWashroom3","Stairs3GF",weight=10)
G.add_edge("MensWashroom3","CSHoDOffice",weight=15)

#CSHodOffice
G.add_edge("CSHoDOffice","Stairs3GF",weight=8)

#Library
#G.add_edge("Library","Amphitheatre",weight=1)
G.add_edge("Library","GreenLobby",weight=30)
G.add_edge("Library","DisconnectedLobby",weight=19)
G.add_edge("Library","DSCEve",weight=74)
G.add_edge("Library","CanteenEntrance",weight=54)

#Amphitheatre
G.add_edge("Amphitheatre","GreenLobby",weight=35)
G.add_edge("Amphitheatre","Room2",weight=33)

#Room1
G.add_edge("Room1","Room2",weight=14)
G.add_edge("Room1","Amphitheatre",weight=31)

#Room2
G.add_edge("Room2","Room3",weight=14)
G.add_edge("Room2","GreenLobby",weight=21)

#Room3
G.add_edge("Room3","MensWashroom2",weight=5)
G.add_edge("Room3","DisconnectedLobby",weight=23)
G.add_edge("Room3","Stairs5GF",weight=7)

#Stairs5GF
G.add_edge("Stairs5GF","DisconnectedLobby",weight=16)

#DisconnectedLobby
G.add_edge("DisconnectedLobby","GreenLobby",weight=28)
G.add_edge("DisconnectedLobby","ConferenceHall",weight=15)
G.add_edge("DisconnectedLobby","FoyerRoom",weight=15)
G.add_edge("DisconnectedLobby","CanteenEntrance",weight=39)

#ConferenceHall
G.add_edge("ConferenceHall","FoyerRoom",weight=5)
G.add_edge("ConferenceHall","MedicalRoom",weight=13)
G.add_edge("ConferenceHall","Stairs6GF",weight=16)

#MedicalRoom
G.add_edge("MedicalRoom","FoyerRoom",weight=10)
G.add_edge("MedicalRoom","Stairs6GF",weight=7)

#CanteenEntrance
G.add_edge("CanteenEntrance","Stairs6GF",weight=13)
G.add_edge("CanteenEntrance","Canteen",weight=6)
G.add_edge("CanteenEntrance","DSCEve",weight=43)
G.add_edge("CanteenEntrance","GreenLobby",weight=78)
G.add_edge("CanteenEntrance","NCCGround2",weight=17)

#DSCEve
G.add_edge("DSCEve","Library",weight=75)
G.add_edge("DSCEve","CollegePlayground",weight=53)

#BackGate
G.add_edge("BackGate","CollegePlayground",weight=53)
G.add_edge("BackGate","Canteen",weight=126)

#BRLobby
G.add_edge("BRLobby","PhyLab2",weight=25)
G.add_edge("BRLobby","BRoom2",weight=6)
G.add_edge("BRLobby","BRoom3",weight=6)
G.add_edge("BRLobby","BasketballCourt",weight=40)

#BRoom1
G.add_edge("BRoom1","T-Section2",weight=25)
G.add_edge("BRoom1","BRoom2",weight=7)
G.add_edge("BRoom1","RoseGarden",weight=30)
G.add_edge("BRoom1","CollegeGarden",weight=40)

#BRoom3 & BRoom4
G.add_edge("BRoom3","BRoom4",weight=7)

#BRoom4 & BRoom5
G.add_edge("BRoom4","BRoom5",weight=7)

#BRoom5 & BRoom6
G.add_edge("BRoom5","BRoom6",weight=7)

#T-Section2
G.add_edge("T-Section2","Parking",weight=25)
G.add_edge("T-Section2","RoseGarden",weight=20)

#~~~~~~~~~~~~~~~~~ GROUND FLOOR EDGES END HERE~~~~~~~~~~~~~~~~~~~~~~~~~~#
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
#_______________________________________ FLOOR 1 _______________________________________________
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________

# ~~~~~~~~~~~ NODES ~~~~~~~~~~~~~~~~~

G.add_node("Room4",pos=(-4,7))
G.add_node("Room5",pos=(-3,7))
G.add_node("Room6",pos=(-2,7))
G.add_node("StaffRoom1",pos=(-1,7))
G.add_node("Room7",pos=(1,7))
G.add_node("Room8",pos=(2,7))
G.add_node("Room9",pos=(3,7))
G.add_node("Room10",pos=(4,7))
G.add_node("Room11",pos=(5,7))
G.add_node("Room12",pos=(6,7))
G.add_node("Stairs4F1",pos=(7,7))
G.add_node("Stairs1F1",pos=(0,8))
G.add_node("Stairs5F1",pos=(-5.2,6.5))
G.add_node("GirlsCommonRoom",pos=(-5,6))
G.add_node("WomensWashroom2",pos=(-6,6.5))
G.add_node("Room101",pos=(-7,7.5))
G.add_node("Room102",pos=(-7,6.5))
G.add_node("Room103",pos=(-8,7.5))
G.add_node("Room104",pos=(-8,6.5))
G.add_node("Stairs6F1",pos=(-9,7))
G.add_node("ConnectingLobby",pos=(1.5,9))
G.add_node("Stairs2F1",pos=(0.5,10))
G.add_node("Room1001",pos=(1.5,11))
G.add_node("Room1002",pos=(1.5,12))
G.add_node("Room1003",pos=(1.5,13))
G.add_node("Room1004",pos=(2.5,13))
G.add_node("WomensWashroom3",pos=(4,13))
G.add_node("Stairs3F1",pos=(3.5,12))

# ~~~~~~~~~~~ EDGES ~~~~~~~~~~~~~~~~~

#Stairs6F1
G.add_edge("Stairs6F1","Room103",weight=7.8)
G.add_edge("Stairs6F1","Room104",weight=7.8)
G.add_edge("Stairs6F1","Stairs6GF",weight=10)

#Room103
G.add_edge("Room103","Room104",weight=5)
G.add_edge("Room103","Room101",weight=15.6)

#Room104
G.add_edge("Room104","Room102",weight=15.6)

#Room101
G.add_edge("Room101","Room102",weight=5)
G.add_edge("Room101","WomensWashroom2",weight=20)

#Room102
G.add_edge("Room102","WomensWashroom2",weight=20)

#WomensWashroom2
G.add_edge("WomensWashroom2","GirlsCommonRoom",weight=7)

#GirlsCommonRoom
G.add_edge("GirlsCommonRoom","Stairs5F1",weight=7)
G.add_edge("GirlsCommonRoom","Room4",weight=12.1)

#Stairs5F1
G.add_edge("Stairs5F1","Room4",weight=7.1)
G.add_edge("Stairs5F1","Stairs5GF",weight=10)

#
G.add_edge("Room4","Room5",weight=14.2)
G.add_edge("Room5","Room6",weight=14.2)
G.add_edge("Room6","StaffRoom1",weight=14.2)
G.add_edge("StaffRoom1","Room7",weight=14.2)

#Stairs1F1
G.add_edge("Stairs1F1","StaffRoom1",weight=7)
G.add_edge("Stairs1F1","Room7",weight=7)
G.add_edge("Stairs1F1","Stairs1GF",weight=10)

#Room7-12
G.add_edge("Room7","Room8",weight=14.2)
G.add_edge("Room8","Room9",weight=14.2)
G.add_edge("Room9","Room10",weight=14.2)
G.add_edge("Room10","Room11",weight=14.2)
G.add_edge("Room11","Room12",weight=14.2)

#Stairs4F1
G.add_edge("Room12","Stairs4F1",weight=7.1)
G.add_edge("Stairs4F1","Stairs4GF",weight=10)

#ConnectingLobby
G.add_edge("ConnectingLobby","Room7",weight=8)
G.add_edge("ConnectingLobby","Stairs2F1",weight=8)

#Stairs2F1
G.add_edge("Stairs2F1","Room1001",weight=7)
G.add_edge("Stairs2F1","Stairs2GF",weight=10)

#Stairs3F1
G.add_edge("Stairs3F1","Room1002",weight=10)
G.add_edge("Stairs3F1","Room1004",weight=7)
G.add_edge("Stairs3F1","WomensWashroom3",weight=7)
G.add_edge("Stairs3F1","Stairs3GF",weight=10)

#Room1001-1004
G.add_edge("Room1001","Room1002",weight=10)
G.add_edge("Room1002","Room1003",weight=10)
G.add_edge("Room1003","Room1004",weight=5)
#G.add_edge("Room1004","WomensWashroom3",weight=1)
#~~~~~~~~~~~~~ FIRST FLOOR EDGES END HERE ~~~~~~~~~~~~~~~~~~~~~~~


#--------------------------------------------------------------------------------------#
source = "BackGate"
destination  = "Room1004"
# source=str(sys.argv[1])
# destination=str(sys.argv[2])

#fetching x,y coordinates from Nodes
pos=nx.get_node_attributes(G,'pos')

#html outputfile name
output_file("TryHtml.html")

#Name of node is visible while hovering
hov_tooltips = [("Name","@index")]

#customizing plot
plot = figure(tooltips = hov_tooltips,width=1335,height=650, tools="pan,wheel_zoom,reset,zoom_in,zoom_out,box_zoom", 
            toolbar_location="above")


#finding shortest paths
#best path
path1 = nx.shortest_path(G,source,destination,weight='weight',method='dijkstra')
#alternative paths
x = nx.shortest_simple_paths(G,source,destination)

all_pathsnodes = []
path2 = []
path3 = []
for i in range(2):
    all_pathsnodes.append(next(x))

#finding path 2
path2 = all_pathsnodes[0]
path2_edges = set(zip(path2,path2[1:]))

#finding path 3
path3 = all_pathsnodes[1]
path3_edges = set(zip(path3,path3[1:]))

path2_foredges = path2
path3_foredges = path3

# removing extra nodes from the lists of path2 & path3
path2 = list(set(path2) - set(path1))
path3 = list(set(path3) - set(path2) - set(path1))


#creating bokeh's GraphRenderer from Networkx graph
graph = from_networkx(G, layout_function=pos,center=(0,0))

#Finding x,y coordinates of shortest path that is given in path1 
pos_dict_1 = {}
pos_dict_2 = {}
pos_dict_3 = {}
for key,val in pos.items():
    if key in path1:
        pos_dict_1.setdefault(key,[]).append(val)
    if key in path2:
        pos_dict_2.setdefault(key,[]).append(val)
    if key in path3:
        pos_dict_3.setdefault(key,[]).append(val)

xvals_1 = []
yvals_1 = []   
xvals_2 = []
yvals_2 = []      
xvals_3 = []
yvals_3 = []

for i in path1:
    pos_tup = pos_dict_1[i][0]
    xvals_1.append(pos_tup[0])
    yvals_1.append(pos_tup[1])
    
for i in path2:
    pos_tup = pos_dict_2[i][0]
    xvals_2.append(pos_tup[0])
    yvals_2.append(pos_tup[1])

for i in path3:
    pos_tup = pos_dict_3[i][0]
    xvals_3.append(pos_tup[0])
    yvals_3.append(pos_tup[1])


# printing the nodes' names for path1
for i in range(len(path1)):
    plot.text(x=xvals_1[i]-0.18, y=yvals_1[i], text=[path1[i]], angle=1, text_alpha=1, text_font_size={'value': '10pt'})

# printing the nodes' names for path2 
path2_temp = []
for i in path2:
    if i not in path1:
        path2_temp.append(i)

for i in range(len(path2_temp)):
    path2_temp_pos_dict = {}
    for key,val in pos.items():
        if key in path2_temp:
            path2_temp_pos_dict.setdefault(key,[]).append(val)
    
    xvals_temp_2=[]
    yvals_temp_2=[]
    for j in path2_temp:
        pos_tup = path2_temp_pos_dict[j][0]
        xvals_temp_2.append(pos_tup[0])
        yvals_temp_2.append(pos_tup[1])

    plot.text(x=xvals_temp_2[i]-0.18, y=yvals_temp_2[i], text=[path2_temp[i]], angle=1, text_alpha=1, text_font_size={'value': '10pt'})

# printing the nodes' names for path1
path3_temp = []
for i in path3:
    if i not in path1 and i not in path2:
        path3_temp.append(i)

for i in range(len(path3_temp)):
    path3_temp_pos_dict = {}
    for key,val in pos.items():
        if key in path3_temp:
            path3_temp_pos_dict.setdefault(key,[]).append(val)
    
    xvals_temp_3=[]
    yvals_temp_3=[]
    for j in path3_temp:
        pos_tup = path3_temp_pos_dict[j][0]
        xvals_temp_3.append(pos_tup[0])
        yvals_temp_3.append(pos_tup[1])

    plot.text(x=xvals_temp_3[i]-0.18, y=yvals_temp_3[i], text=[path3_temp[i]], angle=1, text_alpha=1, text_font_size={'value': '10pt'})


#coloring the shortest paths nodes with help of x,y vals calculated above
# #path1
for i in range(len(xvals_1)):
    plot.circle(x=xvals_1[i],y=yvals_1[i],size=30, fill_color = 'red', legend_label='Optimal Path')
    
#path2
for i in range(len(xvals_2)):
    plot.circle(x=xvals_2[i],y=yvals_2[i],size=30,fill_color = 'green', legend_label='Path2')

#path3
for i in range(len(xvals_3)):
    plot.circle(x=xvals_3[i],y=yvals_3[i],size=30, fill_color='yellow', legend_label='Path3')

# #path2
# for i in range(len(xvals_2)):
#     plot.circle(x=xvals_2[i],y=yvals_2[i],size=30,fill_color = 'green')

# #path1
# for i in range(len(xvals_1)):
#     plot.circle(x=xvals_1[i],y=yvals_1[i],size=30, fill_color = 'red')

for i in range(len(xvals_1)-1):
    plot.add_layout(Arrow(end=NormalHead(size=10),x_start=xvals_1[i],
    y_start=yvals_1[i],x_end=xvals_1[i+1],y_end=yvalszoom_out,box_zoom", 
            toolbar_location="above")


#finding shortest paths
#best path
path1 = nx.shortest_path(G,source,destination,weight='weight',method='dijkstra')
#alternative paths
x = nx.shortest_simple_paths(G,source,destination)

all_pathsnodes = []
path2 = []
path3 = []
for i in range(2):
    all_pathsnodes.append(next(x))

#finding path 2
path2 = all_pathsnodes[0]
path2_edges = set(zip(path2,path2[1:]))

#finding path 3
path3 = all_pathsnodes[1]
path3_edges = set(zip(path3,path3[1:]))

path2_foredges = path2
path3_foredges = path3

# removing extra nodes from the lists of path2 & path3
path2 = list(set(path2) - set(path1))
path3 = list(set(path3) - set(path2) - set(path1))


#creating bokeh's GraphRenderer from Networkx graph
graph = from_networkx(G, layout_function=pos,center=(0,0))

#Finding x,y coordinates of shortest path that is given in path1 
pos_dict_1 = {}
pos_dict_2 = {}
pos_dict_3 = {}
for key,val in pos.items():
    if key in path1:
        pos_dict_1.setdefault(key,[]).append(val)
    if key in path2:
        pos_dict_2.setdefault(key,[]).append(val)
    if key in path3:
        pos_dict_3.setdefault(key,[]).append(val)

xvals_1 = []
yvals_1 = []   
xvals_2 = []
yvals_2 = []      
xvals_3 = []
yvals_3 = []

for i in path1:
    pos_tup = pos_dict_1[i][0]
    xvals_1.append(pos_tup[0])
    yvals_1.append(pos_tup[1])
    
for i in path2:
    pos_tup = pos_dict_2[i][0]
    xvals_2.append(pos_tup[0])
    yvals_2.append(pos_tup[1])

for i in path3:
    pos_tup = pos_dict_3[i][0]
    xvals_3.append(pos_tup[0])
    yvals_3.append(pos_tup[1])


# printing the nodes' names for path1
for i in range(len(path1)):
    plot.text(x=xvals_1[i]-0.18, y=yvals_1[i], text=[path1[i]], angle=1, text_alpha=1, text_font_size={'value': '10pt'})

# printing the nodes' names for path2 
path2_temp = []
for i in path2:
    if i not in path1:
        path2_temp.append(i)

for i in range(len(path2_temp)):
    path2_temp_pos_dict = {}
    for key,val in pos.items():
        if key in path2_temp:
            path2_temp_pos_dict.setdefault(key,[]).append(val)
    
    xvals_temp_2=[]
    yvals_temp_2=[]
    for j in path2_temp:
        pos_tup = path2_temp_pos_dict[j][0]
        xvals_temp_2.append(pos_tup[0])
        yvals_temp_2.append(pos_tup[1])

    plot.text(x=xvals_temp_2[i]-0.18, y=yvals_temp_2[i], text=[path2_temp[i]], angle=1, text_alpha=1, text_font_size={'