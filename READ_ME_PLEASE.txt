# PROJECT README: QUEUEING ANALYSIS OF A HOSPITAL EMERGENCY ROOM

## DIRECTORY STRUCTURE
project/
├───Codes/                         
│   │   Analysis.py                # Data analysis and visualization script
│   │   ER Wait Time Data Overview.txt # Dataset description
│   │   ER Wait Time Dataset.csv   # Patient arrival/service time data
│   │   er_simulation.py           # M/M/c discrete-event simulation (DES)
│   │   mmc_analytics.py           # Theoretical M/M/1 and M/M/c calculations
│   │   Project_notebook.ipynb     # Interactive analysis notebook
│   ├───modules/                   # Custom Python modules
│   └───__pycache__/               # Auto-generated Python bytecode
├───Final_Result/
│       Project_pdf.pdf            # Final report with results
├───Outline & summary/
│       Project Outline.pdf        # Original project plan
│       Project summary.pdf        # Key findings summary
└───Theory/
        Analytical Models.pdf      # Queueing theory derivations

## KEY FILES
• SIMULATION: Run `er_simulation.py` to validate queue metrics (e.g., wait times).
• THEORY: `mmc_analytics.py` computes analytical results (L, Wq, P_wait).
• ANALYSIS: Use `Analysis.py` or the Jupyter notebook for data exploration.
• REPORT: See `Final_Result/Project_pdf.pdf` for conclusions.

## QUICK START
1. Install dependencies: 
   ```bash
   pip install numpy pandas matplotlib simpy scipy