# simpleProcessorMgmt
a Python program that simulates the execution of processes on a CPU using different scheduling algorithms.

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)

## About
The goal of this Python code is to simulate different scheduling algorithms (FCFS, SJF, Priority) on processes with various attributes such as processID, arrivalTime, burstTime, and priority. The code collects the result of each scheduling algorithhm, and visualize the result in a bar plot for easier comparison.

By default, this code simulates 100 processes with parameters stored in processes.txt. If processes.txt does not exist, the code will generate the file with random numbers.

## Getting Started

### Required Dependency
Please install the followings if needed:

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
Once you've installed the required dependencies, clone the repository into your local system using below command:

```bash
    git clone https://github.com/jinyoungan85/simpleProcessorMgmt.git
```

Navigate to your local repository, run the Python code using the following command:

```bash
    python processorMgmt.py
```