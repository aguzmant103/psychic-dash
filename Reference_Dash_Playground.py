#Import Section
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd




#Opening Dash container
app = dash.Dash()

#Constants declaration
markdown_title = '''
    # Costa Rica Arbitration Control
    A look at 1990-2020 arbitration cases
    '''
markdown_section1 = '''
    ### The following is a table that comprises Costa Rican arbitration demands from 1990 to 2020
    '''
colors = {
    'background': '#111111',
    'text': '#000000'}

#Loading my data in a dataframe
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw')
#Defines function to generate a Dash table from a Pandas' dataframe
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


#App Layout defines the objects that are present in the web application.

app.layout = html.Div([
    dcc.Markdown(
        children=markdown_title,
        style={'textAlign': 'center','color': colors['text'], 'font_size' : '50px'}),
    html.H4(children='Costa Rican Arbitration Cases (1990-2020)'),
    generate_table(df),    
    dcc.Markdown(children=markdown_section1),
    html.Label(' '),
    html.Label('Dispute Type (Single-Select Dropdown)'),   
    dcc.Dropdown(
        options=[
            {'label': 'Regulatory', 'value': 'RG'},
            {'label': 'Environmental', 'value': 'ENV'},
            {'label': 'Breach Contract', 'value': 'BCH'}
        ],
        value='ENV'),
    html.Label('Industries Involved (Multi-Select Dropdown)'),
    dcc.Dropdown(
        options=[
            {'label': 'Fishing and Farming', 'value': 'F&F'},
            {'label': u'Life Sciences', 'value': 'LS'},
            {'label': 'Health', 'value': 'HLT'},
            {'label': 'Mining', 'value': 'MN'},
            {'label': 'Telecommunications', 'value': 'TEL'},
            {'label': 'Oil and Gas', 'value': 'PET'}
        ],
        value=['F&F', 'TEL'],
        multi=True),
    html.Label('Type of Arbitrage'),
    dcc.RadioItems(
        options=[
            {'label': 'Commercial', 'value': 'COM'},
            {'label': u'Investment', 'value': 'INV'}
        ],
        value='COM'),
    html.Label('Provinces'),
    dcc.Checklist(
        options=[
            {'label': 'San Jose', 'value': 'SJ'},
            {'label': 'Cartago', 'value': 'CAR'},
            {'label': 'Heredia', 'value': 'HER'},
            {'label': 'Alajuela', 'value': 'ALA'},
            {'label': 'Puntarenas', 'value': 'PUN'},
            {'label': 'Guanacaste', 'value': 'GUA'},
            {'label': 'Limon', 'value': 'LIM'},
        ],
        value=['SJ', 'CAR','HER','ALA','PUN','GUA','LIM']),
    html.Label('Text Box'),
    dcc.Input(value='Example Text', type='text'),
    dcc.RangeSlider(
        id='year-slider',
        min=1990,
        max=2020,
        step=1,
        value=[1990,2010],
        marks={
            1990: '1990',
            1995: '1995',
            2000: '2000',
            2005: '2005',
            2010: '2010',
            2015: '2015',
            2020: '2020'}),
    html.Div(id='slider-output-container')
    ])


#This section specifies the responsiveness of the application.
@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_output(value):
    return 'Return all values before year "{}"'.format(value)

#Start the application (debug or not)
if __name__ == '__main__':
    app.run_server(debug=True)