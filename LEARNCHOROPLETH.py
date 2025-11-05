import json
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
indian_state=json.load(open(r"C:\Users\VISHAL RAJ\OneDrive\Pictures\NOBEL PROJECT\idianstates.json",'r',encoding='utf-8'))
print(indian_state['features'][1])
df=pd.read_csv(r"C:\Users\VISHAL RAJ\OneDrive\Pictures\NOBEL PROJECT\india_states_ut_2020.csv")
#print(df)
df['Name'] = df['Name'].replace('Odisha', 'Orissa')
df['Name'] = df['Name'].replace('Uttarakhand', 'Uttaranchal')
df['Name'] = df['Name'].replace('Andaman & Nicobar Islands', 'Andaman and Nicobar')
df['Name'] = df['Name'].replace('Dadra and Nagar Haveli and Daman and Diu', 'Dādra and Nagar Haveli and Damān and Diu')
state_id_map={}
for feature in indian_state['features']:
    feature['id']=feature['properties']['id']
    state_id_map[feature['properties']['name']]=feature['id']
print(df)
print(state_id_map)
df['id']=df['Name'].apply(lambda x:state_id_map[x])
print(df)
df['DensityScale']=np.log10(df['Density'])
'''
location=It will be name of the column whose value will be used to map with the feature id.
color=Name of the column which will be used for the coloring.
'''
img=px.choropleth(df,
                  locations='id',
                  geojson=indian_state,
                  color='DensityScale',
                  hover_name='Name',
                  hover_data=['Density'])
img.update_geos(fitbounds="locations", visible=False)
img.show()




















