# -*- coding: utf-8 -*-
"""dataScienceAula01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RgR6llsJAmYYNm0p4AuxtrrXnywZtB8H
"""

import pandas as pd

notas = pd.read_csv("ratings.csv")

notas.columns = ["usuarioId", "filmeId", "nota", "momentos"]

notas.nota.plot(kind="hist")

notas.nota.describe()

import seaborn as sns

sns.boxplot(notas.nota)
