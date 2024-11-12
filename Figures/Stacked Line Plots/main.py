
import matplotlib.pyplot as plt
import pandas as pd
import random as rand

from figure_formatting import highlight_glacials, format_tick_positions
from figure_arguments import args_site_01, args_site_02


def plot_basic_figure():
    # Load the datasets
    mg_ca_dataset = pd.read_csv('data/mg_ca_example.csv')
    d18O_dataset = pd.read_csv('data/d18O_example_1.csv')
    second_d18O_dataset = pd.read_csv('data/d18O_example_2.csv')

    # Define the figure
    fig, axs = plt.subplots(
        nrows=2,
        figsize = (8, 5),
        sharex='all'  # Important so all the axes share the same
    )

    # Reduce the space between axes to 0
    fig.subplots_adjust(hspace=0)

    for ax in axs:
        highlight_glacials(ax)

    axs[0].plot(mg_ca_dataset.age_ka, mg_ca_dataset.BWT, **args_site_01)
    axs[0].set(ylabel='BWT Estimate ({})'.format(u'\N{DEGREE SIGN}C'), ylim = [0, 1.5])

    axs[1].plot(d18O_dataset.age_ka, d18O_dataset.d18O, **args_site_01)
    axs[1].plot(second_d18O_dataset.age_ka, second_d18O_dataset.d18O, **args_site_02)

    axs[1].set(ylabel="Planktic {} ({})".format(r'$\delta^{18}$O', u"\u2030"), ylim=[3.7, 2.0])

    format_tick_positions(axs, 2, 1200, 2500, True)

    plt.show()


if __name__ == "__main__":
    plot_basic_figure()
