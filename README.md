# CoD-dex — Call of Duty Character Index

The CoD-dex is a Python-based application that lets users search, view, and collect Call of Duty characters using a local Flask API. It includes keyword search, a personal codex, and optional Matplotlib visualizations.

##  Features
You can:
- Search characters by keyword (e.g., "ghost", "141", "walker")
- Add characters to your personal CoD-dex
- View or remove saved characters
- Optional Matplotlib charts which include:
  - Characters per faction
  - Characters per game
  - CoD-dex completion progress

##  Requirements

Make sure you have **Python 3.10+** installed.

Install all dependencies using:
`pip install -r requirements.txt`  

Your requirements.txt should contain:  
`flask`   
`requests`   
`matplotlib`


## How to Run the Application (Step-by-Step)
The CoD‑dex requires two terminals because the API and the main program run separately.

Step 1 — Start the Flask API
Open a terminal in the project folder and run:  
`python api.py`  
You should see something like:
 * Running on http://127.0.0.1:5000  
Leave this terminal open and running.
 The API must stay active for the CoD‑dex to work.

Step 2 — Run the CoD-dex Program  
Open a second terminal in the same project folder and run:  
`python main.py`  
You will see the main menu:
1. Search Character
2. Add Character to CoD-dex
3. View CoD-dex
4. Remove Character
5. View Charts
6. View Interaction Log
7. Exit
8. Help / Troublshooting  
Use the number keys to choose an option.  
#### Logging
All user actions (searches, additions, removals, codex views) are automatically recorded in:  
`interaction_log.txt`  
This file is created every time the program runs.
#### Charts
Selecting option 6 in the menu will open Matplotlib charts showing:  
- Characters per faction  
- Characters per game  
- Your CoD-dex completion progress  
These charts require Matplotlib to be installed.
