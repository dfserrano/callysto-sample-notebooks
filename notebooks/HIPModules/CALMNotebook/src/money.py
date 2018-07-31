def graph():
    # Imports, borrowing code from a 'library' that is used to generate the graph.
    import plotly.offline as py
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    import numpy as np
    import random
    from numpy import random as rand
    import pandas as pd
    
    # Initalizes data sets.
    months = []
    costSmoke = []
    costDrink = []
    rent = []
    
    # Generates data for 12 months.
    for i in range(12):
        months.append(i+1)
    for i in months:
        costSmoke.append(i*21.3*6.25)
        costDrink.append(i*4*200)
        rent.append(1190)
    
    # Plots data in graph.
    trace1 = go.Scatter(
        x = months,
        y = costSmoke,
        mode = 'lines+markers',
        name = 'Cigarettes'
    )

    trace2 = go.Scatter(
        x = months,
        y = rent,
        mode = 'lines+markers',
        name = 'Rent'
    )

    trace3 = go.Scatter(
        x = months,
        y = costDrink,
        mode = 'lines+markers',
        name = 'Alcohol'
    )

    data = [trace1, trace2, trace3]
    layout = go.Layout(title='Cost of Cigarettes Over a Year vs. Cost of Rent Each Month', xaxis=dict(title='Months'), yaxis=dict(title='Cost in Dollars'))
    fig = go.Figure(data = data, layout = layout)
    py.iplot(fig, filename='line-mode')