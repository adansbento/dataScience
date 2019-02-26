# Data Science

This git was created with the intention of following the course
https://www.alura.com.br/formacao-data-science

 # Tools Python
- NumPy
- Pandas
- Seaborn (preview)
- Matplotlib 

**note** :
 code was made in the https://colab.research.google.com

# Class 1

Panda's Command:
 
- <b>head()</b>:<br>
returns the previous 5 items in the list
 
- <b>list.shape</b>:<br>
 Return a tuple representing the dimensionality of the DataFrame.<br>
 <b>note:</b>used for list `shape`,  number of itens and columns.
 
 - <b>list['column'].unique()</b>: <br>
 Return values unique the series 'list'.

 - <b>notas.columns = ["usuarioId", "filmeId", "nota", "momentos"]</b>:<br>
  Change the names of columns.

 - <b>notas['notas'].value_counts()</b>:
 Returns object containing counts of unique values.


# Class 2

Panda's Command:

<b>sns.notas.nota.plot(kind="hist")</b>:<br>
Show to histogram the dataFrame

<b>notas.nota.describe()</b>:<br>
Show summary with details ex: means,min,max 25%,50%,75% the dataFrame

Seaborn's Command:<br>
import seaborn as sns

<b>boxplot(notas.nota)</b>:
<br>Show summary with details ex: means,min,max 25%,50%,75% the dataFrame visually
