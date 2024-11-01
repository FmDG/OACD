import gsw
import matplotlib.pyplot as plt
import numpy as np


def density_plot(
        min_temp:float = -4.0,
        max_temp:float = 15.0,
        min_sal:float = 33.0,
        max_sal:float = 36.0,
        water_depth: float = 2340,
        longitude: float = 158.506,
        latitude: float = 32.652,
        num_isopycnals:int = 10
):
    """
    This function uses the Gibbs Seawater (GSW) library to generate a contour plot of density (sigma-2)
    given minimum and maximum temperature and salinity values. It takes four parameters, min_temp, max_temp,
    min_sal and max_sal, as input and plots the density contours of the resulting temperature-salinity space.
    It also labels the axes, contour lines and titles the plot.
    :param min_temp: minimum temperature of the plot
    :param max_temp: maximum temperature of the plot
    :param min_sal: minimum salinity of the plot
    :param max_sal: maximum salinity of the plot
    :param water_depth: water depth of the region where we are calculating density.
    :param latitude: latitude of the region where we are calculating density plot.
    :param longitude: longitude of the region where we are calculating density plot.
    :param num_isopycnals: number of density isopycnals specified in the plot
    :return: density plot
    """
    # Define the temperature and salinity space
    temperatures = np.linspace(min_temp, max_temp, 156)
    salinity = np.linspace(min_sal, max_sal, 156)
    # Create a mesh of this space
    temp, sal = np.meshgrid(temperatures, salinity)
    # Absolute pressure at depth in dbar
    absolute_pressure = (1023.6 * 9.81 * water_depth) / 100000
    # Converted absolute pressure to sea pressure, which is absolute pressure - 10.1325 dbar
    sea_pressure = absolute_pressure - 10.1325
    # Convert practical salinity to absolute salinity
    ab_sal = gsw.SA_from_SP(sal, sea_pressure, longitude, latitude)
    # Determine the densities of each of the isopycnals
    # Generate a density space using this mesh
    densities = gsw.sigma2(ab_sal, temp)  ## NOTE: Change this function to sigma0 - sigma4 depending on preference.

    # Create the figure
    fig, ax = plt.subplots(figsize=(7, 6))
    # Generate contours in density space for each T and S point
    contours = ax.contour(sal, temp, densities, colors="grey", zorder=1, levels=num_isopycnals)
    # Label the density contours
    plt.clabel(contours, fontsize=10, inline=False, fmt="%.1f")
    # Label the axes
    ax.set(xlabel=r'Salinity (psu)', ylabel=r'Temperature ($^\circ$C)')

    plt.tight_layout()

    return ax