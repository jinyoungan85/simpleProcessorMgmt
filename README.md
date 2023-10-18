# simpleProcessorMgmt
a Python program that simulates the execution of processes on a CPU using different scheduling algorithms.

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Expected Output](#expected-output)

## About
The goal of this Python code is to simulate different scheduling algorithms (FCFS, SJF, Priority) on processes with various attributes such as processID, arrivalTime, burstTime, and priority. The code collects the result of each scheduling algorithhm, and visualize the result in a bar plot for easier comparison.

By default, this code simulates 100 processes with parameters stored in processes.txt. If processes.txt does not exist, the code will generate the file with random numbers.

Upon completion of the simulation, the following metrics for algorithms will be displayed:
- Average Turnaround Time(ms)
- Average Waiting Time(ms)
- CPU Utilization(%)

## Getting Started

### Required Dependency
Please install the following if needed:

- Python 3.8 (or higher version)
- matplotlib 3.7.2 (or higher version)

```bash
    conda install python
    conda install matplotlib
```

### Required Dependencies
Please make sure you have the following dependencies installed:

- Python (version 3.8 or higher)
- Matplotlib (latest version)

You can install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

To install Matplotlib, you can use the following command:

```bash
    conda install matplotlib
```

## Usage
Once you've installed the required dependencies, clone the repository into your local system using the below command:

```bash
    git clone https://github.com/jinyoungan85/simpleProcessorMgmt.git
```

Navigate to your local repository, run the Python code using the following command:

```bash
    python processorMgmt.py
```

### Expected Output
![image](https://github.com/jinyoungan85/simpleProcessorMgmt/assets/50179109/d4ecf301-94d3-4c8d-bda4-f609212d4b15)

![image](https://github.com/jinyoungan85/simpleProcessorMgmt/assets/50179109/779396a2-4088-49e1-a3a3-4c7e4103ec40)
