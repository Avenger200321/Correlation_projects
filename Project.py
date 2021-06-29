import csv
from numpy.lib import corrcoef
import plotly.express as px
import numpy as np

def draw_graph():
    with open('Prodata.csv') as f :
        df = csv.DictReader(f)
        graph = px.scatter(df,x ='days', y = 'marks')
        graph.show()
def get_data(data_path):
    marks =[]
    days =[]
    with open('Prodata.csv')as f:
        df = csv.DictReader(f)
        for i in df:
            marks.append(float(i['marks']))
            days.append(float(i['days']))
    return {
        'x' : days ,
        'y' : marks
    }
def find_correlation(data_source):
    cor = np.corrcoef(data_source['x'],data_source['y'])
    print(cor[0,1])
def setup():
    data_path ='./Prodata.csv'
    data_source = get_data(data_path)
    find_correlation(data_source)
    draw_graph()
setup()