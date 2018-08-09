def graph():
    # Imports, borrowing code from a 'library' that is used to generate the graph.
    import plotly.offline as py
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    import numpy as np
    from numpy import random as rand
    import math

    init_notebook_mode(connected=True)

    # Initializes data sets.
    ages = []
    heights = []

    # Generates data set.
    for i in range(30):
        ages.append(rand.uniform(3.0, 3.9)) 
        heights.append(rand.uniform(94-rand.random_sample(), 94+rand.random_sample()))

    # Sorts data set from least to greatest.
    ages.sort()
    heights.sort()

    # Generates graph.
    trace = go.Scatter(
        x = ages,
        y = heights,
        mode = 'markers', 
        name = "Age vs. Height"
    )

    data = [trace]
    py.iplot(data, filename='scatter-mode')