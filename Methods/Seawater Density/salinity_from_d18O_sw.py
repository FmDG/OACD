import matplotlib.pyplot as plt
import pandas as pd


sea_level = pd.read_csv('data/sea_level_data_Rohling_2021.csv')


def bespoke_inverse_salinity(d18O_sw: float, age: float, d18O_sw_modern: float, salinity_modern: float) -> float:
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

