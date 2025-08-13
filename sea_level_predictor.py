import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = res_all.slope
    intercept_all = res_all.intercept

    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = slope_all * x_pred_all + intercept_all

    plt.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (All Data)')

    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = res_recent.slope
    intercept_recent = res_recent.intercept

    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent

    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit Line (Since 2000)')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
