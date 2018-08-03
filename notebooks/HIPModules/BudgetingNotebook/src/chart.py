def pie():
    # Import statments.
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    init_notebook_mode(connected=True)

    # Generate graph.
    labels = ['Rent and Utilities', 'Food', 'Savings', 'Spending Money', 'Other (Clothing, Gym Membership, etc)']
    values = [35, 15, 20, 15, 15] # Percentage distribution.
    trace = go.Pie(labels=labels, values=values)
    layout = go.Layout(title='Example Budget in Percentages')
    iplot(go.Figure(data=[trace], layout=layout), filename='piechart')
    
def bar():
    # Import statments.
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    init_notebook_mode(connected=True)

    # Generate graph.
    x = ['Rent and Utilities', 'Food', 'Savings', 'Spending Money', 'Other']
    y = [2000, 250, 400, 200, 350]
    data = [go.Bar(x=x, y=y)]
    layout = go.Layout(title='Budget Assuming $3200 in Total Income')
    iplot(go.Figure(data=data, layout=layout), filename='barchart')
    
def graphing(total, rent, utilities, savings, food, spending_money, clothes, other):
    # Import statments.
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    init_notebook_mode(connected=True)
    
    # Generate pie graph.
    labels = ['Rent', 'Utilities', 'Savings', 'Food', 'Spending Money', 'Clothes', 'Other']
    values = [rent, utilities, savings, food, spending_money, clothes, other] # Percentage distribution.
    trace = go.Pie(labels=labels, values=values)
    layout = go.Layout(title='Your Budget in Percentages')
    iplot(go.Figure(data=[trace], layout=layout), filename='yourpiechart')
    
    # Generate bar graph.
    x = ['Rent', 'Utilities', 'Savings', 'Food', 'Spending Money', 'Clothes', 'Other']
    y = [rent*total, utilities*total, savings*total, food*total, spending_money*total, clothes*total, other*total]
    data = [go.Bar(x=x, y=y)]
    layout = go.Layout(title='Your Budget in Dollars')
    iplot(go.Figure(data=data, layout=layout), filename='youtbarchart')
