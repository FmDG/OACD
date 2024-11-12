import matplotlib.pyplot as plt
import pandas as pd


sea_level = pd.read_csv('data/sea_level_data_Rohling_2021.csv')


def salinity_from_d18O_sw(d18O_sw: float, age: float, d18O_sw_modern: float, salinity_modern: float) -> float:
    """
    Calculate the past salinity of seawater at a given age using the oxygen isotope ratio (δ18O) and modern salinity data.

    This function uses a combination of oxygen isotope fractionation data and sea level history to estimate the salinity
    of seawater at a particular time in the past. The calculation adjusts for changes in ice volume, relative sea level,
    and the relationship between δ18O and salinity.

    Parameters:
    -----------
    d18O_sw : float
        The oxygen isotope ratio (δ18O) of seawater at the target age, in per mil (‰).

    age : float
        The age (in thousand years) at which to calculate the salinity. This will be rounded to the nearest thousand years.

    d18O_sw_modern : float
        The δ18O value of modern seawater, in per mil (‰), to use as a baseline for comparison.

    salinity_modern : float
        The current average salinity of seawater (in PSU) to use as a baseline for the past salinity estimate.

    Returns:
    --------
    float
        The estimated salinity (in PSU) of seawater at the given age.

    Notes:
    ------
    The function assumes the use of the sea level database (stored as `sea_level`), which contains information about the
    δ18O of seawater from ice volume changes and the relative sea level (RSL) for various ages.

    The relationship between δ18O and salinity for the Pacific Ocean, as given by LeGrande and Schmidt (2008), is used
    to derive the change in salinity due to changes in the δ18O ratio of seawater.

    The formula used assumes that modern salinity is 34.7 PSU at an average ocean depth of 3682 meters, with relative sea
    level corrections applied based on the past sea level.
    """

    # The sea level database stores ages as floats to the nearest 1 ka.
    age_round = round(age)
    # Find the associated d18O change on the sea level expected for that age.
    age_info = sea_level.loc[sea_level.age_ka == age_round]
    d18O_ivc = age_info.d18Ow_IV
    # Correct d18O_sw for the change in ice volume d18O_sw
    adjusted_d18o_sw = d18O_sw - d18O_ivc
    # Determine the difference in d18O_sw from the past to the modern
    delta_d18O_sw = adjusted_d18o_sw - d18O_sw_modern
    # Derive the difference in salinity from the LeGrande and Schmidt (2008) relationship for the Pacific Ocean.
    delta_salinity = delta_d18O_sw * (1 / 0.44)
    # Correct the change in salinity for the different sea level of the past
    rsl = age_info.SL_m.values[0]
    # 3682 is the average depth of the oceans in m, and 34.7 is the average salinity of the oceans in PSU
    delta_salinity = delta_salinity + ((rsl/3682) * 34.7)
    salinity_final = salinity_modern + delta_salinity
    return salinity_final

