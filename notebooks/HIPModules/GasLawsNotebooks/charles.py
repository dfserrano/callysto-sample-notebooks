def graph(ave_volume):
    # Imports, borrowing code from a 'library' that is used to generate the graph.
    import plotly.offline as py
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    import numpy as np
    import random
    from numpy import random as rand
    
    # Initialize data sets. This makes sure it does not graph old data from previous experiments.
    volumes = []
    temps = []
    trials = []
    tests = []
    
    for i in range(10):
        
        yielded = random.uniform((ave_volume-(rand.random_sample()*10)), (ave_volume+rand.random_sample()*10))

        # Rounds value to 2 decimal places before adding it to the list of data.
        volume = round(yielded, 2)
        volumes.append(volume)

        # Constant multiple in Charles' Law.
        kC = 0.56

        # Charles' Law is technically V/T = k, where k is constant for that specific system, (It varies between systems.)
        # and V1/T1 V2/T2 is only a result of this relationship. Students do not need to learn this however.
        # k is just arbitrarily set.

        # Adds value to list of data. 
        temp = kC*volume

        temps.append(temp)

        tests.append((volume, temp))

        # Labels trials according to how many values are in the list of data
        if len(volumes) > len(trials):
            trials.append('Trial ' + str(len(volumes)))
    
    init_notebook_mode(connected=True)

    # Generates volume bars.
    trace1 = go.Bar(
        x=trials,
        y=volumes,
        name='Volume'
    )

    # Generates temperature bars.
    trace2 = go.Bar(
        x=trials,
        y=temps,
        name='Temperature'
    )

    # Gives graph grouped-bars layout.
    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group',
        title='Volume vs. Temperature'
    )

    # Renders graph.
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='grouped-bar')