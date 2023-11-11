import pandas as pd
import numpy as np
import re

df = pd.read_csv('/home/jordina/Desktop/datathon/dades1.csv')
df2 = pd.read_csv('/home/jordina/Desktop/datathon/dades2.csv')

diccionari = {"Underground": 1, "FGC": 1, "Taxi": 2, "Tram": 1, "Electric motorcycle": 2, "Combustion or electric motorcycle with non-renewable source charging": 2, "Scooter (or other micro-mobility devices) with renewable charging": 2, "Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable source charging),": 2, "Electric vehicle (with Zero label and renewable source charging)": 2, "On foot": 0, "Renfe": 1, "Bus": 1, "Bicycle": 0, "Scooter (or other micro-mobility devices) with non-renewable charging": 2}

transports1 = []
for i in range(3):
    transports1.append("Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage " + str(i+1) + "]")
    transports1.append("Indicate the modes of transport you use to return from the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage " + str(i+1) + "]")

dfn = df
dfn = dfn.fillna('DATATHON')
dfn['MitjaPersones'] = '-1'

for indx, row in dfn.iterrows():
    sumaTotal = 0
    suma1 = 0
    cnt1 = 0

    for i in range(3):
        if(row[transports1[2*i]] != 'DATATHON'):
            cnt1 += 1
            suma1 += diccionari[row[transports1[2*i]]]
    
    cntTotal = 0

    if(cnt1 != 0):
        mitja_1 = float(suma1)/float(cnt1)
        sumaTotal += mitja_1
        cntTotal += 1

    suma2 = 0
    cnt2 = 0
    for i in range(3):
        if(row[transports1[2*i+1]] != 'DATATHON'):
            cnt2 += 1
            suma2 += diccionari[row[transports1[2*i+1]]]

    if (cnt2 != 0):
        mitja_2 = float(suma2)/float(cnt2)
        sumaTotal += mitja_2
        cntTotal += 1

    if cntTotal != 0:
        mitja_Total = float(sumaTotal)/float(cntTotal)
        dfn.iloc[indx, -1] = mitja_Total
    else:
        dfn.iloc[indx, -1] = np.nan

dfn["MitjaPersones"] = dfn["MitjaPersones"].dropna()
df2 = dfn

dfn = dfn.loc[dfn["MitjaPersones"] > 1.0]
df2 = df2.loc[df2["MitjaPersones"] <= 1.0]


nom_columnes = ["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the fastest]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the cheapest]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the most comfortable]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the only option]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It has a lower environmental impact]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the healthiest]", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [I need the private vehicle for other trips]"]
for i in range(len(nom_columnes)):
    dfn[nom_columnes[i]] = dfn[nom_columnes[i]].map({'Yes': 1, 'No': 0})
    df2[nom_columnes[i]] = df2[nom_columnes[i]].map({'Yes': 1, 'No': 0})


out = dfn.groupby('Select the center where you study:', as_index = False, sort = False).agg({"Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the fastest]": 'mean', "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the cheapest]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the most comfortable]":"mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the only option]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It has a lower environmental impact]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the healthiest]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [I need the private vehicle for other trips]": "mean", "MitjaPersones": "mean"}).round(4)
out2 = df2.groupby('Select the center where you study:', as_index = False, sort = False).agg({"Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the fastest]": 'mean', "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the cheapest]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the most comfortable]":"mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the only option]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It has a lower environmental impact]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the healthiest]": "mean", "Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [I need the private vehicle for other trips]": "mean", "MitjaPersones": "mean"}).round(4)

for indx,row in out.iterrows():
    s = row[0]
    ss = str(re.findall(r'\((.*?)\)', s))
    out.iloc[indx, 0] = ss[1:-1]

for indx,row in out2.iterrows():
    s = row[0]
    ss = str(re.findall(r'\((.*?)\)', s))
    out2.iloc[indx, 0] = ss[1:-1]


# tipus_transport = set([])

# for indx, row in df.iterrows():
#     for i in range(6):
#         tipus_transport.add(row[transports1[i]])


# print(len(tipus_transport))
# print(dfn["MitjaPersones"])
dfn.to_csv('out.csv')
out.to_csv('outpriv.csv')
out2.to_csv('outpub.csv')