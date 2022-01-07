from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def _help():
    print("List of commands:\n"
    "\n"
    "connect\n"
    "\n"
    "missing - requires data\n"
    "\n"
    "dataframe - requires data\n"
    "\n"
    "drop_specific_rows - requires data, column name, value in column you wish to drop\n"
    "\n"
    "simple_plot - requires x, y, title, colour, x_label, y_label\n"
    "\n"
    "plt_scatter - requires  x, y, title, colour, x_label, y_label\n"
    "\n"
    "normalise - requires data")

def connect():
    print('Cleaner module successfully connected...')

def missing(data):
    print ("Number of missing values is:\n",data.isnull().sum(),"Length of dataset is:", len(data),"\n")
    
def dataframe(data):
    df = pd.DataFrame(data)
    return df

def drop_specific_rows(data, data_column, value):
    dropped = data.drop(data.loc[data_column == value].index)
    return dropped

def simple_plot(data_1, data_2, title, color, x_label, y_label):
    plt.plot(data_1, data_2, fmt = color, linestyle= 'solid', marker = None)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
        
def plt_scatter(data_1, data_2, title, color, x_label, y_label):
    plt.scatter(data_1, data_2, fmt = color,)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
def normalise(data):
    norm = (data-data.min())/(data.max()-data.min())
    return norm


