def graph():
    # Imports, borrowing code from a 'library' that is used to generate the graph.
    import plotly.offline as py
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    import numpy as np
    import random
    from numpy import random as rand
    import pandas as pd
    
    init_notebook_mode(connected=True)
    
    # Accesses data file.
    df = pd.read_csv('src/affectsofsubstanceabuse.csv')
    
    # Initalizes data sets.
    total = []
    influence = []
    none = []
    
    # Calculates difference between total crash deaths and deaths involving substance abuse.
    for i in df['Total # of Crash Deaths']:
        total.append(i);
    for i in df['# of Fatalities Involving Drugs Alone or Drugs and Alcohol']:
        influence.append(i)
    for i in range(14):
        none.append(total[i] - influence[i])

    # Plots data in graph.
    trace1 = go.Bar(
        x = df['Location'],
        y = none,
        name = 'Accidents w/o Drugs or Alcohol'
    )
    trace2 = go.Bar(
        x = df['Location'],
        y = influence,
        name = 'Accidents w/ Drugs and/or Alcohol'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='stack',
        title = 'Crash Fatalities vs. Drugs and/or Alcohol Consumption'
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='stacked-bar')