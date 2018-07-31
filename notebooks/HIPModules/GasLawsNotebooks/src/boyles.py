# Boyle's Law simulation code.

def graph(N, volume):
    # Imports, borrowing code from a 'library' that is used to generate the graph.
    import plotly.offline as py
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    import numpy as np
    from numpy import random as rand
    import math
    init_notebook_mode(connected=True)

    # Initialize data sets. This makes sure it does not graph old data from previous experiments.
    trials = []
    gx = []
    gy = []

    # Constant multiple in Boyle's Law.
    kB = 1

    # Boyle's Law is technically PV = k, where k is constant for that specific system, (It varies between systems.)
    # and P1V1 = P2V2 is only a result of this relationship. Students do not need to learn this however.
    # For simplicity k is set to 1.

    # Randomly generate data based on user defined volume and number of trials.
    for i in range(0, N):
        temp = rand.random_sample() * volume

        # Prevent large outliers.
        # The limit is arbitrary, it is just so the graph looks nice and so the relationship is clearly defined.
        limit = rand.random_sample() + 1
        while(kB/temp > volume/limit):
            temp = rand.random_sample() * volume

        # Adds noise to points.
        outputx = rand.uniform(temp-(rand.random_sample()/4), temp+(rand.random_sample()/4))
        outputy = rand.uniform((kB/temp)-(rand.random_sample()/4), (kB/temp)+(rand.random_sample()/4))

        # Add the values to the list of data.
        trials.append((outputx, outputy))
        gx.append(outputx)
        gy.append(outputy)

    # Organizes data.
    trace = go.Scatter(x=gx, y=gy, mode='markers')

    # Labels graph.
    templayout = go.Layout(title='Pressure vs. Volume', xaxis=dict(title='Volume'), yaxis=dict(title='Pressure'))

    # Renders graph. 
    tempdata = [trace]
    fig = go.Figure(data=tempdata, layout=templayout)
    py.iplot(fig, filename='scatter-plot')
    
    # Return list of data for the table.
    return trials