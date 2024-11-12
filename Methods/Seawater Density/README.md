# Seawater Density

This generates a seawater density plot for a certain depth in the ocean. This figure can be customised for a certain 
depth, longitude, and latitude in the ocean. This currently calculates the sigma-2 density isopycnals but can be changed
in the code for density_plot.py on line 44. The sea level curve for the salinity calculations comes from Rohling et al., 2021
which can be found at https://www.science.org/doi/10.1126/sciadv.abf5326.


## PreRequisites

The prerequisite packages for this are:
- [Pandas](https://zenodo.org/records/13819579)
- [Numpy](https://www.nature.com/articles/s41586-020-2649-2)
- [GSW](https://zenodo.org/records/5214122)
- [MatPlotLib](https://matplotlib.org)

This code is designed to run on Python 3.

## Usage

Running main.py will generate a temperature-salinity space and plot the mean past salinities. Replacing the csv file, 
example_data.csv with your own data will allow for use of this code with your own data.

## Result

This will end up looking something like the below:

![](example_figure.png)

## System Requirements

The code was written on MacOS Sequoia 15.1 in 2024, but is expected to run on all operating systems that can run 
Python 3. The runtime on a standard desktop computer should be < 0.1 seconds. The installation time on a standard 
desktop computer should be < 0.1 seconds. 



