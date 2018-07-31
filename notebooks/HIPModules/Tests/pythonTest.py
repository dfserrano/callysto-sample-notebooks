
import  plotly.plotlyplotly.p  as py
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("testChart.csv")

table = ff.create_table(df)
py.iplot(table, filename='tableTest')