import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    ### Create figure
    fig, ax = plt.subplots()
    ### Plot scatter data
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    ### Set x axis limits to include past 2050
    ax.set_xlim([1850, 2075])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    ### Get list of x values 
    x = np.arange(1880, 2051, 1)
    ### Plot line using y = mx+b
    ax.plot(x, result.slope * x + result.intercept)

    # Create second line of best fit
    adjust_result = linregress(df.loc[df["Year"] >= 2000]["Year"], df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    ### Get list of x values 
    x2 = np.arange(2000, 2051,1)
    ### Plot line using y=mx+b
    ax.plot(x2, adjust_result.slope * x2 + adjust_result.intercept)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()