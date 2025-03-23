# SIR Predictive Analysis Project
### By: Mohammed Rehan
Contributions: Zayn Bhatti, Jeremiah Chulliyadan, Nandan Varma, Huzayfa Jasat

## Introduction
This project explores the application of epidemiological models used to analyze and predict the spread of measles in the United States for the next 20 years. The SIR model is used to preform a predictive analysis using historical data on U.S. measles cases.

Inspired by Mr. P Solver's video $[2]$ on the creating a SIR model in python, this project uses the same approach to solve systems of differential equations using `odeint`, a python package from `scipy.integrate`. Historical data is used to derive all perameters being based on a CSV file $[1]$ containing recorded cases, which serve as the foundations to determining the transmission rate of measles.

Using seperate functions, this program calculates the infection rate constant from histoical data, solves a system of differential equations, and creates a interactive user interface.

It is important to note that I AM NOT AN EPIDEMIOLOGIST and this project is not intended to simulate or predict real-world scenarios. Instead, it serves as experience in Python libraries like `Matplotlib`, `SciPy`, and `NumPy`. The results presented are purely theoretical and are not reflective of real world epidemiological trends

Note: This project was created by Mohammed Rehan Ali Shaik. Tested by contributors. All functions, concepts, or ideas used from other sources are credited on the references page and in-text citations, using their respective identification (more information on the reference pages)

## The SIR Model
<img src='SIR Image.PNG'>

### SIR Model Explanation
#### References: $[2][3][4]$

#### The SIR (Susceptible, Infected, Recovered) model is the simplest epidemiological model used to study the spread of infectious diseases.
#### This model uses a few assumptions to hold true
1. Fixed population size: The U.S. Population stays constant over the measurement period
2. Homogeneous Mixing: the population is assumed to mix randomly and evenly
3. Immunity after recovery: The recovered population cannot become susceptible
4. Doesn't factor  in intervention: Assumes no external intervention like vaccinations

#### With these assumptions, the SIR model breaks the U.S. populations into 3 separate populations:
1. Susceptible (S): Individuals who can contract the disease, The susceptible population decreases as individuals become infected.
2. Infected (I): Individuals currently infected and capable of spreading the disease, The infected population increases when susceptible individuals are infected and decreases as they recover.
3. Recovered (R): Individuals who have recovered and are immune, The recovered population increases as infected individuals recover.

#### Assuming population can only move forward in the model, differential equations are used to describe how the populations change over time

- Susceptible population:
  $\frac{dS}{dt} = -\frac{\beta}{N} S I$


- Infected population: $\frac{dI}{dt} = \frac{\beta}{N} S I - \gamma I$

- Recovered population:
  $\frac{dR}{dt} = \gamma I$


#### This system of equations is solved by `ODEINT` from `SciPy.Integrate`

### Parameters and Variables:
- $\beta$: Infection/Transmission rate constant.
- $\gamma$: Recovery rate constant $\frac{1}{Recovery Period (days)}$
- $N = S + I + R$: Total population.

#### This model helps analyze disease dynamics and predict the spread of infections using 8 functions

## Results
#### Comparrison Data taken from $[6]$
In 2017, the United States reported 120 cases of measles, significantly higher than the usual annual reports of 1 to 2 cases, largely due to an outbreak in a largely unvaccinated Somali community in Minnesota. $[6]$ According to the predictions made by the SIR (Susceptible-Infected-Recovered) model, the estimated number of infections for the same year was 170.11.

$$
\text{Accuracy} = \left( 1 - \frac{| \text{Predicted} - \text{Actual} |}{\text{Actual}} \right) \times 100
$$

Using the predicted value of 170.11 and the actual value of 120:

$$
\text{Accuracy} = \left( 1 - \frac{|170.11 - 120|}{120} \right) \times 100 = \left( 1 - \frac{50.11}{120} \right) \times 100 \approx 58.18\%
$$

The model's prediction is approximately 58.18% accurate, indicating that it overestimated the number of infections. This suggests the model may not fully capture the complexity of the outbreak and could benefit from further refinement and adjustments.

## Improvements

- Refinement of Parameters: Regularly update infection and recovery rates based on real-time data and regional factors, such as vaccination coverage and sociodemographic variables, to improve model accuracy.

- Data Structures and Efficiency: Use more advanced data structures like `Pandas DataFrames` for better handling of time-series data, optimize calculations with vectorization and parallel processing techniques, and store large datasets in `SQL databases` for efficient querying and management.

- Incorporate More Complex Models: Extend the SIR model to more sophisticated models like `SEIR` or `SIRS`, which include additional compartments, and use stochastic processes to account for variability in disease transmission.

## References
[1] "US Measles Cases and Deaths (OWID, 2017)," Our World in Data, Available: https://github.com/owid/owid-datasets/blob/master/datasets/US%20Measles%20Cases%20and%20Deaths%20(OWID%2C%202017)/US%20Measles%20Cases%20and%20Deaths%20(OWID%2C%202017).csv, Accessed: Jan. 8, 2025.

[2] Mr P Solver, "The SIR Disease Model in PYTHON" YouTube, Jan. 2, 2020. [Online]. Available: https://www.youtube.com/watch?v=zpYMiJd3pqg. [Accessed: Jan. 8, 2025].

[3] L. Polson, "Python Metaphysics Series: Vid2," GitHub, Available: https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid2.ipynb, Accessed: Jan. 8, 2025.

[4] https://www.youtube.com/watch?v=f1a8JYAixXU

[5] https://www.canada.ca/en/public-health/services/diseases/measles/health-professionals-measles.html

[6] https://en.wikipedia.org/wiki/Epidemiology_of_measles?utm_source=chatgpt.com

### Reference Usage

- Sections containing concepts or ideas from external sources have been given reference at the section title
- Lines copied and pasted from external sources have been given in-text citation at the end of the respective sentence





