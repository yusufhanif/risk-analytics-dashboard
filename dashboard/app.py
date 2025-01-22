from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('/data/gapminder_unfiltered.csv')

# initializing the app
app = Dash()

app.layout = []

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

