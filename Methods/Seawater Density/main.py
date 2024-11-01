import matplotlib.pyplot as plt

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

    salinities = [33.5, 33.7, 35.1, 34.4]
    temperatures = [-2, 1.1, 0.5, 3.5]

    ax.scatter(
        salinities,
        temperatures
    )

    plt.show()