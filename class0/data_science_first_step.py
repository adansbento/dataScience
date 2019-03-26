# -*- coding: utf-8 -*-
"""Data Science first step.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16cL85uj1Li0bNam-N2euufUImv4pwuCE
"""

import pandas as pd

notas = pd.read_csv("ratings.csv")

notas.head()

notas.shape

notas.columns = ["usuarioId", "filmeId", "notas", "momentos"]

notas.head()

notas['notas'].unique()

notas['notas'].value_counts()

notas['notas'].mean()