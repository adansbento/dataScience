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

Seaborn<b>boxplot(notas.nota)</b>:
<br>Show summary with details ex: means,min,max 25%,50%,75% the dataFr
Seaborn's Command:<br>
ame visually

# Class 2.1

Command:

<b>rating.query("movieId==1")</b>:<br>
search by movieId

<b>rating.groupby("movieId")</b>:<br>
Group by movieId

<b>medias_por_filme.plot(kind="hist")</b>:<br>
Show the histogram according collection
<br>

Seaborn's Command:<br>

<b>sns.distplot(medias_por_filme)</b>:<br>
Show summary details ex: means,min,max 25%,50%,75% on the chart

# Class 3

## Variables can be classified as follows:

- Quantitative Variables:
 are the characteristics that can be measured on a quantitative scale, that is, they have numerical values ​​that make sense. They can be continuous or discrete.

- Discrete variables:
 measurable characteristics that can take on only a finite or infinite number of values ​​and thus only make whole values ​​meaningful. They are usually the result of counts. Examples: number of children, number of bacteria per liter of milk, number of cigarettes smoked per day.

- Continuous variables, measurable characteristics that take values ​​on a continuous scale (on the real line), for which fractional values ​​make sense. Usually they should be measured by some instrument. Examples: weight (balance), height (ruler), time (clock), blood pressure, age.

- Qualitative (or categorical) variables:
 these are the characteristics that do not have quantitative values, but, instead, are defined by several categories, that is, they represent a classification of individuals. They can be nominal or ordinal.

- Nominal variables: 
there is no ordering among categories. Examples: sex, eye color, smoker / non-smoker, sick / healthy.

- Ordinal variables: 
there is an ordering between categories. Examples: schooling (1st, 2nd, 3rd grades), stage of illness (initial, intermediate, terminal), month of observation (January, February, ..., December).


# Class 4

## Seaborn's commad

- Load file tmdb:<br>
tmdb = pd.read_csv("tmdb_5000_movies.csv")
<br>

- Print first 5 lines:<br>
tmdb.head()
<br>

- Count each original_language:<br>
tmdb["original_language"].value_counts()<br>

- Reset index hide column "index" and show amount:<br>
amount_language = tmdb["original_language"].value_counts().to_frame().reset_index()<br>
amount_language.columns = ["original_linguage","total"]<br>
amount_language.head()<br>

- Show graphics with barplot:<br>
sns.barplot(x="original_linguage", y="total", data=amount_language)<br>

- Show graphics with catplot **It is works with version more than 0.9.0:<br>
!pip install seaborn==0.9.0<br>
import seaborn as sns<br>
sns.catplot(x="original_language", kind="count", data = tmdb<br>