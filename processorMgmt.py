# @jinyoungan85
# Github: https://github.com/jinyoungan85/simpleProcessorMgmt.git

import matplotlib.pyplot as plt
import os, random


class Process:
    # Constructor of Process class and its attributes 
    # (processID, arrivalTime, burstTime, priority) initialization
    def __init__(self, processID, arrivalTime, burstTime, priority=None):
        self.processID = processID      # unique identifier of a process
        self.arrivalTime = arrivalTime  # time when a process arrives in the ready queue
        self.burstTime = burstTime      # amount of time needed to complete a process
        self.waitingTime = 0            # amount of time a process waits in the ready queue
        self.priority = priority        # priority of a process (optional), by default None
    
class Scheduler:
    # Constructor of Scheduler class and its attributes
    def __init__(self):
        self.readyQueue = []           # list of processes in the ready queue
        self.currentTime = 0           # current time
        self.totalWaitingTime = 0      # total waiting time of all processes
        self.totalExecutionTime = 0    # total execution time = sum of burst times of all processes
        self.totalTurnaroundTime = 0   # total turnaround time of all processes
        
    def add_process(self, process):
        self.readyQueue.append(process)
        
    def resetSchedulerTime(self):       # reset the scheduler time and total turnaround time
        self.currentTime = 0
        self.totalWaitingTime = 0
        self.totalTurnaroundTime = 0
        self.totalExecutionTime = 0
        
    def run_scheduling_algorithm(self, algorithm):
        print("\nRunning scheduling algorithm: ", algorithm)
        if algorithm == "FCFS":
            # sort the ready queue by ascending order of arrival time
            # 'key' parameter calls a function on each list element before making comparisons for sorting
            # lambda is an anonymous function that takes one argument and returns a value
            # lambda x: x.arrivalTime same as def f(x): return x.arrivalTime
            # x is an element in the readyQueue and x.arrivalTime is the arrival time of the process element
            self.readyQueue.sort(key=lambda x: x.arrivalTime)
            self.fcfs()
        elif algorithm == "SJF":
            # sort the ready queue by ascending order of burst time
            self.readyQueue.sort(key=lambda x: x.burstTime)
            self.sjf()
        elif algorithm == "Priority":
            # sort the ready queue by ascending order of priority
            self.readyQueue.sort(key=lambda x: x.priority, reverse=True)
            self.priority()
        else:
            print("Invalid input: Please enter FCFS, SJF, or Priority.")
    
    # First Come First Served (FCFS) Scheduling Algorithm
    def fcfs(self):
        for process in self.readyQueue:
            self.calculate_metrics(process)
            
    # Shortest Job First (SJF) Scheduling Algorithm
    def sjf(self):
        for process in self.readyQueue:
            self.calculate_metrics(process)
                
    # Priority Scheduling Algorithm
    def priority(self):
        for process in self.readyQueue:
            self.calculate_metrics(process)
    
    # Algorithm function calls this function to calculate performance metrics
    def calculate_metrics(self, process):
        if process.arrivalTime > self.currentTime:
            self.currentTime = process.arrivalTime
        process.waitingTime = self.currentTime - process.arrivalTime
        process.turnaroundTime = process.waitingTime + process.burstTime
        print(f"Process {process.processID} waiting time: {process.waitingTime} "
              f"burst time: {process.burstTime} turnaround time: {process.turnaroundTime}")
        self.currentTime += process.burstTime
        self.totalWaitingTime += process.waitingTime
        self.totalTurnaroundTime += process.turnaroundTime
        self.totalExecutionTime += process.burstTime
        
# Run a simulation scenario and print the results in a text and a bar graph
def main():
    processList = []      # a list to hold processes
    NUM_PROCESSES = 100   # number of processes to simulate
    
    # Generate processes and append them to processList if processes.txt is not found
    if not os.path.exists(".\processes.txt"):
        for _ in range(NUM_PROCESSES):
            processID = random.randint(1, 99)
            arrivalTime = random.randint(1, 99)
            burstTime = random.randint(1, 99)
            priority = random.randint(1, 99)
            processList.append(Process(processID, arrivalTime, burstTime, priority))

        # Write the processes data to a txt file withing the same directory
        with open(".\processes.txt", "w") as outfile:
            for process in processList:
                outfile.write(f"{process.processID},{process.arrivalTime},{process.burstTime},{process.priority}\n")
    
    else:
        print("Found processes.txt. Reading processes from the file...")
        with open(".\processes.txt", "r") as infile:      # read processes from the file
            for line in infile:
                line = line.strip()                       # remove leading and trailing whitespace
                processID, arrivalTime, burstTime, priority = line.split(",")
                process = Process(processID, int(arrivalTime), int(burstTime), int(priority))
                processList.append(process)
        
    scheduler = Scheduler()             # create a scheduler object
    for process in processList:
        scheduler.add_process(process)  # add processes to the readyQueue of the scheduler object
    
    algorithmNames = ["FCFS", "SJF", "Priority"]  # Add more algorithm names as needed
    average_turnaround_times = []     # a list to hold average turnaround times of scheduling algorithms
    average_waiting_times = []        # a list to hold average waiting times of scheduling algorithms        
    cpu_utilizations = []             # a list to hold cpu utilizations of scheduling algorithms
    
    for algorithm in algorithmNames:
        scheduler.run_scheduling_algorithm(algorithm)  # run the scheduling algorithm
        # Average Turnaround Time = (Sum of Turnaround Time of all processes) / (Number of processes)
        average_waiting = scheduler.totalWaitingTime / len(scheduler.readyQueue)
        average_turnaround = scheduler.totalTurnaroundTime / len(scheduler.readyQueue)
        # append the metrics to the corresponding lists
        average_waiting_times.append(average_waiting)
        average_turnaround_times.append(average_turnaround)
        # CPU Utilization(%) = (Total Execution Time / Total Simulation Time) * 100
        cpu_utilizations.append((scheduler.totalExecutionTime / scheduler.currentTime) * 100)
        scheduler.resetSchedulerTime()      # reset the scheduler time and total turnaround time
        
    # Display the metrics for each algorithm to compare them at glance
    print(f"\nThe number of processes simulated: {len(processList)}")
    print(" Algorithm\tAverage Turnaround Time(ms)\tAverage Waiting Time(ms)\tCPU Utilization(%)")
    for i in range(len(algorithmNames)):
        print(f"{algorithmNames[i]:>10}\t{average_turnaround_times[i]:<10.2f}\t\t\
            {average_waiting_times[i]:<10.2f}\t\t\t{cpu_utilizations[i]:>10.2f}")                   
        
    # visualize the average metrics of scheduling algorithms by plotting a bar graph
    barWidth = 0.25
    r1 = range(len(algorithmNames))    # a list for x-coordinates of bars for average turnaround times
    r2 = [x + barWidth for x in r1]    # a list for x-coordinates of bars for average waiting times
    plt.figure(figsize=(10, 6))        # set the bar figure size
    plt.bar(r1, average_turnaround_times, color='blue', width=barWidth, edgecolor='grey', label='Average Turnaround Time') # .bar(x, y, ...)
    plt.bar(r2, average_waiting_times, color='orange', width=barWidth, edgecolor='grey', label='Average Waiting Time')
    plt.xlabel("Scheduling Algorithm")
    plt.ylabel("Time (ms)")
    plt.xticks([r + barWidth/2 for r in range(len(algorithmNames))], algorithmNames)  # put labels on x-axis, xticks([x-coordinates], [labels])
    plt.title("Average Turnaround Time and Average Waiting Time Among Scheduling Algorithms")
    plt.legend()
    # Add labels with average metrics above the bars
    for i in range(len(algorithmNames)):
        plt.text(r1[i], average_turnaround_times[i], f'{average_turnaround_times[i]:.2f}', ha='center', va='bottom', fontsize=9)
        plt.text(r2[i], average_waiting_times[i], f'{average_waiting_times[i]:.2f}', ha='center', va='bottom', fontsize=9)
    plt.show()
    
    
if __name__ == "__main__":
    main()