# ITEC 3265 OS Assignment3, Due 10/20/2023
# Jin-Young An 
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
        self.totalTurnaroundTime = 0    # total turnaround time of all processes
        
    def add_process(self, process):
        self.readyQueue.append(process)
        
    def resetSchedulerTime(self):       # reset the scheduler time and total turnaround time
        self.currentTime = 0
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
            self.readyQueue.sort(key=lambda x: x.priority)
            self.priority()
        else:
            print("Invalid input: Please enter FCFS, SJF, or Priority.")
    
    # First Come First Served (FCFS) Scheduling Algorithm
    def fcfs(self):
        for process in self.readyQueue:
            # if the arrival time of a process is greater than the current time
            # move the current time to the arrival time to simulate the process arrival
            if process.arrivalTime > self.currentTime:
                self.currentTime = process.arrivalTime
            # calculate the waiting time = time a process spent waiting in readyQueue before execution
            process.waitingTime = self.currentTime - process.arrivalTime
            # calculate the turnaround time of a process: turnaround time = waiting time + burst time
            process.turnaroundTime = process.waitingTime + process.burstTime
            
            print(f"Process {process.processID} waiting time: {process.waitingTime} "
                  f"burst time: {process.burstTime} turnaround time: {process.turnaroundTime}")
            
            # store performance metrics (waitingTime, turnaroudTime) of the process
            self.calculate_metrics(process)
            # move the current time to the end of the process execution
            self.currentTime += process.burstTime
            # update total turnaround time upon each process completion
            self.totalTurnaroundTime += process.turnaroundTime
            
    # Shortest Job First (SJF) Scheduling Algorithm
    def sjf(self):
        for process in self.readyQueue:
            if process.arrivalTime > self.currentTime:
                self.currentTime = process.arrivalTime
            process.waitingTime = self.currentTime - process.arrivalTime
            process.turnaroundTime = process.waitingTime + process.burstTime
            print(f"Process {process.processID} waiting time: {process.waitingTime} "
                  f"burst time: {process.burstTime} turnaround time: {process.turnaroundTime}")
            self.calculate_metrics(process)
            self.currentTime += process.burstTime
            self.totalTurnaroundTime += process.turnaroundTime
                
    # Priority Scheduling Algorithm
    def priority(self):
        pass
    
    # Algorithm function calls this function to calculate performance metrics
    def calculate_metrics(self, process):
        waitingTime = process.waitingTime
        turnaroundTime = process.turnaroundTime
        cpuUtilization = 0
        return waitingTime, turnaroundTime, cpuUtilization


# Run a scenario and print the results with visualizations
def main():
    process1 = Process(processID=1, arrivalTime=5, burstTime=10)
    process2 = Process(processID=2, arrivalTime=10, burstTime=15)
    process3 = Process(processID=3, arrivalTime=30, burstTime=20)
    process4 = Process(processID=4, arrivalTime=40, burstTime=5)
    
    scheduler = Scheduler()             # create a scheduler object
    scheduler.add_process(process1)     # add processes to the readyQueue of the scheduler object
    scheduler.add_process(process2)
    scheduler.add_process(process3)
    scheduler.add_process(process4)
    
    algorithmNames = ["FCFS", "SJF"]  # Add more algorithm names as needed
    average_turnaround_times = []
    
    for algorithm in algorithmNames:
        scheduler.run_scheduling_algorithm(algorithm)  # run the scheduling algorithm, FCFS
        print("Total time elapsed: ", scheduler.currentTime)
        # Average Turnaround Time = (Sum of Turnaround Time of all processes) / (Number of processes)
        average_turnaround = scheduler.totalTurnaroundTime / len(scheduler.readyQueue)
        average_turnaround_times.append(average_turnaround)
        print(f"Average Turnaround Time: {average_turnaround:.2f}")
        scheduler.resetSchedulerTime()                 
    
    print(average_turnaround_times)
    plt.bar(algorithmNames, average_turnaround_times)
    plt.xlabel("Scheduling Algorithm")
    plt.ylabel("Average Turnaround Time")
    plt.title("Average Turnaround Time Among Scheduling Algorithms")
    plt.show()
    
    
if __name__ == "__main__":
    main()