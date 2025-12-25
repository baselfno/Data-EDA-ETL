# Data-EDA-ETL

This guide covers running the notebook specifically, or the entire code pipeline in general.

---

## Setup

**Clone repository:**
```bash
git clone <https://github.com/baselfno/Data-EDA-ETL.git>
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
pip install jupyter nbconvert
```

---

## Run Notebook Directly

**Execute notebook from command line:**

Windows (PowerShell):
```bash
jupyter nbconvert --to notebook --execute notebooks/eda.ipynb --output eda_output.ipynb
```

macOS/Linux:
```bash
jupyter nbconvert --to notebook --execute notebooks/eda.ipynb --output eda_output.ipynb
```

This runs the notebook and saves the executed version as `eda_output.ipynb` with all outputs included.

**View results:**
- Output notebook: `notebooks/eda_output.ipynb`
- Generated figures: `reports/figures/*.png`

---

**Alternative - Generate HTML report:**
```bash
jupyter nbconvert --to html --execute notebooks/eda.ipynb --output eda_report.html
```

Opens `notebooks/eda_report.html` in your browser to view results.

---

**Note:** The notebook expects processed data in `data/processed/analytics_table.parquet`. If it doesn't exist, run the ETL pipeline first: `python scripts/run_etl.py`
