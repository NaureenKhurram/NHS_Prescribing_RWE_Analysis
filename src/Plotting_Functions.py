# PLOTTING FUNCTIONS 

"""
Reusable plotting functions for NHS Prescription Cost Analysis project.

Functions include:
- Bar charts
- Horizontal bar charts
- Line charts
- Boxplots
- Histogram
- Stacked bar charts

"""

# import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np

# function to plot a bar graph

def plot_bar(df, 
             title, 
             ylabel,
             xlabel = "",
             figsize=(10,5),
             rotation = 0):
	
    # define the figsize
    plt.figure(figsize=figsize)
    	
    bars = plt.bar(df.index, df.values, color="orange")
    		
    	# set labels and title
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=rotation)
    
    plt.tight_layout()
    plt.show()


# function to plot a horizontal bar graph
def plot_barh(
            df, 
            category_col,
            value_col,
            title, 
            ylabel,
            xlabel,
            isCurrency = False,
            label_currency = "M",
            figsize=(12,10),
            extra_label=""):
	
   # plotting the data
    fig, ax = plt.subplots(figsize=figsize)
    
    # setting the bar labels
    if extra_label:
        y_label = df[category_col] + "\n(" + df[extra_label] + ")"
        bars = ax.barh(y_label, df[value_col])
    else:
        bars = ax.barh(df[category_col], df[value_col])


    ax.invert_yaxis()

    if (label_currency == "S"):

        if isCurrency:
            labels = [ f"£{x/1:.1f}" for x in df[value_col]]
        else:
            labels = [ f"{x/1:.1f}" for x in df[value_col]]

    else:
        # adding data labels
        if label_currency == "M":
            
            divisor = 1_000_000
            suffix = "M"
    
        elif label_currency == "B":
            
            divisor = 1_000_000_000
            suffix = "B"
    
        if isCurrency:
            labels = [f"£{x/divisor:.1f}{suffix}" for x in df[value_col]]
        else:
            labels = [f"{x/divisor:.1f}{suffix}" for x in df[value_col]]


    ax.bar_label(bars, labels=labels, padding=3)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Remove x-axis 
    ax.set_xticks([])
    
    plt.tight_layout()
    plt.show()


# function to plot a line graph
def plot_line(
            df, 
            category_col,
            value_col,
            title, 
            ylabel,
            xlabel,
            isCurrency = False,
            label_currency = "M",
            figsize=(10,7),
            marker="o",
            rotation=0):

    # creating plot 
    fig, ax = plt.subplots(figsize=figsize)

    # setting plot variables
    ax.plot(df[category_col], df[value_col], marker=marker)

    # setting title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


    # # set x axis labels
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

     # set y axis labels
    if (label_currency == "M"):

            # checking if currency is true
            if isCurrency:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"£{x/1_000_000:.0f}M"))
            else:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1_000_000:.0f}M"))
                
    elif (label_currency == "B"):

            # checking if currency is true
            if isCurrency:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"£{x/1_000_000_000:.0f}B"))
            else:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1_000_000_000:.0f}B"))

    
    # show x labels
    plt.xticks(rotation=rotation)
    
    plt.tight_layout()
    plt.show()


# defining a function to plot a histogram

def plot_histogram(
        vals,
        plotLog = False,
        title="",
        xlabel="",
        ylabel="",
        bins = 50,
        figsize = (8,5)):

    # create figure
    plt.figure(figsize = figsize)

    # plot the histogram

    # plotting using log
    if plotLog:
        plt.hist(np.log1p(vals), bins=bins)
        title = title + " (log scale)"
        xlabel = "log (" + xlabel + " + 1)"

    else:                                       # plotting normal values
        plt.hist(vals, bins=bins)
       
    # set labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


    # show
    plt.show()


# defining a function to plot a boxplot

def plot_boxplot(
        vals,
        plotLog = False,
        title="",
        xlabel="",
        ylabel="",
        figsize = (8,5)):

    # create figure
    fig, ax = plt.subplots(figsize=figsize)

    # plot the boxplot

    # plotting using log
    if plotLog:
        ax.boxplot(np.log1p(vals))
        title = title + " (log scale)"
        ylabel = f"log({ylabel} + 1)"

    else:                                       # plotting normal values
        ax.boxplot(vals)
       
    # set labels and title
    ax.set_title(title)

    if xlabel:
        ax.set_xlabel(xlabel)

    if ylabel:
        ax.set_ylabel(ylabel)

    ax.grid(axis="y", linestyle="--", alpha=0.5)

    # show
    plt.tight_layout()
    plt.show()

    return fig, ax

# function to plotting stacked bar chart

def plot_stacked_bar(
        df,
        title,
        xlabel,
        ylabel,
        leg_title,
        rotation=45,
        figsize = (10,6)
        
):


    # plotting the stacked bar chart
    fig, ax = plt.subplots(figsize=figsize)

    df.plot(kind="bar", stacked=True, ax=ax)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.tick_params(axis="x", rotation=rotation)

    ax.legend(
        title=leg_title,
        bbox_to_anchor=(1.05, 1),
        loc="upper left")
    
    plt.tight_layout()
    plt.show()

# defining a function to plot a pie chart

def plot_pie_chart(
            df, 
            category_col,
            value_col,
            title, 
            figsize=(8,8),
            percentage = True):
	
   # creating figure object
    fig, ax = plt.subplots(figsize=figsize)
    
    # creating the pie chart
    ax.pie(
            df[value_col],
            labels=df[category_col],
            autopct="%1.1f%%" if percentage else None,
            startangle=90)

    ax.set_title(title)
    
    plt.tight_layout()
    plt.show()


# function to plot line graph for multiple categoryes
def plot_line_categories(
            df, 
            category_col,
            value_col,
            group_col,
            title, 
            ylabel,
            xlabel,
            isCurrency = False,
            label_currency = "M",
            figsize=(12,7),
            marker="o",
            rotation=0):

    # creating plot 
    fig, ax = plt.subplots(figsize=figsize)

    # setting plot variables for each group

    for group in df[group_col].unique():
        data = df[df[group_col] == group]
        
        ax.plot(
            data[category_col],
            data[value_col],
            marker=marker,
            label=group
        )

    
    # setting title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


    # # set x axis labels
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    # set legend
    ax.legend(title = group_col.replace("_"," ").upper(),
             bbox_to_anchor=(1.05, 1),
            loc="upper left")

    
     # set y axis labels
    if (label_currency == "M"):

            # checking if currency is true
            if isCurrency:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"£{x/1_000_000:.0f}M"))
            else:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1_000_000:.0f}M"))
                
    elif (label_currency == "B"):

            # checking if currency is true
            if isCurrency:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"£{x/1_000_000_000:.0f}B"))
            else:
                ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1_000_000_000:.0f}B"))

    
    # show x labels
    plt.xticks(rotation=rotation)
    
    plt.tight_layout()
    plt.show()
