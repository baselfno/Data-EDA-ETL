# Data-EDA-ETL

This guide covers running the notebook specifically, or the entire code pipeline in general.

---

## Setup

**Clone repository:**
```bash
git clone https://github.com/baselfno/Data-EDA-ETL.git
cd Data-EDA-ETL/week2
```

**Sync dependencies:**
```bash
uv sync
```

**Add notebook support:**
```bash
uv add notebook
```

---

## Run Notebook

**Launch Jupyter:**
```bash
uv run jupyter notebook
```

Your browser will open automatically showing the project files.

**Open and run the notebook:**
1. Click on `notebooks` folder
2. Click on `eda.ipynb` to open it
3. Run all cells: **Cell → Run All** (or press Shift+Enter for each cell)

The notebook will display results directly in your browser and save figures to `reports/figures/`.

---

**Note:** The notebook expects processed data in `data/processed/analytics_table.parquet`. If it doesn't exist, run the ETL pipeline first: `python scripts/run_etl.py`
