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

# VISUEL 2

statuts = df_taches["Statut"].value_counts().reset_index()
statuts.columns = ["Statut", "Nombre de tâches"]

fig2 = px.pie(statuts, names="Statut", values="Nombre de tâches", title="Répartition des statuts des tâches")
fig2.show()

# VISUEL 3

df_merged = pd.merge(df_taches, df_emp, on="ID_Employé")

taches_par_dept = df_merged["Département"].value_counts().reset_index()
taches_par_dept.columns = ["Département", "Nombre de Tâches"]

fig3 = px.bar(taches_par_dept, x="Département", y="Nombre de Tâches", title="Nombre de tâches par département")
fig3.show()

# VISUEL 4

df_taches["Date de début"] = pd.to_datetime(df_taches["Date de début"])
df_taches["Date de fin"] = pd.to_datetime(df_taches["Date de fin"])

df_taches["Durée (jours)"] = (df_taches["Date de fin"] - df_taches["Date de début"]).dt.days

df_merged = pd.merge(df_taches, df_emp, on="ID_Employé")

duree_moyenne = df_merged.groupby("Nom")["Durée (jours)"].mean().reset_index()

fig4 = px.bar(duree_moyenne, x="Nom", y="Durée (jours)", title="Durée moyenne des tâches par employé")
fig4.show()
