# 📊 Unemployment Analysis in India - COVID-19 Impact

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0.3-green.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.2-orange.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12.2-red.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

* [Overview](#overview)
* [Key Findings](#key-findings)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Visualizations](#visualizations)
* [Technologies Used](#technologies-used)
* [Sample Output](#sample-output)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## 🔍 Overview

This project analyzes the socio-economic impact of COVID-19 on unemployment trends in India using real-world government data.
The analysis compares urban and rural areas, identifies the most affected regions, and visualizes the dramatic spike in unemployment rates during the lockdown period (April–July 2020).

**Dataset Source:** Unemployment in India (May 2019 - June 2020)
**Data Points:** 740 entries | 7 features | 27 regions covered

---

## ⚙️ CI/CD (GitHub Actions)

This project automatically runs analysis tests on every push using GitHub Actions to ensure code reliability.

---

## 🎯 Key Findings

| Finding                     | Insight                                                         |
| --------------------------- | --------------------------------------------------------------- |
| 📈 **Peak Unemployment**    | Surged to over 20% during April–July 2020                       |
| 🏆 **Most Affected States** | Tripura (28.35%), Haryana (26.28%), Jharkhand (20.59%)          |
| 🏙️ **Urban vs Rural**      | Urban areas hit harder (23.5%) than rural (17.8%)               |
| 📅 **Seasonal Pattern**     | Highest unemployment in May–June, lowest in September–October   |
| 📉 **Employment Drop**      | Estimated employed population decreased by ~15% during lockdown |
| ⏱️ **Recovery Time**        | Started recovering gradually after July 2020                    |

---

## 📸 Visualization Gallery

| 📈 Unemployment Trend | 🏆 Top 5 Regions |
|:---:|:---:|
| ![Unemployment](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/unemployment_over_time.png) | ![Top 5](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/top5_regions.png) |

| 🏙️ Urban vs Rural | 🔥 Correlation Heatmap |
|:---:|:---:|
| ![Urban Rural](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/urban_vs_rural_timeseries.png) | ![Heatmap](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/correlation_heatmap.png) |

| 📅 Monthly Pattern | 🌾 Urban/Rural Pie |
|:---:|:---:|
| ![Monthly](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/monthly_unemployment.png) | ![Pie](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/urban_vs_rural_pie.png) |

| 📊 Unemployment by Region | 📉 Employment Over Time |
|:---:|:---:|
| ![By Region](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/unemployment_by_region.png) | ![Employed](https://raw.githubusercontent.com/Aya-Mohamed945/unemployment-analysis/main/outputs/figures/employed_over_time.png) |

---

## 📁 Project Structure

```
unemployment-analysis/
│
├── data/
│   └── Unemployment in India.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── visualizations.py
│   └── main.py
│
├── outputs/
│   └── figures/
│       ├── unemployment_over_time.png
│       ├── employed_over_time.png
│       ├── unemployment_by_region.png
│       ├── top5_regions.png
│       ├── urban_vs_rural_pie.png
│       ├── urban_vs_rural_timeseries.png
│       ├── correlation_heatmap.png
│       └── monthly_unemployment.png
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### Prerequisites

* Python 3.9 or higher
* pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/unemployment-analysis.git
cd unemployment-analysis
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Dataset

Place the `Unemployment in India.csv` file inside the `data/` folder.

---

## 🚀 Usage

### Run the Complete Analysis

```bash
python src/main.py
```

This will:

* Load and clean the dataset
* Remove duplicates & handle missing values
* Perform statistical analysis
* Generate 8 visualizations
* Save all plots to `outputs/figures/`

---

## 📊 Interactive Dashboard (Streamlit)

This project includes an interactive dashboard built using **Streamlit** to visualize unemployment trends in India.

### 🚀 Features:
- Real-time data preview
- Unemployment trend over time
- Top affected regions visualization
- Simple and interactive UI

---

### ▶️ How to run the dashboard:

```bash
streamlit run app.py

The dashboard will open automatically in your browser at:
http://localhost:8501

---

### Run Specific Modules (Interactive Mode)

```python
from src.data_loader import load_and_clean_data
from src.analysis import calculate_covid_impact, get_top5_unemployment_regions

df = load_and_clean_data()
calculate_covid_impact(df)
top5, _ = get_top5_unemployment_regions(df)
print(top5)
```

---

## 📊 Visualizations

| # | File Name                     | Description                      |
| - | ----------------------------- | -------------------------------- |
| 1 | unemployment_over_time.png    | Time series of unemployment rate |
| 2 | employed_over_time.png        | Employment trends                |
| 3 | unemployment_by_region.png    | Bar chart of regions             |
| 4 | top5_regions.png              | Most affected regions            |
| 5 | urban_vs_rural_pie.png        | Urban vs Rural                   |
| 6 | urban_vs_rural_timeseries.png | Trend comparison                 |
| 7 | correlation_heatmap.png       | Correlation matrix               |
| 8 | monthly_unemployment.png      | Monthly pattern                  |

---

## 💻 Technologies Used

| Category        | Technologies        |
| --------------- | ------------------- |
| Data Processing | Pandas, NumPy       |
| Visualization   | Matplotlib, Seaborn |
| Environment     | Python              |
| Version Control | Git & GitHub        |

---

## 📈 Sample Output

```
==================================================
COVID-19 Impact on Unemployment:
==================================================
Pre-COVID Average: 8.72%
Post-COVID Average: 19.34%
Increase: 121.8%

==================================================
Top 5 Most Affected Regions:
==================================================
Tripura            28.35%
Haryana            26.28%
Jharkhand          20.59%
Bihar              18.92%
Himachal Pradesh   18.54%
```

---

## 🤝 Contributing

* Fork the repository
* Create a branch
* Commit changes
* Push to branch
* Open a Pull Request

---

## 📝 License

MIT License

---

## 📧 Contact

Aya Mohamed Abd Elazim
Email: [aya.320240137@ejust.edu.eg](mailto:your.email@example.com)
GitHub: @https://github.com/Aya-Mohamed945

---

## ⭐ Support

If you found this project helpful, please give it a star on GitHub!
