# Elevator Simulation

This project is forked from a project by <a href="https://github.com/mrbrianevans">mrbrianevans</a> and simulates the behavior of an elevator system in a building with multiple floors. The simulation includes an example algorithm for elevator movement and provides the option to visualize the elevator's operations. You are encouraged to test your elevator logic to come up with an optimal solution for different times, floors and numbers of people.

<img src="lift.jpg" alt="anime-lift" width="500"/>

## Features

- **Random Data Generation:** Generates random timestamped data to simulate elevator usage over a period of time, simulating typical elevator usage patterns.
- **Simulation Algorithms:**
  - **Baseline Algorithm:** Follows a simple up-and-down approach, reversing direction only at the top or bottom floors.
  - **Design your own:** Test functions before submitting to the Data Engineers' Coding Challenge!
- **Animation:** Visualize the elevator's movements and passenger behavior using a GUI.

## Files

- **elevator_simulation.py:** The core simulation script that defines the behavior of the elevator, the people using it, and the various algorithms that control it. The simulation can run with or without animation.
- **charts.py:** A script for generating visualizations such as histograms of elevator wait times and plots of mean floor entries/exits by time interval.
- **create_entries.py:** A script for generating a pandas DataFrame of simulated entries and exits throughout the day. 
- **run_lifts.ipynb:** A Jupyter notebook that provides an interface to run and test the elevator simulation with different parameters and visualise the results.  
  - **Efficient Algorithm:** Prioritizes passengers already in the elevator and optimizes for the closest destination.
  - **Baseline Algorithm:** Follows a simple up-and-down approach, reversing direction only at the top or bottom floors.
- **Animation:** Visualize the elevator's movements and passenger behavior using a GUI.

## Prerequisites

- Python 3.x
- Libraries: `random`, `pandas`, `datetime`, `tkinter`, `time`

## Installation

Clone this repository:

```bash
git clone https://github.com/uncultivate/elevator-master.git
cd elevator-master
```

## Usage

### Running the Simulation

You can run the simulation in several ways, depending on your environment:

#### Running locally in a Jupyter Notebook
To run the simulation locally in a Jupyter Notebook:

1. Install Jupyter Notebook (if you haven't already):

```bash
pip install notebook
```

2. Open Jupyter Notebook

```bash
jupyter notebook
```

3. Load the Notebook: Open the run_lifts_master.ipynb file in Jupyter Notebook.

4. Run the Simulation: Follow the instructions provided in the notebook. You can adjust the parameters, run the simulation, and visualise the results directly within the notebook.

#### Running in Google Colab
If you prefer to run the simulation in Google Colab:

1. Open Google Colab:
  - Go to <a href="https://colab.research.google.com">Google Colab</a> and upload the run_lifts.ipynb.
2. Upload the other project files:
  - Upload the elevator_simulation.py, charts.py, and create_entries.py files to your Colab runtime
3. Run the Simulation:
  - Run the cells in the notebook. Google Colab allows you to execute Python code, visualize results, and adjust parameters just like in a local Jupyter Notebook. The only drawback is that you will not be able to run the tkinter animations. 


### Viewing the Results
The results, including total time elapsed, shortest wait time, longest wait time, and average wait time, can be created as a DataFrame. If the animation is enabled, these results will also appear in the GUI.

<img src="elevator_video.gif" alt="screenshot" width="500"/>