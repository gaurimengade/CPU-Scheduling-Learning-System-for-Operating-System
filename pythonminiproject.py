def show_menu():

    print("\n")
    print("~" * 60)
    print("          CPU SCHEDULING LEARNING SYSTEM")
    print("~" * 60)

    print("\nThis system helps you learn CPU Scheduling")
    print("and solve your own scheduling problems step-by-step.")

    print("\nSelect an option:")

    print("1. FCFS - First Come First Serve")
    print("2. SJF - Shortest Job First")
    print("3. Priority Scheduling")
    print("4. Round Robin")
    print("5. Exit")

    print("_" * 65)


def show_theory(choice):

    if choice == 1:

        print("\n")
        print("." * 70)
        print("              FCFS - FIRST COME FIRST SERVE")
        print("." * 70)

        print("""
MEANING :-
-------
FCFS stands for First Come First Serve.
It is one of the simplest CPU Scheduling Algorithms.
The process that arrives first gets the CPU first.

It follows:
First In -> First Out (FIFO)

TYPE :-
----
FCFS is a NON-PREEMPTIVE scheduling algorithm.
Non-preemptive means that once a process gets the CPU,
it continues execution until it finishes.

HOW FCFS WORKS :-
--------------
Step 1:
Check the Arrival Time of all processes.

Step 2:
Find the process that arrived first.

Step 3:
Give the CPU to that process.

Step 4:
Execute the process completely.

Step 5:
After it finishes, select the next available process.

Step 6:
Continue until all processes are completed.


EXAMPLE :-
-------
Suppose:
P1 -> AT = 0, BT = 5
P2 -> AT = 1, BT = 3
P3 -> AT = 2, BT = 2

Arrival order:
P1 -> P2 -> P3

Therefore:
Execution Order = P1 -> P2 -> P3


ADVANTAGES :-
----------
1. Very simple to understand.
2. Easy to implement.
3. Easy to calculate.
4. Processes are handled according to arrival order.


DISADVANTAGES :-
-------------
1. Short processes may wait behind long processes.
2. Average waiting time can become high.
3. It is not suitable for time-sharing systems.


CONVOY EFFECT :-
-------------
Convoy Effect is an important disadvantage of FCFS.
It occurs when a long CPU-bound process comes first and makes many short processes wait for a long time.

Example:
P1 -> BT = 10
P2 -> BT = 2
P3 -> BT = 1

FCFS Order:
P1 -> P2 -> P3

P1 takes 10 units of CPU time.
Therefore, P2 and P3 have to wait until P1 finishes.
This situation is called the Convoy Effect.


WHY DOES CONVOY EFFECT OCCUR?
-----------------------------
FCFS mainly considers Arrival Time.
It does not consider whether a process has a small or large Burst Time.
Therefore, a long process arriving first can make
short processes wait.


EFFECTS OF CONVOY EFFECT :-
------------------------
1. Waiting time increases.
2. Average waiting time increases.
3. Short processes experience unnecessary delay.
4. Overall system performance can decrease.


IMPORTANT FORMULAS :-
-------------------
Completion Time:
CT = Time at which the process finishes

Turnaround Time:
TAT = CT - AT

Waiting Time:
WT = TAT - BT

Average Waiting Time:
Average WT = Total WT / Number of Processes

Average Turnaround Time:
Average TAT = Total TAT / Number of Processes """)

    elif choice == 2:

        print("\n")
        print("." * 70)
        print("              SJF - SHORTEST JOB FIRST")
        print("." * 70)

        print("""
MEANING :-
-------
SJF stands for Shortest Job First.
In SJF, the process having the smallest Burst Time is selected first.

Main idea:
Shortest Burst Time -> Execute First

TYPE :-
----
The SJF implemented in this project is NON-PREEMPTIVE.
Once a process starts execution, it continues until it finishes.


HOW SJF WORKS :-
-------------
Step 1:
Check which processes have arrived.

Step 2:
Look at the Burst Time of available processes.

Step 3:
Select the process having the smallest Burst Time.

Step 4:
Execute that process completely.

Step 5:
Again check the available processes.

Step 6:
Select the process with the smallest Burst Time.

Step 7:
Continue until all processes are completed.


EXAMPLE :-
-------
Suppose:
P1 -> AT = 0, BT = 6
P2 -> AT = 0, BT = 3
P3 -> AT = 0, BT = 2

All processes are available.

Burst Times:
P1 = 6
P2 = 3
P3 = 2

Smallest Burst Time = P3

Therefore:
Execution Order = P3 -> P2 -> P1

ADVANTAGES :-
----------
1. Short processes finish quickly.
2. It can reduce average waiting time.
3. Easy to understand for simple examples.

DISADVANTAGES :-
-------------
1. Burst Time needs to be known or estimated.
2. Long processes may wait for a long time.
3. Starvation can occur.


STARVATION :-
----------
Starvation means that a process waits for a very long time because other processes keep getting selected.

For example:
If short processes keep arriving continuously, a long process may continue waiting.
Therefore, SJF can cause starvation.

IMPORTANT POINT
---------------
SJF selects according to:
   Smallest Burst Time
   But the process must first have arrived.
   A process that has not arrived cannot be selected.


IMPORTANT FORMULAS :-
-------------------
Completion Time:
CT = Time at which the process finishes

Turnaround Time:
TAT = CT - AT

Waiting Time:
WT = TAT - BT

Average Waiting Time:
Average WT = Total WT / Number of Processes

Average Turnaround Time:
Average TAT = Total TAT / Number of Processes """)

    elif choice == 3:

        print("\n")
        print("." * 70)
        print("                 PRIORITY SCHEDULING")
        print("." * 70)

        print("""
MEANING :-
-------
In Priority Scheduling, every process is assigned a priority number.
The CPU selects the process according to its priority.

PRIORITY RULE USED IN THIS PROJECT :-
----------------------------------
Smaller Priority Number = Higher Priority

For example:-
Priority 1 -> Highest
Priority 2 -> Second Highest
Priority 3 -> Third Highest

TYPE :-
----
The Priority Scheduling implemented in this project is NON-PREEMPTIVE.
Once a process starts execution, it continues until it finishes.


HOW PRIORITY SCHEDULING WORKS :-
-----------------------------
Step 1:
Check which processes have arrived.

Step 2:
Check their priority values.

Step 3:
Select the process with the highest priority.

Step 4:
Execute the selected process completely.

Step 5:
Check the remaining available processes.

Step 6:
Select the next highest-priority process.

Step 7:
Continue until all processes are completed.


EXAMPLE :-
-------
Suppose:
P1 -> AT = 0, BT = 5, Priority = 3
P2 -> AT = 0, BT = 3, Priority = 1
P3 -> AT = 0, BT = 2, Priority = 2

Priority order:
P2 -> Priority 1
P3 -> Priority 2
P1 -> Priority 3

Therefore:
Execution Order = P2 -> P3 -> P1

ADVANTAGES :-
----------
1. Important processes can execute first.
2. Useful when processes have different importance.
3. Easy to understand and implement.

DISADVANTAGES :-
-------------
1. Low-priority processes may wait for a long time.
2. Starvation can occur.
3. Priority values must be assigned correctly.

STARVATION :-
----------
A low-priority process may keep waiting if higher-priority processes continue to arrive.
This problem is called starvation.

IMPORTANT POINT
---------------
In this project:
    Lower Priority Number = Higher Priority


IMPORTANT FORMULAS :-
-------------------
Completion Time:
CT = Time at which the process finishes

Turnaround Time:
TAT = CT - AT

Waiting Time:
WT = TAT - BT

Average Waiting Time:
Average WT = Total WT / Number of Processes

Average Turnaround Time:
Average TAT = Total TAT / Number of Processes """)

    elif choice == 4:

        print("\n")
        print("." * 70)
        print("                ROUND ROBIN SCHEDULING")
        print("." * 70)

        print("""
MEANING :-
-------
Round Robin is a CPU Scheduling Algorithm mainly used for time-sharing systems.
Each process gets a fixed amount of CPU time.
This fixed amount of time is called TIME QUANTUM.

TYPE :-
----
Round Robin is a PREEMPTIVE scheduling algorithm.
Preemptive means the CPU can stop the currently running process and give the CPU to another process.


TIME QUANTUM :-
------------
Time Quantum is the maximum amount of CPU time given to a process during one turn.

Example:
Time Quantum = 2

A process can execute for up to 2 time units
in one turn.


HOW ROUND ROBIN WORKS :-
---------------------
Step 1:
Processes are placed in the Ready Queue.

Step 2:
The first process gets the CPU.

Step 3:
It runs for the given Time Quantum.

Step 4:
If the process finishes, it is removed.

Step 5:
If it does not finish, its remaining Burst Time
is calculated.

Step 6:
The unfinished process goes to the end of
the Ready Queue.

Step 7:
The next process gets the CPU.

Step 8:
Continue until all processes are completed.

EXAMPLE :-
-------
Suppose:
P1 -> BT = 5
P2 -> BT = 3
P3 -> BT = 2

Time Quantum = 2

Execution can be:
P1 -> 2 units
P2 -> 2 units
P3 -> 2 units
P1 -> 2 units
P2 -> 1 unit
P1 -> 1 unit

ADVANTAGES :-
----------
1. Fair CPU allocation.
2. Suitable for time-sharing systems.
3. Every process gets a chance to execute.
4. No process can hold the CPU for too long.

DISADVANTAGES :-
-------------
1. Very small Time Quantum can cause many context switches.
2. Very large Time Quantum makes it similar to FCFS.
3. Choosing the correct Time Quantum is important.

CONTEXT SWITCH :-
--------------
A context switch happens when the CPU changes from one process to another.

For example:
P1 -> CPU

Then CPU changes to:
P2 -> CPU

This change is called a context switch.

IMPORTANT FORMULAS :-
-------------------
Completion Time:
CT = Time at which the process finishes

Turnaround Time:
TAT = CT - AT

Waiting Time:
WT = TAT - BT

Average Waiting Time:
Average WT = Total WT / Number of Processes

Average Turnaround Time:
Average TAT = Total TAT / Number of Processes """)
        

def calculate_result(processes):

    total_wt = 0
    total_tat = 0

    print("\n")
    print("     FINAL RESULT")
    print("_" * 25)

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    print("_" * 50)

    for p in processes:

        p["TAT"] = p["CT"] - p["AT"]

        p["WT"] = p["TAT"] - p["BT"]

        total_tat = total_tat + p["TAT"]
        total_wt = total_wt + p["WT"]

        print(
            p["PID"], "\t",
            p["AT"], "\t",
            p["BT"], "\t",
            p["CT"], "\t",
            p["TAT"], "\t",
            p["WT"]
        )

    average_wt = total_wt / len(processes)
    average_tat = total_tat / len(processes)

    print("\nTotal Waiting Time =", total_wt)
    print("Total Turnaround Time =", total_tat)
    print("Average Waiting Time =",round(average_wt, 2))
    print( "Average Turnaround Time =",round(average_tat, 2) )
 

def show_gantt_chart(gantt_chart):

    print("\n")
    print("_" * 70)
    print("                 GANTT CHART")
    print("_" * 70)

    if len(gantt_chart) == 0:
        print("No execution data available.")
        return

    # Print process names
    print("|", end="")

    for item in gantt_chart:
        print("  " + item[0] + "  |", end="")
    print()

    # Print starting time
    print(gantt_chart[0][1], end="")

    # Print ending times
    for item in gantt_chart:

        print("       " + str(item[2]), end="")

    print("\n")

    print("The Gantt Chart shows the order in which")
    print("the CPU executes the processes.")

    print("_" * 70)

 
def fcfs(processes):

    print("\n")
    print("." * 70)
    print("                     FCFS SOLUTION")
    print("." * 70)

    # Arrange processes according to Arrival Time
    processes.sort(key=lambda x: x["AT"])

    time = 0

    # Store Gantt Chart information
    gantt_chart = []

    for i in range(len(processes)):
        p = processes[i]

        print("\n")
        print("-" * 60)
        print("STEP", i + 1)
        print("-" * 60)

        # CPU is idle
        if time < p["AT"]:

            print("CPU is idle from", time, "to", p["AT"] )

            gantt_chart.append( ("IDLE", time, p["AT"]))

            time = p["AT"]

        print("\nSelected Process:", p["PID"])
        print("Why selected?")
        print("It arrived first according to FCFS.")

        start_time = time

        print("\nStart Time =", start_time)
        print("Burst Time =", p["BT"])

        # CT = Start Time + BT
        time = time + p["BT"]

        p["CT"] = time

        print("\nCompletion Time:")
        print("CT =", start_time, "+", p["BT"])
        print("CT =", p["CT"])

        # Store Gantt Chart data
        gantt_chart.append( (p["PID"], start_time, p["CT"])  )

    show_gantt_chart(gantt_chart)
    calculate_result(processes)
 
def sjf(processes):

    print("\n")
    print("." * 70)
    print("                     SJF SOLUTION")
    print("." * 70)

    time = 0
    completed = 0

    gantt_chart = []

    while completed < len(processes):
        available = []

        # Find processes that have arrived
        for p in processes:

            if p["AT"] <= time and "CT" not in p:
                available.append(p)

        # No process is available
        if len(available) == 0:
            next_process = None

            for p in processes:
                if "CT" not in p:

                    if next_process is None:
                        next_process = p

                    elif p["AT"] < next_process["AT"]:
                        next_process = p

            print("\nCPU is idle from",time,"to",next_process["AT"] )
            gantt_chart.append(("IDLE", time, next_process["AT"])  )

            time = next_process["AT"]

            continue
        # Select process with smallest BT
        selected = available[0]

        for p in available:
            if p["BT"] < selected["BT"]:
                selected = p

        print("\n")
        print("-" * 60)
        print("STEP", completed + 1)
        print("-" * 60)
        print("\nAvailable Processes:")

        for p in available:
            print( p["PID"], "-> AT =", p["AT"], ", BT =", p["BT"])

        print("\nSelected Process:", selected["PID"])
        print("Why selected?")
        print("It has the smallest Burst Time.")

        start_time = time

        print("\nStart Time =", start_time)
        print("Burst Time =", selected["BT"])

        # Calculate CT
        time = time + selected["BT"]

        selected["CT"] = time

        print("\nCompletion Time:")
        print("CT =", start_time, "+", selected["BT"])
        print("CT =", selected["CT"])

        # Store Gantt Chart
        gantt_chart.append(
            (
                selected["PID"],
                start_time,
                selected["CT"]
            )
        )

        completed = completed + 1

    show_gantt_chart(gantt_chart)
    calculate_result(processes)

def priority_scheduling(processes):

    print("\n")
    print("." * 70)
    print("              PRIORITY SCHEDULING SOLUTION")
    print("." * 70)

    time = 0
    completed = 0

    gantt_chart = []

    while completed < len(processes):

        available = []

        # Find available processes
        for p in processes:

            if p["AT"] <= time and "CT" not in p:

                available.append(p)

        # No process is available
        if len(available) == 0:

            next_process = None

            for p in processes:
                if "CT" not in p:

                    if next_process is None:

                        next_process = p

                    elif p["AT"] < next_process["AT"]:

                        next_process = p

            print( "\nCPU is idle from",time,"to",next_process["AT"])

            gantt_chart.append(
                ("IDLE", time, next_process["AT"])
            )

            time = next_process["AT"]

            continue

        # Select highest priority
        # Smaller number = higher priority
        selected = available[0]

        for p in available:

            if p["Priority"] < selected["Priority"]:

                selected = p

        print("\n")
        print("-" * 60)
        print("STEP", completed + 1)
        print("-" * 60)

        print("\nAvailable Processes:")

        for p in available:

            print(p["PID"],"-> Priority =", p["Priority"],", BT =", p["BT"])

        print("\nSelected Process:", selected["PID"])
        print("Why selected?")
        print("It has the highest priority.")

        start_time = time

        print("\nStart Time =", start_time)
        print("Burst Time =", selected["BT"])

        # Calculate CT
        time = time + selected["BT"]

        selected["CT"] = time

        print("\nCompletion Time:")
        print("CT =", start_time, "+", selected["BT"])
        print("CT =", selected["CT"])

        # Store Gantt Chart
        gantt_chart.append(
            (
                selected["PID"],
                start_time,
                selected["CT"]
            )
        )

        completed = completed + 1

    show_gantt_chart(gantt_chart)
    calculate_result(processes)
 

def round_robin(processes, quantum):

    print("\n")
    print("." * 70)
    print("                  ROUND ROBIN SOLUTION")
    print("." * 70)

    # Arrange according to Arrival Time
    processes.sort(key=lambda x: x["AT"])

    # Store remaining burst time
    for p in processes:
        p["Remaining"] = p["BT"]
        queue = []
        gantt_chart = []
        time = 0
        completed = 0
        index = 0

    print("\nTime Quantum =", quantum)

    while completed < len(processes):
        # Add newly arrived processes
        while (index < len(processes)and processes[index]["AT"] <= time):

            queue.append(processes[index])
            index = index + 1

        # If Ready Queue is empty
        if len(queue) == 0:
             if index < len(processes):

                print("\nCPU is idle from",time,"to",processes[index]["AT"])
                gantt_chart.append(
                    (
                        "IDLE",time,processes[index]["AT"]
                    )
                )
                time = processes[index]["AT"]
                continue

        # Take first process from queue
        p = queue.pop(0)

        print("\n")
        print("-" * 60)
        print("CURRENT PROCESS:", p["PID"])
        print("-" * 60)

        print("Current Time =", time)
        print("Remaining Burst Time =", p["Remaining"])
        print("\nWhy selected?")
        print( p["PID"], "is at the front of the Ready Queue." )

        start_time = time

        # Process can finish
        if p["Remaining"] <= quantum:

            print( "\nProcess can finish in this turn.")

            time = time + p["Remaining"]

            p["Remaining"] = 0

            p["CT"] = time

            print("Execution Time =", time - start_time)
            print( "Completion Time =", p["CT"] )
            completed = completed + 1

        # Process cannot finish
        else:
            print( "\nProcess cannot finish in this turn.")

            time = time + quantum
            p["Remaining"] = (p["Remaining"] - quantum )

            print("Execution Time =",quantum )

            print("Remaining Burst Time =", p["Remaining"] )
            # Add newly arrived processes
            while ( index < len(processes)and processes[index]["AT"] <= time):

                queue.append(processes[index])
                index = index + 1
                queue.append(p)
        # Add execution to Gantt Chart
        gantt_chart.append( ( p["PID"],start_time,time))

    show_gantt_chart(gantt_chart)
    calculate_result(processes)
 

def get_integer(message):

    while True:

        try:

            value = int(input(message))

            if value < 0:
                print("Please enter 0 or a positive number.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")

def take_process_input(choice):

    print("\n")
    print("." * 70)
    print("                 ENTER PROCESS DETAILS")
    print("." * 70)

    n = get_integer( "\nEnter number of processes: " )

    while n == 0:

        print("Number of processes must be greater than 0.")

        n = get_integer("Enter number of processes again: ")
        
    processes = []

    for i in range(n):

        print("\nProcess", i + 1)
        print("-" * 30)

        pid = input("Enter Process ID: ")

        at = get_integer("Enter Arrival Time: ")

        bt = get_integer( "Enter Burst Time: " )
        while bt == 0:

            print( "Burst Time must be greater than 0.")
            bt = get_integer("Enter Burst Time again: ")

        # Store process information
        process = {
            "PID": pid,
            "AT": at,
            "BT": bt
        }
        # Priority required only for Priority Scheduling
        if choice == 3:

            priority = get_integer("Enter Priority: ")

            process["Priority"] = priority

        processes.append(process)

    return processes
 

def show_input_data(processes, choice):

    print("\n")
    print("-" * 70)
    print("                  ENTERED PROCESS DATA")
    print("-" * 70)

    if choice == 3:

        print("\nProcess\tAT\tBT\tPriority")
        print("-" * 40)

        for p in processes:

            print( p["PID"], "\t",
                   p["AT"], "\t",
                   p["BT"], "\t",
                   p["Priority"] )
    else:

        print("\nProcess\tAT\tBT")
        print("-" * 30)

        for p in processes:

            print( p["PID"], "\t",
                   p["AT"], "\t",
                   p["BT"] )


def main():

    while True:

        show_menu()
        choice = get_integer("\nEnter your choice: " )
        
        if choice == 5:

            print("\n")
            print("~" * 65)
            print("Thank you for using")
            print("CPU Scheduling Learning System!...")
            print("~" * 65)

            break

        if choice < 1 or choice > 5:

            print("\nInvalid choice!")
            print( "Please select between 1 and 5.")

            continue

        print("\nLoading theory...")
        show_theory(choice)

        print("\n")
        print("~" * 65)
        solve = input("Do you want to solve your own problem? (yes/no): " ).lower()

        if solve != "yes":
            print("\nReturning to main menu..." )

            continue
        
        processes = take_process_input(choice)

        show_input_data( processes,choice)

        quantum = 0

        if choice == 4:
            quantum = get_integer("\nEnter Time Quantum: " )

            while quantum == 0:
                print( "Time Quantum must be greater than 0." )
                quantum = get_integer("Enter Time Quantum again: " )

        print("\n")
        print("." * 70)
        print("                  SOLVING PROBLEM")
        print("." * 70)

        if choice == 1:
            fcfs(processes)

        elif choice == 2:
            sjf(processes)

        elif choice == 3:
            priority_scheduling(processes)

        elif choice == 4:
             round_robin(processes,quantum)

        print("\n")
        print("=" * 70)
        print("                SOLUTION COMPLETED")
        print("=" * 70)

        again = input("\nDo you want to try another problem? (yes/no): ").lower()

        if again != "yes":
            print("\n")
            print( "Thank you for using")
            print("CPU Scheduling Learning System....")
            print("~" * 65)
            break
 
main()
 