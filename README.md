# Digital-filters-and-examples-Python

This repository implements FIR-window Based functions. Files include: 

1. High pass fitler and example
2. Low pass filter and example.
3. band pass filter and example.
4. noth filter and example.

The design of the filter is based on the windowing method which includes the next steps:

1. Choosing the type of window according to the attenuation in the stop band or the ripple in the transition band 
![Alt text](https://github.com/Edgar-Noita/Digital-filters-and-examples-Python/blob/main/window.png)

2. Choosing the number of coefficients according to the specfication of the windows and the size of the transition band. The more the cefficientes, the shorter the transition period.

3. Define the equation of the filter by using the inverse furier transform of an ideal window:
 ![Alt text](https://github.com/Edgar-Noita/Digital-filters-and-examples-Python/blob/main/eq_2.png)


