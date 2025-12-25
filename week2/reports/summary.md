# Week 2 Summary — ETL + EDA

## Key findings

- **AE is the top revenue market**  
  Total revenue: **324,843.68** from **1,348 orders**.  
  Followed by KW (**307,761.92**), QA (**292,329.93**), and SA (**286,976.39**).

- **Average Order Value (AOV) is similar across markets**  
  Range: **244.01 (QA)** → **260.15 (KW)**.  
  Revenue differences are mainly driven by **order volume**, not basket size.

- **Monthly revenue trend**  
  Peak: **Jan 2025 = 106,530.04**  
  Secondary peak: **Apr 2025 = 101,450.03**  
  Lowest: **Dec 2025 = 63,659.12**

- **Refund rates by country (refunds / orders)**  
  - AE: **39.8%** (536 / 1,348)  
  - KW: **40.7%** (540 / 1,326)  
  - QA: **41.7%** (560 / 1,344)  
  - SA: **41.8%** (515 / 1,232)

- **SA vs AE comparison**  
  - Refund rate: **SA 41.8%** vs **AE 39.8%** → **+2.0 percentage points**  
  - Revenue: **AE 324.8k** vs **SA 287.0k** → AE higher by **~13%**  
  - AOV: **AE 257.61** vs **SA 257.84** (almost identical)

- **Winsorized order amount distribution**  
  - Count: **4,755**  
  - Mean: **254.87**, Median (p50): **257.07**  
  - p90: **450.41**, p95: **473.74**, Max: **499.99**

---

## Definitions

- **Revenue** = sum(`amount`) per group.
- **AOV (Average Order Value)** = mean(`amount`) per group.
- **Refund rate** = refunds / total orders, where refund = `status_clean == "refund"`.
- **Winsorized amount** = capped version of `amount` to reduce the influence of extreme values.
- **Monthly aggregation** = grouping by `month` extracted from `created_at`.

---

## Data quality caveats

- **Missing timestamps**: 507 orders have missing `created_at`, affecting time-based analysis.
- **Join coverage**: Country match rate is **100%**, so all orders were successfully matched to users.
- **Outliers**: Extreme `amount` values were winsorized to stabilize distribution.
- **Refund rate level**: Refund rates are unusually high (~40%) and may indicate data labeling or business logic issues.

---

## Next questions

- Why is the refund rate consistently high across all countries?
- Are refunds concentrated in specific products, users, or time periods?
- Does revenue per active user differ significantly between AE and SA?
- Are there seasonal patterns beyond the single-year monthly trend?
