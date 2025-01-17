import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv
import tkinter as tk
import matplotlib
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data = []
beta_list = []
previous_cases = 0
previous_population = 0
gamma = 1 / 10
population = 3349900000
times = np.arange(0, 20, 1)

def reading_data():
    with open('US Measles Cases and Deaths (OWID, 2017).csv', 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            cleaned_line = {key: value for key, value in line.items() if value and value.strip()}
            data.append(cleaned_line)

def beta_value(prev_pop, prev_case):
    for line in data:
        current_case = line.get('Reported Cases', '0').strip()
        current_pop = line.get('Reported Population', '0').strip()

        current_case = int(current_case) if current_case else 0
        current_pop = int(current_pop) if current_pop else 0

        if current_case == 0 or current_pop == 0:
            continue

        delta_case = current_case - prev_case
        delta_pop = current_pop - prev_pop

        if prev_pop != 0 and prev_case != 0:
            temp_beta = delta_case / (prev_case * delta_pop)
            beta_list.append(temp_beta)

        prev_case = current_case
        prev_pop = current_pop

    avg_beta = sum(beta_list) / len(beta_list) if beta_list else 0
    print(f'Average Transmission Rate: {avg_beta}')
    return avg_beta

def dadt(a, t, b, g, n):
    s, i, r = a
    return [
        -b / n * s * i,
        b / n * s * i - g * i,
        g * i
    ]

def initial_data(d):
    if d:
        return d[-1]
    else:
        return None

def solve_ode():
    iO = int(initial_data(data).get('Reported Cases', '0').strip()) if initial_data(data) else 0
    sO = population - iO
    rO = 0

    yo = [sO, iO, rO]
    sol = odeint(dadt, yo, times, args=(beta_value(previous_population, previous_cases), gamma, population))

    global S, I, R
    S, I, R = sol.T

def update(val):
    x_position = slider.val
    vertical_line.set_xdata([x_position])

    idx = (np.abs(times - x_position)).argmin()
    y_infected = I[idx]
    y_recovered = R[idx]

    intersection_itext.set_position((x_position, y_infected))
    intersection_itext.set_text(f'({x_position:.2f}, {y_infected:.2f})')

    intersection_rtext.set_position((x_position, y_recovered))
    intersection_rtext.set_text(f'({x_position:.2f}, {y_recovered:.2f})')

    fig.canvas.draw_idle()

def user_interface():
    reading_data()
    solve_ode()

    global fig, ax, slider, vertical_line, intersection_itext, intersection_rtext

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    ax.plot(times, I, label='Infected', color='blue')
    ax.plot(times, R, label='Recovered', color='green')
    vertical_line = ax.axvline(x=0, color='red', linestyle='--')
    intersection_itext = ax.text(0, 0, "", color='blue', fontsize=10)
    intersection_rtext = ax.text(0, 0, "", color='green', fontsize=10)

    ax.set_xlabel('Time')
    ax.set_ylabel('Cases')
    ax.set_title('Prediction Model')
    ax.legend()
    ax.grid(True)

    ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'Time', times.min(), times.max(), valinit=0, valstep=(times[1] - times[0]))
    slider.on_changed(update)

    root = tk.Tk()
    root.wm_title("SIR Model Plot")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    tk.mainloop()

user_interface()
