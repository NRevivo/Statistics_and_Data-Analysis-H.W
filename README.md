# Statistical Analysis and Quality Control

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Statistical_Computing-8CAAE6)

An applied statistics project focused on translating probability theory into reliable,
reusable Python analysis. The work combines exact discrete-distribution calculations,
statistical power analysis, probability models for competing processes, and quality
control analysis based on manufacturing inspection logs.

This repository is part of my graduate-level **Statistics and Data Analysis** coursework
and demonstrates how I use Python to move from mathematical definitions to practical,
data-driven conclusions.

## Project Overview

The analysis is organized around five statistical problems:

1. **One-sided binomial testing**
   - Calculate exact right-tailed p-values.
   - Find rejection thresholds for a selected significance level.
   - Measure test power under an alternative success rate.
   - Identify non-monotonic power changes and the minimum sample size needed to reach
     a target power.

2. **Negative-binomial and duel probabilities**
   - Model the number of attempts required to achieve a fixed number of successes.
   - Calculate the probability that one of two players finishes first.
   - Account for ties when both players complete their task in the same round.
   - Calculate the expected duration of the duel.

3. **Sums of discrete random variables**
   - Convolve independent probability mass functions.
   - Represent distributions as value-probability arrays.
   - Extend the convolution process to sums of multiple independent variables.

4. **Coupon-collector probabilities**
   - Compute the exact probability of collecting all coupon types by a given time.
   - Determine quantiles for collecting a specified number of distinct coupons.

5. **Manufacturing quality control**
   - Clean and reconcile inspection logs from multiple data sources.
   - Aggregate inspected and defective items by machine.
   - Estimate machine-specific defect rates.
   - Test manufacturer claims using exact binomial p-values.
   - Determine the number of products required to detect a target number of defects
     with a chosen confidence level.

## Why This Project Matters

The project reflects several skills that are directly relevant to data science,
statistics, and analytics roles:

- Converting statistical definitions into tested, reusable functions.
- Choosing exact probability calculations instead of relying on simulation when precision
  matters.
- Working with numerical edge cases, including very small p-values.
- Separating data cleaning from statistical inference.
- Using aggregated evidence to support operational quality-control decisions.
- Communicating analytical results through a reproducible Jupyter Notebook.

## Repository Structure

```text
.
├── hw1/
│   ├── HW1.ipynb              # Interactive analysis and results
│   ├── hw1.py                 # Reusable statistical functions
│   ├── factory_log_1.csv      # Raw inspection log
│   ├── factory_log_2.csv      # Raw inspection log
│   ├── factory_log_3.csv      # Raw inspection log
│   └── factory_log_clean.csv  # Cleaned inspection data
├── .gitignore
└── README.md
```

## Technologies

- **Python**
- **NumPy** for numerical arrays and probability-distribution representations
- **pandas** for tabular data cleaning and aggregation
- **SciPy** for exact binomial and negative-binomial distribution calculations
- **Matplotlib** for statistical visualizations
- **Jupyter Notebook** for an interactive, reproducible workflow

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NRevivo/Statistics---Data-Analysis--H.W.git
cd Statistics---Data-Analysis--H.W
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install numpy pandas scipy matplotlib jupyter
```

### 4. Run the analysis

```bash
jupyter notebook hw1/HW1.ipynb
```

The notebook contains the exploratory workflow, calculations, and outputs. The
functions in [`hw1/hw1.py`](hw1/hw1.py) can also be imported into other Python
scripts or notebooks:

```python
from hw1.hw1 import binom_pvalue, critical_k, power

p_value = binom_pvalue(k=16, n=40, p0=0.2)
threshold = critical_k(n=40, p0=0.2, alpha=0.01)
test_power = power(n=40, p0=0.2, p1=0.35, alpha=0.01)
```

## Analytical Approach

The implementation emphasizes transparent statistical reasoning:

- **Tail probabilities** are calculated with SciPy survival functions to avoid
  unnecessary loss of precision.
- **Critical values** are found by searching for the smallest rejection threshold
  satisfying the chosen significance level.
- **Power analysis** evaluates the same rejection rule under an alternative
  distribution.
- **Discrete convolutions** combine independent probability mass functions while
  preserving sorted support values.
- **Quality-control inference** is based on totals over usable batches rather than
  treating individual log records as independent experiments.

## Learning Outcomes

By completing this project, I practiced:

- Exact hypothesis testing with binomial models.
- Power, sample-size, and threshold calculations.
- Negative-binomial modeling.
- Distribution convolution.
- Coupon-collector reasoning.
- Data validation and cleaning with pandas.
- Translating business questions into statistical decision rules.

## Portfolio Note

This project showcases a practical balance between mathematical statistics and
software implementation. It is especially representative of work where an analyst
must validate messy operational data, select an appropriate probability model, and
produce a precise result that can support a real-world quality decision.
