# -*- coding: utf-8 -*-
"""Copy of dataScienceAula03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vUPiGDfNuf0VrydXSFEdshK9yNRASyf7
"""



"""# New Section"""

!pip install seaborn==0.9.0

import pandas as pd
import seaborn as sns

print(sns.__version__)

tmdb = pd.read_csv("tmdb_5000_movies.csv")

tmdb.head()

tmdb["original_language"].value_counts()

amount_language = tmdb["original_language"].value_counts().to_frame().reset_index()
amount_language.columns = ["original_linguage","total"]
amount_language.head()

sns.barplot(x="original_linguage", y="total", data=amount_language)

sns.catplot(x="original_language", kind="count", data = tmdb)