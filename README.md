# Data-EDA-ETL — Notebook Analysis

Quick guide to run the exploratory data analysis notebook only.

---

## Setup

**Clone repository:**
```bash
git clone <https://github.com/baselfno/Data-EDA-ETL.git>
cd Data-EDA-ETL/week2
```

**Create virtual environment:**

Windows:
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

**Open and run:**
- Navigate to `notebooks/eda.ipynb`
- Run all cells (Cell → Run All)

The notebook loads `data/processed/analytics_table.parquet`, performs analysis, and saves figures to `reports/figures/`.

---

**Note:** Raw data must be in `data/raw/` and processed data in `data/processed/` for the notebook to work. If processed data doesn't exist, run the ETL pipeline first using `python scripts/run_etl.py`.
