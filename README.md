# HR Attrition & Productivity Analyzer

A Python and Pandas data analysis project that merges employee demographic records with workplace performance data to clean missing compensation figures, benchmark department-level productivity, and identify retention risks among top performers.

## Project Overview

This project simulates an end-to-end HR analytics workflow using relational data merging, group-wise missing value imputation, feature engineering, and multi-condition boolean filtering.

### Datasets Used
1. **Employee Details (`df_emp`)**: Employee ID (`id`), `age`, `department` (IT, HR, Finance, Marketing), `monthly_salary` (containing missing values), and `attrition_status` (`1` = Left, `0` = Retained).
2. **Work & Performance Metrics (`df_work`)**: Employee ID (`id`), `overtime` (hours/units logged last month), `stock_options`, and `performance_rating` (1–5 scale).

## Key Pipeline Steps

1. **Relational Data Merging**: Combined `df_emp` and `df_work` via an inner join on `id` using `pd.merge()`.
2. **Group-Wise Missing Value Imputation**: Replaced missing `monthly_salary` entries with each employee's respective department average using `groupby("department")["monthly_salary"].transform("mean")` and `.fillna()`.
3. **Department Productivity Benchmarking**: Engineered a `productivity_per_dept` feature mapping each department's mean `performance_rating` back onto individual employee rows.
4. **Retention Risk Filtering**: Applied compound boolean indexing to isolate high-performing employees (`performance_rating >= 4`) with zero stock options (`stock_options == 0`) who left the company (`attrition_status == 1`).

## Key Findings

* **Department Productivity**: **IT** achieved the highest average productivity score at **4.75 / 5.0**, followed by **Marketing** (**4.00**), while **HR** and **Finance** both averaged **3.50**.
* **High-Performer Retention Risk**: Filtering for top performers without equity incentives flagged **Employee ID 101** (IT, Age 34, Monthly Salary ₹75,000, Performance Rating 5, Stock Options 0) as a critical attrition case despite IT leading overall department performance.

## Tech Stack

* **Python 3**
* **Pandas** (`merge`, `groupby`, `transform`, `fillna`, boolean filtering)
* **NumPy** (`np.nan`)

## How to Run

1. Clone the repository:
   ```bash
git clone https://github.com/Sahil-del59/HR-Attrition-Analyzer.git
cd HR-Attrition-Analyzer