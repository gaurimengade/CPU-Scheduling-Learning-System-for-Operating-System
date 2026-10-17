import tkinter as tk

from tkinter import ttk, messagebox

from collections import deque









APP_BG = "#F1F5F9"

SIDEBAR = "#E2E8F0"

CARD_BG = "#FFFFFF"

ACCENT = "#0284C7"

TEXT = "#1E293B"

MUTED = "#64748B"

GREEN = "#16A34A"

ORANGE = "#D97706"

RED = "#DC2626"






THEORY = {

    "FCFS": {

        "full": "First Come First Serve",

        "type": "Non-preemptive",

        "summary": (

            "MEANING :-\n"

            "FCFS stands for First Come First Serve.\n"

            "It is one of the simplest CPU Scheduling Algorithms.\n"

"The process that arrives first gets the CPU first.\n\n"



"It follows:-"

"First In -> First Out (FIFO)\n\n"





"TYPE :-\n"

"FCFS is a NON-PREEMPTIVE scheduling algorithm.\n"



"Non-preemptive means that once a process gets the CPU,it continues execution until it finishes."

        ),

        "steps": [

           "Step 1:\n"
           "Check the Arrival Time of all processes.\n\n"



"Step 2:\n"
"Find the process that arrived first.\n\n"



"Step 3:\n"
"Give the CPU to that process.\n\n"



"Step 4:\n"
"Execute the process completely.\n\n"



"Step 5:\n"
"After it finishes, select the next available process.\n\n"



"Step 6:\n"
"Continue until all processes are completed."

        ],

        "example": (

            "P1: AT=0, BT=4\n"

            "P2: AT=1, BT=3\n"

            "P3: AT=2, BT=2\n\n"

            "Execution: P1 -> P2 -> P3"

        ),

        "pros": [

            "1. Very simple to understand.\n"

"2. Easy to implement.\n"

"3. Easy to calculate.\n"

"4. Processes are handled according to arrival order.\n"

        ],

        "cons": [

            "Short processes may wait behind long processes.",

            "Average waiting time can be high.",

            "May cause the convoy effect."

        ],

        "extra": (

            "Preemptive: No.\n"

            "Selection: Earliest arrival time.\n\n"

            "CONVOY EFFECT :-\n"

"-------------\n"

"Convoy Effect is an important disadvantage of FCFS.\n"

"It occurs when a long CPU-bound process comes first and makes many short processes wait for a long time.\n"



"Example:\n"

"P1 -> BT = 10\n"

"P2 -> BT = 2\n"

"P3 -> BT = 1\n"



"FCFS Order:\n"

"P1 -> P2 -> P3\n"



"P1 takes 10 units of CPU time.\n"

"Therefore, P2 and P3 have to wait until P1 finishes.\n"

"This situation is called the Convoy Effect.\n\n"





"WHY DOES CONVOY EFFECT OCCUR?\n"

"-----------------------------\n"

"FCFS mainly considers Arrival Time.\n"

"It does not consider whether a process has a small or large Burst Time.\n"

"Therefore, a long process arriving first can make\n"

"short processes wait.\n\n"





"EFFECTS OF CONVOY EFFECT :-\n"

"------------------------\n"

"1. Waiting time increases.\n"

"2. Average waiting time increases.\n"

"3. Short processes experience unnecessary delay.\n"

"4. Overall system performance can decrease.\n\n\n"

"IMPORTANT POINT\n" "---------------\n" "SJF selects according to:\n" " Smallest Burst Time\n" " But the process must first have arrived.\n" " A process that has not arrived cannot be selected.\n\n" "IMPORTANT FORMULAS :-\n" "-------------------\n" "Completion Time:\n" "CT = Time at which the process finishes\n\n" "Turnaround Time:\n" "TAT = CT - AT\n\n" "Waiting Time:\n" "WT = TAT - BT\n\n" "Average Waiting Time:\n" "Average WT = Total WT / Number of Processes\n\n" "Average Turnaround Time:\n" "Average TAT = Total TAT / Number of Processes\n"



        )

    },



    "SJF": {

        "full": "Shortest Job First",

        "type": "Non-preemptive",

        "summary": (

            "MEANING :-\n" 

            "-------\n" 

            "SJF stands for Shortest Job First.\n" 

            "In SJF, the process having the smallest Burst Time is selected first.\n\n" 

            "Main idea:\n" 

            "Shortest Burst Time -> Execute First\n\n" 

            "TYPE :-\n" "----\n" 

            "The SJF implemented in this project is NON-PREEMPTIVE.\n"

            "Once a process starts execution, it continues until it finishes.\n\n"

        ),

        "steps": [

            "Step 1:\n" "Check which processes have arrived.\n\n" "Step 2:\n" "Look at the Burst Time of available processes.\n\n" "Step 3:\n" "Select the process having the smallest Burst Time.\n\n" "Step 4:\n" "Execute that process completely.\n\n" "Step 5:\n" "Again check the available processes.\n\n" "Step 6:\n" "Select the process with the smallest Burst Time.\n\n" "Step 7:\n" "Continue until all processes are completed.\n\n"

        ],

        "example": (

           "Suppose:\n" "P1 -> AT = 0, BT = 6\n" "P2 -> AT = 0, BT = 3\n" "P3 -> AT = 0, BT = 2\n\n" "All processes are available.\n\n" "Burst Times:\n" "P1 = 6\n" "P2 = 3\n" "P3 = 2\n\n" "Smallest Burst Time = P3\n\n" "Therefore:\n" "Execution Order = P3 -> P2 -> P1\n\n"

        ),

        "pros": [

           "1. Short processes finish quickly.\n" "2. It can reduce average waiting time.\n" "3. Easy to understand for simple examples.\n\n"

        ],

        "cons": [

            "1. Burst Time needs to be known or estimated.\n" "2. Long processes may wait for a long time.\n" "3. Starvation can occur.\n\n"

        ],

        "extra": (

            "Preemptive: No.\n"

            "Selection: Smallest burst time among arrived processes.\n\n"

            "STARVATION :-\n" "----------\n" "Starvation means that a process waits for a very long time because other processes keep getting selected.\n\n" "For example:\n" "If short processes keep arriving continuously, a long process may continue waiting.\n" "Therefore, SJF can cause starvation.\n\n" "IMPORTANT POINT\n" "---------------\n" "SJF selects according to:\n" " Smallest Burst Time\n" " But the process must first have arrived.\n" " A process that has not arrived cannot be selected.\n\n\n"

        "IMPORTANT POINT\n" "---------------\n" "SJF selects according to:\n" " Smallest Burst Time\n" " But the process must first have arrived.\n" " A process that has not arrived cannot be selected.\n\n" "IMPORTANT FORMULAS :-\n" "-------------------\n" "Completion Time:\n" "CT = Time at which the process finishes\n\n" "Turnaround Time:\n" "TAT = CT - AT\n\n" "Waiting Time:\n" "WT = TAT - BT\n\n" "Average Waiting Time:\n" "Average WT = Total WT / Number of Processes\n\n" "Average Turnaround Time:\n" "Average TAT = Total TAT / Number of Processes\n"

        )

    },



    "Priority": {

        "full": "Priority Scheduling",

        "type": "Non-preemptive",

        "summary": (

            "MEANING :-\n" "-------\n" "In Priority Scheduling, every process is assigned a priority number.\n" "The CPU selects the process according to its priority.\n\n" "PRIORITY RULE USED IN THIS PROJECT :-\n" "----------------------------------\n" "Smaller Priority Number = Higher Priority\n\n" "For example:-\n" "Priority 1 -> Highest\n" "Priority 2 -> Second Highest\n" "Priority 3 -> Third Highest\n\n" "TYPE :-\n" "----\n" "The Priority Scheduling implemented in this project is NON-PREEMPTIVE.\n" "Once a process starts execution, it continues until it finishes.\n\n"

        ),

        "steps": [

            "Step 1:\n" "Check which processes have arrived.\n\n" "Step 2:\n" "Check their priority values.\n\n" "Step 3:\n" "Select the process with the highest priority.\n\n" "Step 4:\n" "Execute the selected process completely.\n\n" "Step 5:\n" "Check the remaining available processes.\n\n" "Step 6:\n" "Select the next highest-priority process.\n\n" "Step 7:\n" "Continue until all processes are completed.\n\n"

        ],

        "example": (

          "Suppose:\n" "P1 -> AT = 0, BT = 5, Priority = 3\n" "P2 -> AT = 0, BT = 3, Priority = 1\n" "P3 -> AT = 0, BT = 2, Priority = 2\n\n" "Priority order:\n" "P2 -> Priority 1\n" "P3 -> Priority 2\n" "P1 -> Priority 3\n\n" "Therefore:\n" "Execution Order = P2 -> P3 -> P1\n\n"

        ),

        "pros": [

          "1. Important processes can execute first.\n" "2. Useful when processes have different importance.\n" "3. Easy to understand and implement.\n\n"

        ],

        "cons": [

            "1. Low-priority processes may wait for a long time.\n" "2. Starvation can occur.\n" "3. Priority values must be assigned correctly.\n\n"

        ],

        "extra": (

            "Preemptive: No.\n"

            "Selection: Smallest priority number among arrived processes.\n\n"

           "STARVATION :-\n" "----------\n" "A low-priority process may keep waiting if higher-priority processes continue to arrive.\n" "This problem is called starvation.\n\n" "IMPORTANT POINT\n" "---------------\n" "In this project:\n" " Lower Priority Number = Higher Priority\n\n\n" "IMPORTANT FORMULAS :-\n" "-------------------\n" "Completion Time:\n" "CT = Time at which the process finishes\n\n" "Turnaround Time:\n" "TAT = CT - AT\n\n" "Waiting Time:\n" "WT = TAT - BT\n\n" "Average Waiting Time:\n" "Average WT = Total WT / Number of Processes\n\n" "Average Turnaround Time:\n" "Average TAT = Total TAT / Number of Processes\n"

        )

    },



    "Round Robin": {

        "full": "Round Robin Scheduling",

        "type": "Preemptive",

        "summary": (

           "MEANING :-\n" "-------\n" "Round Robin is a CPU Scheduling Algorithm mainly used for time-sharing systems.\n" "Each process gets a fixed amount of CPU time.\n" "This fixed amount of time is called TIME QUANTUM.\n\n" "TYPE :-\n" "----\n" "Round Robin is a PREEMPTIVE scheduling algorithm.\n" "Preemptive means the CPU can stop the currently running process and give the CPU to another process.\n\n" "TIME QUANTUM :-\n" "------------\n" "Time Quantum is the maximum amount of CPU time given to a process during one turn.\n\n"

        ),

        "steps": [

          "Step 1:\n" "Processes are placed in the Ready Queue.\n\n" "Step 2:\n" "The first process gets the CPU.\n\n" "Step 3:\n" "It runs for the given Time Quantum.\n\n" "Step 4:\n" "If the process finishes, it is removed.\n\n" "Step 5:\n" "If it does not finish, its remaining Burst Time\n" "is calculated.\n\n" "Step 6:\n" "The unfinished process goes to the end of\n" "the Ready Queue.\n\n" "Step 7:\n" "The next process gets the CPU.\n\n" "Step 8:\n" "Continue until all processes are completed.\n\n"

        ],

        "example": (

            "P1: AT=0, BT=5\n"

            "P2: AT=0, BT=3\n"

            "Time Quantum = 2\n\n" "A process can execute for up to 2 time units\n" "in one turn.\n\n"

            "P1: 0-2\n"

            "P2: 2-4\n"

            "P1: 4-6\n"

            "P2: 6-7\n"

            "P1: 7-8"

        ),

        "pros": [

            "1. Fair CPU allocation.\n" "2. Suitable for time-sharing systems.\n" "3. Every process gets a chance to execute.\n" "4. No process can hold the CPU for too long.\n\n"

        ],

        "cons": [

            "1. Very small Time Quantum can cause many context switches.\n" "2. Very large Time Quantum makes it similar to FCFS.\n" "3. Choosing the correct Time Quantum is important.\n\n"

        ],

        "extra": (

            "Preemptive: Yes.\n"

            "Selection: First process in the ready queue.\n\n"

          "CONTEXT SWITCH :-\n" "--------------\n" "A context switch happens when the CPU changes from one process to another.\n\n" "For example:\n" "P1 -> CPU\n\n" "Then CPU changes to:\n" "P2 -> CPU\n\n" "This change is called a context switch.\n\n\n" "IMPORTANT FORMULAS :-\n" "-------------------\n" "Completion Time:\n" "CT = Time at which the process finishes\n\n" "Turnaround Time:\n" "TAT = CT - AT\n\n" "Waiting Time:\n" "WT = TAT - BT\n\n" "Average Waiting Time:\n" "Average WT = Total WT / Number of Processes\n\n" "Average Turnaround Time:\n" "Average TAT = Total TAT / Number of Processes\n"

        )

    }

}





# ==================== SCHEDULING ALGORITHMS ====================



def simulate(algorithm, input_processes, quantum=2):



    if not input_processes:

        raise ValueError("Please add at least one process.")



    # Make a fresh copy for each simulation.

    processes = []



    for index, p in enumerate(input_processes):



        process = {

            "PID": str(p["PID"]),

            "AT": int(p["AT"]),

            "BT": int(p["BT"]),

            "Priority": (

                int(p["Priority"])

                if algorithm == "Priority"

                else None

            ),

            "remaining": int(p["BT"]),

            "CT": None,

            "TAT": 0,

            "WT": 0,

            "order": index

        }



        if process["AT"] < 0:

            raise ValueError(

                f'{process["PID"]}: Arrival time cannot be negative.'

            )



        if process["BT"] <= 0:

            raise ValueError(

                f'{process["PID"]}: Burst time must be greater than zero.'

            )



        if (

            algorithm == "Priority"

            and process["Priority"] <= 0

        ):

            raise ValueError(

                f'{process["PID"]}: Priority must be greater than zero.'

            )



        processes.append(process)



    if algorithm == "Round Robin" and quantum <= 0:

        raise ValueError("Time quantum must be greater than zero.")



    time = 0

    completed = 0

    total = len(processes)



    gantt = []

    steps = []



    def add_segment(pid, start, end):

        if end > start:

            gantt.append({

                "PID": pid,

                "Start": start,

                "End": end

            })



    def add_idle(until):

        nonlocal time



        if until > time:

            add_segment("IDLE", time, until)



            steps.append(

                f"CPU is idle from {time} to {until} "

                "because no process has arrived."

            )



            time = until



    # ---------------- FCFS ----------------



    if algorithm == "FCFS":



        ordered = sorted(

            processes,

            key=lambda p: (p["AT"], p["order"])

        )



        for p in ordered:



            if time < p["AT"]:

                add_idle(p["AT"])



            start = time

            time += p["BT"]



            p["CT"] = time



            add_segment(p["PID"], start, time)



            steps.append(

                f'{p["PID"]} executes from {start} to {time}. '

                f'BT = {p["BT"]}. CT = {time}.'

            )



    # ---------------- SJF ----------------



    elif algorithm == "SJF":



        while completed < total:



            available = [

                p for p in processes

                if p["CT"] is None and p["AT"] <= time

            ]



            if not available:



                next_arrival = min(

                    p["AT"]

                    for p in processes

                    if p["CT"] is None

                )



                add_idle(next_arrival)

                continue



            p = min(

                available,

                key=lambda x: (

                    x["BT"],

                    x["AT"],

                    x["order"]

                )

            )



            start = time

            time += p["BT"]



            p["CT"] = time

            completed += 1



            add_segment(p["PID"], start, time)



            steps.append(

                f'SJF selects {p["PID"]} because its burst time '

                f'is {p["BT"]}. Execution: {start}-{time}.'

            )



    # ---------------- PRIORITY ----------------



    elif algorithm == "Priority":



        while completed < total:



            available = [

                p for p in processes

                if p["CT"] is None and p["AT"] <= time

            ]



            if not available:



                next_arrival = min(

                    p["AT"]

                    for p in processes

                    if p["CT"] is None

                )



                add_idle(next_arrival)

                continue



            p = min(

                available,

                key=lambda x: (

                    x["Priority"],

                    x["AT"],

                    x["order"]

                )

            )



            start = time

            time += p["BT"]



            p["CT"] = time

            completed += 1



            add_segment(p["PID"], start, time)



            steps.append(

                f'{p["PID"]} is selected with priority '

                f'{p["Priority"]}. Execution: {start}-{time}.'

            )



    # ---------------- ROUND ROBIN ----------------



    elif algorithm == "Round Robin":



        ordered = sorted(

            processes,

            key=lambda p: (p["AT"], p["order"])

        )



        ready = deque()

        index = 0



        while completed < total:



            # Add every process that has arrived.

            while (

                index < total

                and ordered[index]["AT"] <= time

            ):

                ready.append(ordered[index])

                index += 1



            # If no process is ready, move to the next arrival.

            if not ready:



                if index < total:

                    add_idle(ordered[index]["AT"])

                    continue



                break



            p = ready.popleft()



            start = time

            run_time = min(quantum, p["remaining"])



            time += run_time

            p["remaining"] -= run_time



            add_segment(p["PID"], start, time)



            steps.append(

                f'{p["PID"]} executes from {start} to {time}. '

                f'Executed for {run_time} units. '

                f'Remaining BT = {p["remaining"]}.'

            )



            # New arrivals join the queue before the running process

            # is placed back into the queue.

            while (

                index < total

                and ordered[index]["AT"] <= time

            ):

                ready.append(ordered[index])

                index += 1



            if p["remaining"] == 0:



                p["CT"] = time

                completed += 1



                steps.append(

                    f'{p["PID"]} completes at time {time}.'

                )



            else:

                ready.append(p)



    else:

        raise ValueError("Unknown scheduling algorithm.")



    # ---------------- CALCULATE RESULTS ----------------



    for p in processes:



        p["TAT"] = p["CT"] - p["AT"]

        p["WT"] = p["TAT"] - p["BT"]



    results = sorted(

        processes,

        key=lambda p: p["order"]

    )







    for p in results:



        steps.append(

            f'{p["PID"]}: CT={p["CT"]}, '

            f'TAT={p["TAT"]}, WT={p["WT"]}'

        )



    return results, gantt, steps





# ==================== MAIN APPLICATION ====================



class CPUSchedulingApp:



    def __init__(self, root):



        self.root = root

        self.root.title("CPU Scheduling Learning System")

        self.root.geometry("1280x820")

        self.root.minsize(1000, 680)

        self.root.configure(bg=APP_BG)



        self.processes = []



        self.current_algorithm = tk.StringVar(value="FCFS")

        self.quantum = tk.StringVar(value="2")



        self._style()

        self._build_layout()

        self._build_process_tab()

        self._build_results_tab()

        self._build_learn_tab()



        self.show_theory()

        self._refresh_input_tree()



    # ---------------- STYLE ----------------



    def _style(self):



        style = ttk.Style()

        style.theme_use("clam")



        style.configure(

            "Treeview",

            background=CARD_BG,

            foreground=TEXT,

            fieldbackground=CARD_BG,

            rowheight=30,

            font=("Segoe UI", 10)

        )



        style.configure(

            "Treeview.Heading",

            background=SIDEBAR,

            foreground=TEXT,

            font=("Segoe UI", 10, "bold")

        )



        style.map(

            "Treeview",

            background=[("selected", ACCENT)],

            foreground=[("selected", APP_BG)]

        )



        style.configure(

            "TNotebook",

            background=APP_BG,

            borderwidth=0

        )



        style.configure(

            "TNotebook.Tab",

            background=SIDEBAR,

            foreground=TEXT,

            padding=(15, 9),

            font=("Segoe UI", 10, "bold")

        )



        style.map(

            "TNotebook.Tab",

            background=[("selected", ACCENT)],

            foreground=[("selected", APP_BG)]

        )



    # ---------------- LAYOUT ----------------



    def _build_layout(self):



        self.sidebar = tk.Frame(

            self.root,

            bg=SIDEBAR,

            width=250

        )



        self.sidebar.pack(side="left", fill="y")

        self.sidebar.pack_propagate(False)



        tk.Label(

            self.sidebar,

            text="CPU SCHEDULING",

            bg=SIDEBAR,

            fg=ACCENT,

            font=("Segoe UI", 17, "bold")

        ).pack(anchor="w", padx=20, pady=(25, 5))



        tk.Label(

            self.sidebar,

            text="LEARNING SYSTEM",

            bg=SIDEBAR,

            fg=MUTED,

            font=("Segoe UI", 9, "bold")

        ).pack(anchor="w", padx=20, pady=(0, 25))



        tk.Label(

            self.sidebar,

            text="Select Algorithm",

            bg=SIDEBAR,

            fg=TEXT,

            font=("Segoe UI", 11, "bold")

        ).pack(anchor="w", padx=20, pady=(5, 8))



        for algorithm in THEORY:



            tk.Radiobutton(

                self.sidebar,

                text=algorithm,

                variable=self.current_algorithm,

                value=algorithm,

                command=self.show_theory,

                bg=SIDEBAR,

                fg=TEXT,

                selectcolor=CARD_BG,

                activebackground=SIDEBAR,

                activeforeground=ACCENT,

                font=("Segoe UI", 10)

            ).pack(anchor="w", padx=20, pady=5)



        tk.Label(

            self.sidebar,

            text="Time Quantum (Round Robin)",

            bg=SIDEBAR,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack(anchor="w", padx=20, pady=(25, 5))



        self.quantum_entry = tk.Entry(

            self.sidebar,

            textvariable=self.quantum,

            bg=CARD_BG,

            fg=TEXT,

            insertbackground=TEXT,

            relief="flat",

            font=("Segoe UI", 10)

        )



        self.quantum_entry.pack(

            fill="x",

            padx=20,

            ipady=7

        )



        self._button(

            self.sidebar,

            "Run Simulation",

            self.run_simulation,

            ACCENT,

            APP_BG

        ).pack(fill="x", padx=20, pady=(25, 8))



        self._button(

            self.sidebar,

            "Load Sample Data",

            self.load_sample,

            CARD_BG,

            TEXT

        ).pack(fill="x", padx=20, pady=5)



        self._button(

            self.sidebar,

            "Clear All Processes",

            self.clear_all,

            CARD_BG,

            RED

        ).pack(fill="x", padx=20, pady=5)



        tk.Label(

            self.sidebar,

            text="Learn | Simulate | Understand",

            bg=SIDEBAR,

            fg=MUTED,

            font=("Segoe UI", 8)

        ).pack(side="bottom", pady=20)



        self.main = tk.Frame(

            self.root,

            bg=APP_BG

        )



        self.main.pack(

            side="left",

            fill="both",

            expand=True,

            padx=20,

            pady=18

        )



        tk.Label(

            self.main,

            text="CPU Scheduling Learning System",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 20, "bold")

        ).pack(anchor="w")



        tk.Label(

            self.main,

            text="Understand scheduling algorithms through interactive examples.",

            bg=APP_BG,

            fg=MUTED,

            font=("Segoe UI", 10)

        ).pack(anchor="w", pady=(2, 15))



        self.notebook = ttk.Notebook(self.main)

        self.notebook.pack(fill="both", expand=True)



        self.process_tab = tk.Frame(

            self.notebook,

            bg=APP_BG

        )



        self.results_tab = tk.Frame(

            self.notebook,

            bg=APP_BG

        )



        self.learn_tab = tk.Frame(

            self.notebook,

            bg=APP_BG

        )



        self.notebook.add(

            self.process_tab,

            text="Process Input"

        )



        self.notebook.add(

            self.results_tab,

            text="Results & Gantt Chart"

        )



        self.notebook.add(

            self.learn_tab,

            text="Learn Algorithm"

        )



  



    def _button(self, parent, text, command, bg, fg):



        return tk.Button(

            parent,

            text=text,

            command=command,

            bg=bg,

            fg=fg,

            activebackground=ACCENT,

            activeforeground=APP_BG,

            relief="flat",

            cursor="hand2",

            font=("Segoe UI", 10, "bold"),

            padx=10,

            pady=10

        )



    # ---------------- PROCESS TAB ----------------



    def _build_process_tab(self):



        tk.Label(

            self.process_tab,

            text="Add Process",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        ).pack(anchor="w", padx=15, pady=(15, 10))



        form = tk.Frame(

            self.process_tab,

            bg=CARD_BG

        )



        form.pack(

            fill="x",

            padx=15,

            pady=(0, 15)

        )



        self.pid_entry = self._field(form, "Process ID", 0)

        self.at_entry = self._field(form, "Arrival Time", 1)

        self.bt_entry = self._field(form, "Burst Time", 2)

        self.priority_entry = self._field(form, "Priority", 3)



        # Store the Priority field container separately.

        self.priority_box = self.priority_entry.master



        self.add_button = self._button(

            form,

            "Add Process",

            self.add_process,

            ACCENT,

            APP_BG

        )



        self.add_button.grid(

            row=1,

            column=8,

            padx=10,

            pady=12,

            sticky="ew"

        )



        for col in range(9):

            form.grid_columnconfigure(col, weight=1)



        tk.Label(

            self.process_tab,

            text="Process List",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        ).pack(anchor="w", padx=15, pady=(0, 8))



        table_frame = tk.Frame(

            self.process_tab,

            bg=CARD_BG

        )



        table_frame.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=(0, 10)

        )



        columns = ("PID", "AT", "BT", "Priority")



        self.input_tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            selectmode="browse"

        )



        headings = {

            "PID": "Process ID",

            "AT": "Arrival Time",

            "BT": "Burst Time",

            "Priority": "Priority"

        }



        for col in columns:

            self.input_tree.heading(col, text=headings[col])

            self.input_tree.column(

                col,

                width=130,

                anchor="center"

            )



        self.input_tree.pack(

            side="left",

            fill="both",

            expand=True,

            padx=8,

            pady=8

        )



        scrollbar = ttk.Scrollbar(

            table_frame,

            orient="vertical",

            command=self.input_tree.yview

        )



        scrollbar.pack(

            side="right",

            fill="y",

            pady=8

        )



        self.input_tree.configure(

            yscrollcommand=scrollbar.set

        )



        self._button(

            self.process_tab,

            "Delete Selected Process",

            self.delete_selected,

            CARD_BG,

            RED

        ).pack(

            anchor="e",

            padx=15,

            pady=(0, 12)

        )



    def _field(self, parent, label, column):



        box = tk.Frame(parent, bg=CARD_BG)



        tk.Label(

            box,

            text=label,

            bg=CARD_BG,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack(anchor="w", pady=(0, 5))



        entry = tk.Entry(

            box,

            bg=APP_BG,

            fg=TEXT,

            insertbackground=TEXT,

            disabledbackground="#E2E8F0",

            disabledforeground="#94A3B8",

            relief="flat",

            font=("Segoe UI", 10),

            width=12

        )



        entry.pack(fill="x", ipady=7)



        box.grid(

            row=0,

            column=column,

            padx=10,

            pady=12,

            sticky="ew"

        )



        return entry



    # ---------------- RESULTS TAB ----------------



    def _build_results_tab(self):



        tk.Label(

            self.results_tab,

            text="Scheduling Results",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        ).pack(anchor="w", padx=15, pady=(12, 8))



        metrics = tk.Frame(self.results_tab, bg=APP_BG)



        metrics.pack(

            fill="x",

            padx=15,

            pady=(0, 12)

        )



        self.avg_wt_label = self._metric(

            metrics, "Average Waiting Time", "-"

        )



        self.avg_tat_label = self._metric(

            metrics, "Average Turnaround Time", "-"

        )



        self.process_count_label = self._metric(

            metrics, "Processes", "0"

        )



        result_frame = tk.Frame(

            self.results_tab,

            bg=CARD_BG

        )



        result_frame.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=(0, 10)

        )



        columns = (

            "PID", "AT", "BT", "Priority", "CT", "TAT", "WT"

        )



        self.result_tree = ttk.Treeview(

            result_frame,

            columns=columns,

            show="headings",

            height=5

        )



        for col in columns:

            self.result_tree.heading(col, text=col)

            self.result_tree.column(

                col,

                width=85,

                anchor="center"

            )



        self.result_tree.pack(

            side="left",

            fill="both",

            expand=True,

            padx=8,

            pady=8

        )



        result_scroll = ttk.Scrollbar(

            result_frame,

            orient="vertical",

            command=self.result_tree.yview

        )



        result_scroll.pack(side="right", fill="y", pady=8)



        self.result_tree.configure(

            yscrollcommand=result_scroll.set

        )



        tk.Label(

            self.results_tab,

            text="Gantt Chart",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        ).pack(anchor="w", padx=15, pady=(0, 5))



        self.gantt_canvas = tk.Canvas(

            self.results_tab,

            height=100,

            bg=CARD_BG,

            highlightthickness=0

        )



        self.gantt_canvas.pack(

            fill="x",

            padx=15,

            pady=(0, 10)

        )



        tk.Label(

            self.results_tab,

            text="Step-by-Step Execution",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        ).pack(anchor="w", padx=15, pady=(0, 5))



        steps_frame = tk.Frame(

            self.results_tab,

            bg=CARD_BG

        )



        steps_frame.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=(0, 12)

        )



        self.steps_text = tk.Text(

            steps_frame,

            height=5,

            bg=CARD_BG,

            fg=TEXT,

            insertbackground=TEXT,

            relief="flat",

            wrap="word",

            font=("Consolas", 10)

        )



        self.steps_text.pack(

            side="left",

            fill="both",

            expand=True,

            padx=8,

            pady=8

        )



        steps_scroll = ttk.Scrollbar(

            steps_frame,

            orient="vertical",

            command=self.steps_text.yview

        )



        steps_scroll.pack(side="right", fill="y", pady=8)



        self.steps_text.configure(

            yscrollcommand=steps_scroll.set

        )



    def _metric(self, parent, title, value):



        card = tk.Frame(parent, bg=CARD_BG)



        card.pack(

            side="left",

            fill="x",

            expand=True,

            padx=(0, 8)

        )



        tk.Label(

            card,

            text=title,

            bg=CARD_BG,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack(anchor="w", padx=12, pady=(10, 2))



        label = tk.Label(

            card,

            text=value,

            bg=CARD_BG,

            fg=ACCENT,

            font=("Segoe UI", 17, "bold")

        )



        label.pack(anchor="w", padx=12, pady=(0, 10))



        return label



    # ---------------- LEARN TAB ----------------



    def _build_learn_tab(self):



        heading = tk.Frame(self.learn_tab, bg=APP_BG)



        heading.pack(

            fill="x",

            padx=15,

            pady=(15, 8)

        )



        self.theory_title = tk.Label(

            heading,

            text="Algorithm Theory",

            bg=APP_BG,

            fg=TEXT,

            font=("Segoe UI", 13, "bold")

        )



        self.theory_title.pack(anchor="w")



        self.theory_type = tk.Label(

            heading,

            text="",

            bg=APP_BG,

            fg=ACCENT,

            font=("Segoe UI", 10, "bold")

        )



        self.theory_type.pack(anchor="w", pady=(4, 0))



        text_frame = tk.Frame(self.learn_tab, bg=CARD_BG)



        text_frame.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=(0, 15)

        )



        self.theory_text = tk.Text(

            text_frame,

            bg=CARD_BG,

            fg=TEXT,

            font=("Segoe UI", 11),

            wrap="word",

            relief="flat",

            padx=18,

            pady=15

        )



        self.theory_text.pack(

            side="left",

            fill="both",

            expand=True

        )



        scrollbar = ttk.Scrollbar(

            text_frame,

            orient="vertical",

            command=self.theory_text.yview

        )



        scrollbar.pack(side="right", fill="y")



        self.theory_text.configure(

            yscrollcommand=scrollbar.set

        )



        self.theory_text.tag_configure(

            "heading",

            foreground=ACCENT,

            font=("Segoe UI", 12, "bold"),

            spacing1=12,

            spacing3=5

        )



        self.theory_text.tag_configure(

            "body",

            foreground=TEXT,

            font=("Segoe UI", 10)

        )



    def show_theory(self):



        algorithm = self.current_algorithm.get()

        data = THEORY[algorithm]



        self.theory_title.config(

            text=f'{algorithm} - {data["full"]}'

        )



        self.theory_type.config(

            text=f'Algorithm Type: {data["type"]}'

        )



        # Show Priority input only for Priority Scheduling.

        if algorithm == "Priority":



            self.priority_box.grid()



            self.priority_entry.config(state="normal")



        else:



            self.priority_entry.config(state="normal")

            self.priority_entry.delete(0, "end")

            self.priority_entry.config(state="disabled")



            self.priority_box.grid_remove()



        # Time quantum is editable only for Round Robin.

        if algorithm == "Round Robin":

            self.quantum_entry.config(state="normal")

        else:

            self.quantum_entry.config(state="disabled")



        self.theory_text.config(state="normal")

        self.theory_text.delete("1.0", "end")



        sections = [
            ("WHAT IT MEANS", data["summary"]),
            ("WORKING STEPS", "\n".join(data["steps"])),
            ("EXAMPLE", data["example"]),
            ("ADVANTAGES", "\n".join("- " + x for x in data["pros"])),
            ("LIMITATIONS", "\n".join("- " + x for x in data["cons"])),
            ("IMPORTANT CONCEPTS", data["extra"]),
            (
                "IMPORTANT FORMULAS",
                "-------------------\n"
                "Completion Time:\n"
                "CT = Time at which the process finishes\n\n"
                "Turnaround Time:\n"
                "TAT = CT - AT\n\n"
                "Waiting Time:\n"
                "WT = TAT - BT\n\n"
                "Average Waiting Time:\n"
                "Average WT = Total WT / Number of Processes\n\n"
                "Average Turnaround Time:\n"
                "Average TAT = Total TAT / Number of Processes\n"
            ),
        ]

        for title, content in sections:



            self.theory_text.insert(

                "end", title + "\n", "heading"

            )



            self.theory_text.insert(

                "end", content + "\n\n", "body"

            )



        self.theory_text.config(state="disabled")



    # ---------------- PROCESS OPERATIONS ----------------



    def _refresh_input_tree(self):



        for item in self.input_tree.get_children():

            self.input_tree.delete(item)



        for p in self.processes:



            priority_display = (

                p["Priority"]

                if p.get("Priority") is not None

                else "-"

            )



            self.input_tree.insert(

                "",

                "end",

                values=(

                    p["PID"],

                    p["AT"],

                    p["BT"],

                    priority_display

                )

            )



    def add_process(self):



        algorithm = self.current_algorithm.get()



        pid = self.pid_entry.get().strip()

        at = self.at_entry.get().strip()

        bt = self.bt_entry.get().strip()



        # Priority is required only for Priority Scheduling.

        priority = None



        if algorithm == "Priority":



            priority = self.priority_entry.get().strip()



            if not priority:



                messagebox.showwarning(

                    "Missing Priority",

                    "Enter a priority for this process."

                )



                return



        if not pid or not at or not bt:



            messagebox.showwarning(

                "Missing Input",

                "Enter Process ID, Arrival Time and Burst Time."

            )



            return



        if any(

            p["PID"].lower() == pid.lower()

            for p in self.processes

        ):



            messagebox.showerror(

                "Duplicate Process",

                "This Process ID already exists."

            )



            return



        try:



            at_value = int(at)

            bt_value = int(bt)



            if at_value < 0:

                raise ValueError(

                    "Arrival time cannot be negative."

                )



            if bt_value <= 0:

                raise ValueError(

                    "Burst time must be greater than zero."

                )



            if algorithm == "Priority":



                priority_value = int(priority)



                if priority_value <= 0:

                    raise ValueError(

                        "Priority must be greater than zero."

                    )



            else:

                priority_value = None



        except ValueError as error:



            messagebox.showerror(

                "Invalid Input",

                str(error)

            )



            return



        self.processes.append({

            "PID": pid,

            "AT": at_value,

            "BT": bt_value,

            "Priority": priority_value

        })



        # Clear the text fields.

        for entry in (

            self.pid_entry,

            self.at_entry,

            self.bt_entry

        ):

            entry.delete(0, "end")



        if algorithm == "Priority":

            self.priority_entry.delete(0, "end")



        self._refresh_input_tree()



    def delete_selected(self):



        selected = self.input_tree.selection()



        if not selected:



            messagebox.showinfo(

                "Select Process",

                "Select a process to delete."

            )



            return



        values = self.input_tree.item(

            selected[0],

            "values"

        )



        pid = values[0]



        self.processes = [

            p for p in self.processes

            if p["PID"] != pid

        ]



        self._refresh_input_tree()



    def clear_all(self):



        if not self.processes:

            return



        if messagebox.askyesno(

            "Clear All",

            "Remove all processes?"

        ):



            self.processes.clear()

            self._refresh_input_tree()



            for item in self.result_tree.get_children():

                self.result_tree.delete(item)



            self.gantt_canvas.delete("all")

            self.steps_text.delete("1.0", "end")



            self.avg_wt_label.config(text="-")

            self.avg_tat_label.config(text="-")

            self.process_count_label.config(text="0")



    def load_sample(self):



        algorithm = self.current_algorithm.get()



        if algorithm == "Priority":



            self.processes = [

                {"PID": "P1", "AT": 0, "BT": 5, "Priority": 2},

                {"PID": "P2", "AT": 1, "BT": 3, "Priority": 1},

                {"PID": "P3", "AT": 2, "BT": 8, "Priority": 3},

                {"PID": "P4", "AT": 3, "BT": 2, "Priority": 2}

            ]



        else:



            self.processes = [

                {"PID": "P1", "AT": 0, "BT": 5, "Priority": None},

                {"PID": "P2", "AT": 1, "BT": 3, "Priority": None},

                {"PID": "P3", "AT": 2, "BT": 8, "Priority": None},

                {"PID": "P4", "AT": 3, "BT": 2, "Priority": None}

            ]



        self._refresh_input_tree()



        messagebox.showinfo(

            "Sample Data Loaded",

            f"Sample processes loaded for {algorithm}."

        )



    # ---------------- RUN SIMULATION ----------------



    def run_simulation(self):



        if not self.processes:



            messagebox.showwarning(

                "No Processes",

                "Add processes or load sample data first."

            )



            self.notebook.select(self.process_tab)

            return



        algorithm = self.current_algorithm.get()

        # Every process must have a priority when Priority Scheduling is selected.
        if algorithm == "Priority":
            missing_priority = [
                p["PID"] for p in self.processes
                if p.get("Priority") is None
            ]
            if missing_priority:
                messagebox.showwarning(
                    "Priority Missing",
                    "Priority values are missing for: "
                    + ", ".join(missing_priority)
                    + "\n\nSelect Priority first, then click Load Sample Data, "
                      "or clear the list and add each process with a priority."
                )
                self.notebook.select(self.process_tab)
                return

        try:

            # Quantum is validated only for Round Robin.

            if algorithm == "Round Robin":



                try:

                    quantum = int(self.quantum.get())

                except ValueError:

                    raise ValueError(

                        "Enter an integer time quantum."

                    )



                if quantum <= 0:

                    raise ValueError(

                        "Time quantum must be greater than zero."

                    )



            else:

                quantum = 2



            results, gantt, steps = simulate(

                algorithm,

                self.processes,

                quantum

            )



        except (ValueError, KeyError, TypeError) as error:



            messagebox.showerror(

                "Simulation Error",

                str(error)

            )



            return



        for item in self.result_tree.get_children():

            self.result_tree.delete(item)



        for p in results:



            priority_display = (

                p["Priority"]

                if algorithm == "Priority"

                else "-"

            )



            self.result_tree.insert(

                "",

                "end",

                values=(

                    p["PID"],

                    p["AT"],

                    p["BT"],

                    priority_display,

                    p["CT"],

                    p["TAT"],

                    p["WT"]

                )

            )



        average_wt = sum(

            p["WT"] for p in results

        ) / len(results)



        average_tat = sum(

            p["TAT"] for p in results

        ) / len(results)



        self.avg_wt_label.config(

            text=f"{average_wt:.2f}"

        )



        self.avg_tat_label.config(

            text=f"{average_tat:.2f}"

        )



        self.process_count_label.config(

            text=str(len(results))

        )



        self.draw_gantt(gantt)



        self.steps_text.delete("1.0", "end")



        self.steps_text.insert(

            "end",

            f"Algorithm: {algorithm}\n\n"

        )



        for step in steps:

            self.steps_text.insert(

                "end",

                step + "\n"

            )



        self.notebook.select(self.results_tab)







    def draw_gantt(self, gantt):



        self.gantt_canvas.delete("all")



        if not gantt:



            self.gantt_canvas.create_text(

                20,

                35,

                text="Run the simulation to display the Gantt chart.",

                fill=MUTED,

                anchor="w"

            )



            return



        self.gantt_canvas.update_idletasks()



        canvas_width = max(

            self.gantt_canvas.winfo_width(),

            600

        )



        left_margin = 35

        right_margin = 25



        usable_width = max(

            canvas_width - left_margin - right_margin,

            100

        )



        total_time = max(

            segment["End"]

            for segment in gantt

        )



        if total_time <= 0:

            total_time = 1



        scale = usable_width / total_time



        y1 = 20

        y2 = 58



        palette = [

            "#38BDF8",

            "#34D399",

            "#FBBF24",

            "#C084FC",

            "#FB7185",

            "#2DD4BF",

            "#60A5FA"

        ]



        for index, segment in enumerate(gantt):



            start = segment["Start"]

            end = segment["End"]



            x1 = left_margin + start * scale

            x2 = left_margin + end * scale



            fill = (

                "#CBD5E1"

                if segment["PID"] == "IDLE"

                else palette[index % len(palette)]

            )



            self.gantt_canvas.create_rectangle(

                x1,

                y1,

                x2,

                y2,

                fill=fill,

                outline=APP_BG,

                width=2

            )



            self.gantt_canvas.create_text(

                (x1 + x2) / 2,

                (y1 + y2) / 2,

                text=segment["PID"],

                fill=APP_BG,

                font=("Segoe UI", 9, "bold")

            )



            self.gantt_canvas.create_text(

                x1,

                y2 + 17,

                text=str(start),

                fill=TEXT,

                font=("Segoe UI", 9)

            )



        last_end = gantt[-1]["End"]



        final_x = left_margin + last_end * scale



        self.gantt_canvas.create_text(

            final_x,

            y2 + 17,

            text=str(last_end),

            fill=TEXT,

            font=("Segoe UI", 9)

        )









if __name__ == "__main__":



    root = tk.Tk()



    app = CPUSchedulingApp(root)



    root.mainloop()