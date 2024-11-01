import matplotlib.pyplot as plt
from pandas import read_csv

from density_plot import density_plot



if __name__ == "__main__":
    # Make density plot
    ax = density_plot(
        min_temp = -4.0,
        max_temp = 15.0,
        min_sal = 33.0,
        max_sal = 36.0,
        water_depth = 2340,
        longitude = 158.506,
        latitude = 32.652,
        num_isopycnals = 10
    )

    example_data = read_csv('data/example_data.csv')

    ax.scatter(
        example_data.Salinity,
        example_data.Temperature
    )

    plt.show()