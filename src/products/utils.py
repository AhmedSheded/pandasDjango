import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/2.0.2/faq/usage_faq.html
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))

    if chart_type == 'bar plot':
        title = 'bar plot'
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = 'line plot'
        plt.title(title)
        plt.plot(x, y)
    else:
        title = 'count plot'
        plt.title(title)
        sns.countplot('name', data=df)
