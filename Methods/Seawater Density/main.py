import matplotlib.pyplot as plt
from pandas import read_csv

from density_plot import density_plot
from salinity_from_d18O_sw import bespoke_inverse_salinity

# Modern Measurements
modern_temperature_1209 = 1.805  # in deg C
modern_salinity_1209 = 34.580  # in PSU
modern_d18O_sw_1209 = -0.078  # in per mil

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

    mean_temperature = example_data.temp.mean()

    mean_salinity = bespoke_inverse_salinity(
        d18O_sw = example_data.d18O_sw.mean(),
        age = example_data.age_ka.mean(),
        d18O_sw_modern = modern_d18O_sw_1209,
        salinity_modern = modern_salinity_1209
    )

    ax.scatter(
        mean_salinity,
        mean_temperature,
        label = 'Past'
    )

    ax.scatter(
        modern_salinity_1209,
        modern_temperature_1209,
        label = 'Modern'
    )

    ax.legend()

    plt.show()