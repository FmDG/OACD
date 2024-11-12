import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator


mis_boundaries = pd.read_csv('data/MIS_boundaries.csv')

def highlight_glacials(ax: plt.axis, annotate: bool = False) -> plt.axis:
    """
    Highlights glacial intervals on a plot by shading the corresponding time periods.

    This function iterates through all MIS Boundaries according to LR04 highlights those intervals
    on the provided "ax" (a matplotlib axis). If the `annotate` parameter is set to `True`, it also annotates
    the intervals with their names.

    Parameters:
    -----------
    ax : plt.axis
        The matplotlib axis object where the glacial intervals should be highlighted.

    annotate : bool, optional, default: False
        If True, annotates each glacial interval with its respective label. If False, no
        annotations are added.

    Returns:
    --------
    plt.axis
        The updated matplotlib axis with highlighted glacial intervals (and optionally annotations).

    Notes:
    ------
    The shaded glacial intervals are displayed with a transparent grey color, and the
    annotations are placed slightly below the midpoint of each interval.
    """

    for _, row in mis_boundaries.iterrows():
        if row["glacial"] == "glacial":
            ax.axvspan(row["age_start"], row["age_end"], fc='tab:grey', ec=None, alpha=0.1)
        mid_point = ((row["age_start"] + row["age_end"])/2) - 3
        if annotate:
            ax.annotate(row["interval"], xy=[mid_point, -52])
    return ax


def format_tick_positions(axs: list[plt.Axes], num_plots: int, min_age: int, max_age: int, legend: bool = True,
                          x_axis: str = 'Age (ka)') -> list[plt.Axes]:
    """
    Customize tick positions, axis labels, and spines for a list of subplots.

    This function is designed to modify the appearance of subplots in a figure by adjusting
    the position of ticks, hiding certain spines, and adding secondary x-axis labels for age.
    It can also optionally add legends to each subplot.

    Parameters:
    -----------
    axs : list of plt.Axes
        A list of matplotlib Axes objects representing the subplots to be customized.

    num_plots : int
        The total number of subplots (axes) to be modified in the list `axs`.

    min_age : int
        The minimum value for the age range, used to set the x-axis limits of the bottom-most subplot.

    max_age : int
        The maximum value for the age range, used to set the x-axis limits of the bottom-most subplot.

    legend : bool, optional, default: True
        If True, adds a legend to each subplot. If False, no legend is added.

    age : string, optional, default: Age (ka)
        Defines the x-axis label, set to default to "Age (ka)"

    Returns:
    --------
    list of plt.Axes
        The modified list of Axes objects with customized tick positions, spines, and optional legends.

    Notes:
    ------
    - The function removes or modifies the visibility of certain spines (`top`, `right`, `left`, `bottom`)
      depending on the subplot's position in the layout. Odd-numbered subplots have their left spines removed
      and right ticks positioned to the right, while even-numbered subplots have their right spines removed.
    - Minor tick locators are set for both the x and y axes, with 20 minor ticks for the x-axis and 5 for the y-axis.
    - A secondary x-axis is added at the top of the first subplot with an "Age (ka)" label, and minor ticks are set.
    - The bottom-most subplot will have its x-axis labeled with the range from `min_age` to `max_age`.

    Example:
    --------
    fig, axs = plt.subplots(
        nrows = 3
        sharex = 'all'
    )

    format_tick_positions(axs, num_plots=3, min_age=0, max_age=1500)
    """
    for q in range(num_plots):
        # Remove the left/right axes to make the plot look cleaner
        if q % 2 == 1:
            axs[q].yaxis.set(ticks_position="right", label_position='right')
            axs[q].spines['left'].set_visible(False)
        else:
            axs[q].spines['right'].set_visible(False)
        axs[q].spines['top'].set_visible(False)
        axs[q].spines['bottom'].set_visible(False)
        axs[q].xaxis.set_minor_locator(AutoMinorLocator(20))
        axs[q].yaxis.set_minor_locator(AutoMinorLocator(5))
        if legend:
            axs[q].legend(shadow=False, frameon=False)

    # Set the bottom and top axes on and label them with the age.
    secax = axs[0].secondary_xaxis('top')
    secax.set(xlabel="Age (ka)")
    secax.xaxis.set_minor_locator(AutoMinorLocator(10))
    axs[0].spines['top'].set_visible(True)
    axs[(num_plots - 1)].spines['bottom'].set_visible(True)
    axs[(num_plots - 1)].set(xlabel=x_axis, xlim=[min_age, max_age])
    return axs
