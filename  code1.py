import csv
import pandas as pd
import ploty.graph_objects as go

df = pd.read_csv("sportsData.csv")
print(df.groupby("Sports")["Distance"].mean())

fig = go.Figure(go.Bar(x = df.groupby("Sports")["Distance"].mean(), y = ["Basketball", "Tennis", "Hockey", "FootBall", "Cricket", "Baseball"], orientation = "h"))

fig.show()
