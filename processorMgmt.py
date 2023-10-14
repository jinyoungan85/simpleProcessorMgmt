# ITEC 3265 OS Assignment3, Due 10/20/2023
# Jin-Young An 
# 1. The Python source code for your Processor Management Program.
# 2. A README file providing instructions on how to run your program
#    and any additional information.

class Process:
    # Constructor of Process class and its attributes 
    # (processID, arrivalTime, burstTime, priority) initialization
    def __init__(self, processID, arrivalTime, burstTime, priority=None):
        self.processID = processID      # unique identifier of a process
        self.arrivalTime = arrivalTime  # time when a process arrives in the ready queue
        self.burstTime = burstTime      # amount of time needed to complete a process
        self.waitingTime = 0            # amount of time a process waits in the ready queue
        self.priority = priority        # priority of a process (optional)
    
class Scheduler:
    # Constructor of Scheduler class and its attributes
    def __init__(self):
        self.readyQueue = []           # list of processes in the ready queue
        self.currentTime = 0           # current time
        
    def add_process(self, process):
        self.readyQueue.append(process)
        
    def run_scheduling_algorithm(self, algorithm):
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
                print("currentTime: ", self.currentTime)
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
    
    # Shortest Job First (SJF) Scheduling Algorithm
    def sjf(self):
        pass
    
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
    process2 = Process(processID=2, arrivalTime=10, burstTime=10)
    
    scheduler = Scheduler()             # create a scheduler object
    scheduler.add_process(process1)     # add processes to the readyQueue of the scheduler object
    scheduler.add_process(process2)
    scheduler.run_scheduling_algorithm("FCFS")  # run the scheduling algorithm
    
if __name__ == "__main__":
    main()