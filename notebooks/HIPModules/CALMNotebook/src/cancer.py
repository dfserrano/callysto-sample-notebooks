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
    
    # Data to be graphed.
    labels = ['Carcinogenic to Humans', 'Probably Cacinogenic to Humans', 'Possibly Carcinogenic to Humans']
    values = [9, 1, 4]
    
    # Graphs data.
    trace = go.Pie(labels=labels, values=values)
    py.iplot([trace], filename='basic_pie_chart')