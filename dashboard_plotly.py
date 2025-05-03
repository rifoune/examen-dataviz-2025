import pandas as pd
import plotly.express as px

df_emp = pd.read_csv("Employés.csv")
df_taches = pd.read_csv("Tâches.csv")
print(df_emp.head())
print(df_taches.head())

df_merged = pd.merge(df_taches, df_emp, on='ID_Employé')

taches_par_employe = df_merged['Nom'].value_counts().reset_index()
taches_par_employe.columns = ['Employé', 'Nombre de Tâches']

fig = px.bar(taches_par_employe, x='Employé', y='Nombre de Tâches', title='Nombre de tâches par employé')
fig.show()
