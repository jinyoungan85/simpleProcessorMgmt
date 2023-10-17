# @jinyoungan85
# Github: https://github.com/jinyoungan85/simpleProcessorMgmt.git

import matplotlib.pyplot as plt


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
        self.totalTurnaroundTime = 0    # total turnaround time of all processes
        
    def add_process(self, process):
        self.readyQueue.append(process)
        
    def resetSchedulerTime(self):       # reset the scheduler time and total turnaround time
        self.currentTime = 0
        self.totalWaitingTime = 0
        self.totalTurnaroundTime = 0
        
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
        
# Run a scenario and print the results with visualizations
def main():
    process1 = Process(processID=1, arrivalTime=5, burstTime=10, priority=3)
    process2 = Process(processID=2, arrivalTime=10, burstTime=15, priority=1)
    process3 = Process(processID=3, arrivalTime=30, burstTime=20, priority=2)
    process4 = Process(processID=4, arrivalTime=40, burstTime=5, priority=4)
    
    scheduler = Scheduler()             # create a scheduler object
    scheduler.add_process(process1)     # add processes to the readyQueue of the scheduler object created
    scheduler.add_process(process2)
    scheduler.add_process(process3)
    scheduler.add_process(process4)
    
    algorithmNames = ["FCFS", "SJF", "Priority"]  # Add more algorithm names as needed
    average_turnaround_times = []     # a list to hold average turnaround times of scheduling algorithms
    average_waiting_times = []        # a list to hold average waiting times of scheduling algorithms
    
    for algorithm in algorithmNames:
        scheduler.run_scheduling_algorithm(algorithm)  # run the scheduling algorithm
        print("Total time elapsed: ", scheduler.currentTime) # display the total time elapsed from the start
        # Average Turnaround Time = (Sum of Turnaround Time of all processes) / (Number of processes)
        average_waiting = scheduler.totalWaitingTime / len(scheduler.readyQueue)
        average_turnaround = scheduler.totalTurnaroundTime / len(scheduler.readyQueue)
        average_waiting_times.append(average_waiting)
        average_turnaround_times.append(average_turnaround)
        print(f"Average Waiting Time: {average_waiting:.2f}")
        print(f"Average Turnaround Time: {average_turnaround:.2f}")
        scheduler.resetSchedulerTime()      # reset the scheduler time and total turnaround time                 
        
    # visualize the average turnaround times and average waiting times of scheduling algorithms by plotting a bar graph
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
    plt.show()
    
    
if __name__ == "__main__":
    main()