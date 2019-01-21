#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel("data\mydt.xlsx")
df=pd.read_excel("data\data2.xlsx")
data.tail(10)


# In[2]:


listcolumns=list(data.columns)
listm=listcolumns[3:10]
listm
datam=data[listm]

datam=datam.replace('ABS',0)
data['moyenne']=datam.mean(axis=1)
data['valider']='oui'
a,x=0,0
for i in range(154):
    if data.loc[i,'moyenne']<10:
        data.at[i,'valider']='non'
        a+=1
    if 'ABS' in list(data.loc[i,:]):
        data.at[i,'valider']='ABS'
        x+=1

data['redoublant']='non'
for i in range(154):
    if data.loc[i,'CNE'] in list(df['CNE']):
        data.at[i,'redoublant']='oui'
data.head()        

          


# In[3]:


b=154-a

labels=["non_valider","valider",'ABS']
values=[a,b,x]
explode=(0, 0.15,0.15)
colors=['pink','deeppink','skyblue']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')

plt.savefig('PieChart01.png')

plt.show()


# In[4]:


m=0

df=pd.read_excel("data\mydt.xlsx")
for i in range(154):
    if df.loc[i,'sexe']=='M':
        m+=1
f=154-m        
labels=["Mr","Mss"]
values=[m,f]
explode=(0, 0.15)
colors=['skyblue','pink']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=80)
plt.axis('equal')

plt.savefig('PieChart01.png')

plt.show()        


# In[5]:


v=0

for i in range(154):
    if df.loc[i,'sexe']=='M' and data.loc[i,'valider']=='oui':
        v+=1

w=b-v
nvf=f-w

plt.title('le pourcentage des Mss validont le semestre 1')        
labels=["Mss validé","Mss non validé"]
values=[w,nvf]
explode=(0, 0.15)
colors=['skyblue','pink']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=80)
plt.axis('equal')

plt.savefig('PieChart01.png')

print(plt.show())
nvm=m-v
plt.title('le pourcentage des Mrs validont le semestre 1')        
labels=["Mrs validé","Mrs non validé"]
values=[v,nvm]
explode=(0, 0.15)
colors=['pink','skyblue']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=80)
plt.axis('equal')

plt.savefig('PieChart01.png')

print(plt.show()) 

               
        
        


# In[6]:



t=0
o=0
s=0
e=0
for i in range(154):
    if type(data.loc[i,'CNE']) is str:
        if data.loc[i,'CNE'][0]=='S':
            data.at[i,'region']='TAZA'
            t+=1
        if data.loc[i,'CNE'][0]=='Z':
            data.at[i,'region']='OUJDA'
            o+=1
        if data.loc[i,'CNE'][0]=='C':
            data.at[i,'region']='elhouceima' 
            e+=1
    elif type(data.loc[i,'CNE']) is int:
        data.at[i,'region']='sefrou'
        s+=1

labels=["TAZA","OUJDA","ELHOUCEIMA","SEFROU"]
values=[t,o,e,s]
explode=(0.1, 0.1,0.2,0.1)
colors=['pink','deeppink','skyblue','black']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')

plt.savefig('PieChart01.png')

plt.show()
data.head()          
        


# In[7]:


d=datam.T       
d['moyenne-classe']=datam.mean(axis=0)
dft=d.T
            


# In[8]:



data1=data.sort_values('moyenne', ascending=False).head(10)
data1.index=range(10)
data1


# In[9]:


t=0
for i in range(10):
    if data1.loc[i,'redoublant']=='non':
        t+=1

plt.title('les dix premier majorants')        
labels=["redoublant","non-doublant"]
values=[t,10-t]
explode=(0, 0.15)
colors=['pink','skyblue']
plt.pie(values,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=80)
plt.axis('equal')

plt.savefig('PieChart01.png')

print(plt.show()) 
    
    


# In[10]:


nom_prenom=str(input("entrer nom et prenom"))
c=nom_prenom.split()
nom_=c[0]
prenom_=c[1]


# In[11]:


N=[]
for i in data.NOM:
    N.append(i)
P =[] 
for i in data.Prénom:
    P.append(i)
   
if nom_ in N and prenom_ in P:
    indice=N.index(nom_)
    data.loc[indice,:]    
data['moyenne']=data.mean(axis=1)
data['valider']='oui'
for i in range(154):
    if data.loc[i,'moyenne']<10:
        data.at[i,'valider']='non'
if data.loc[indice,'valider']=='oui':
    print(nom_,prenom_,'est valider')
else:
    print(nom_,prenom_,'est non valider')

if (datam.loc[indice,'analyse1']+datam.loc[indice,'algebre1']+datam.loc[indice,'algebre2'])/3> (datam.loc[indice,'physique1']+datam.loc[indice,'physique2'])/2:
    print('il a une orientation mathematique plus que physique en génerale ')
    if (datam.loc[indice,'analyse1']+datam.loc[indice,'algebre1']+datam.loc[indice,'algebre2'])/3<8:
        print("mais c'est loin de la barre pour valider")
    elif (datam.loc[indice,'analyse1']+datam.loc[indice,'algebre1']+datam.loc[indice,'algebre2'])>=8 or (datam.loc[indice,'analyse1']+datam.loc[indice,'algebre1']+data.loc[indice,'algebre2'])<10:
        print("besoin juste d un peut d'effort pour valider le module de math")
    else:
        print("le module de mathematique est validé avec succé")
        
else:
    print('il a une orientation physique plus que mathematique en génerale ')
    if (datam.loc[indice,'physique1']+datam.loc[indice,'physique2'])/2<8:
        print("mais c'est loin de la barre pour valider")
    elif (datam.loc[indice,'physique1']+datam.loc[indice,'physique2'])/2>=8 or (datam.loc[indice,'physique1']+datam.loc[indice,'physique2'])/2<10:
        print("besoin juste d un peut d'effort pour valider le module de physique")
    else:
        print("le module de physique est validé avec succé")    
        
        
    
if nom_ in N and prenom_ in P:
    indice=N.index(nom_)
fg=data.loc[indice,:]
datap=pd.concat([fg],axis=1)
dtp=datap.T
dtp    


# In[ ]:





# In[ ]:


# 

