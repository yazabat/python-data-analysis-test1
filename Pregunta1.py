# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:12:23 2021

@author: LighthouseLLC
"""

import pandas as pd

acci=pd.read_csv(r'C:\Users\LighthouseLLC\Desktop\Econ\_UNI_Python\data\data\AccidentesAutos_USA.csv')

acci.info()



# %% Pregunta 1.1
# ==============================================================
#  calcule el tiempo que transcurre entre Start_Time y End_Time.
# ==============================================================
type(acci.Start_Time)



dir(acci.Start_Time)

help(acci.Start_Time.sample)


acci.columns

#Exploracion por  muestras de los datos

acci.Start_Time.sample(n=100)
acci.End_Time.sample(n=100)
#Muestra para dos columnas
acci[["Start_Time", "End_Time"]].sample(n=12)

#Transformacion de columnas tipo object (string) a datetime:
#df.COLUMNA = pd.to_datetime(df.COLUMNA)
acci.Start_Time = pd.to_datetime(acci.Start_Time)
acci.End_Time=pd.to_datetime(acci.End_Time)
acci.info()

acci['DeltaT']=acci.End_Time-acci.Start_Time
acci[["Start_Time","End_Time","DeltaT"]].sample(n=20)

#Info en horas
str(acci.DeltaT[0])[7:]

#Tipo de dato de delta T
type(acci.DeltaT)

deltattype = acci.dtypes["DeltaT"]
deltattype


acci.DeltaT.sample(10)

acci.DeltaT=acci.DeltaT.dt.seconds/(60*60)
acci.DeltaT.sample(10)

# %% Pregunta 1.2
# ==============================================================
#  Construya las columnas que almacenen la información de
#  Año, mes, dia y hora.
# ==============================================================
#Nuevas columnas para Start_Time
acci["Start_Time_YEAR"] = acci["Start_Time"].dt.year
acci["Start_Time_MONTH"] = acci["Start_Time"].dt.month
acci["Start_Time_DAY"] = acci["Start_Time"].dt.day
acci["Start_Time_HOUR"] = acci["Start_Time"].dt.strftime("%H:%M:%S")

acci[["Start_Time_YEAR","Start_Time_MONTH","Start_Time_HOUR"]].sample(n=10)

#Nuevas columnas para End_Time
acci["End_Time_YEAR"] = acci["End_Time"].dt.year
acci["End_Time_MONTH"] = acci["End_Time"].dt.month
acci["End_Time_DAY"] = acci["End_Time"].dt.day
acci["End_Time_HOUR"] = acci["End_Time"].dt.strftime("%H:%M:%S")

acci[['Start_Time_HOUR', 'End_Time_HOUR']].sample(n=10)
# %% Item 3: Estados con mayor cantidad de accidentes

dir(acci.State)
tenStates=acci.State.value_counts().head(10)
tenStates.index

# Nuevo dataframe para hacer el analisis descriptivo

accTenST=acci[acci.State.isin(tenStates.index)]
accTenST

#unique
import numpy as np
np.unique(accTenST.State)

import seaborn as sns
sns.barplot(data=accTenST, x="Distance(mi)", y="State")


# %% ITEM _  analisis descriptivo de la severidad de
#los accidentes ocurridos (variable Severity)

dir(acci.Timezone)
acci.Timezone.unique()
acci.Severity.unique()

"""
gb_acc=acci.groupby(by="Timezone")[["Severity"]].count()
res=gb_acc.reset_index()
plt.pie(x="Timezone", labels)

grouped=acci.groupby(['Timezone','Severity']).size()
grouped.plot.bar()

"""
grouped=acci.groupby(['Timezone','Severity']).size()
gb_pivot=grouped.pivot_table(index='Timezone', columns='Severity', aggfunc=np.count)
gb_pivot.plot.bar(figsize=(18,6))
plot.show
# %% ITEM 5

len(acci.Weather_Condition.unique())

FiveClimaCond=acci.Weather_Condition.value_counts().head(5)
accFiveWC=acci[acci.Weather_Condition.isin(FiveClimaCond.index)]



