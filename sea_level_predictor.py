import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig = plt.figure()
    plt.scatter(x=df.Year,y=df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")
    plt.grid()


    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line1=np.arange(df["Year"].min(),2051)
    predict=slope1*line1+intercept1
    plt.plot(line1,predict,color="crimson")


    # Create second line of best fit
    current=df[df["Year"]>=2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(current['Year'], current['CSIRO Adjusted Sea Level'])
    line2=np.arange(2000,2051)
    predict2=slope2*line2+intercept2
    plt.plot(line2,predict2,color="green")


    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
