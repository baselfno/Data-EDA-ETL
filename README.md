# Data-EDA-ETL

This guide covers running the notebook specifically, or the entire code pipeline in general.

---

## Setup

**Clone repository:**
```bash
git clone <REPO_URL>
cd Data-EDA-ETL/week2
```

**Create virtual environment:**

Windows (PowerShell):
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Run Notebook

**Launch Jupyter:**
```bash
jupyter notebook
```

Your browser will open automatically showing the project files.

**Open and run the notebook:**
1. Click on `notebooks` folder
2. Click on `eda.ipynb` to open it
3. Run all cells: **Cell → Run All** (or press Shift+Enter for each cell)

The notebook will display results directly in your browser and save figures to `reports/figures/`.

---

**Note:** The notebook expects processed data in `data/processed/analytics_table.parquet`. If it doesn't exist, run the ETL pipeline first: `python scripts/run_etl.py`
