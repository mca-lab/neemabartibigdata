# 🌍 Integrating and Visualizing World Bank Data for Global Economic Insights

A complete Big Data pipeline built using **Python**, **PySpark**, and **Docker**, designed to automate the ingestion, cleaning, integration, and analysis of global economic datasets such as **GDP** and **Population** from the **World Bank**.

---

# 🚀 Project Overview
This project demonstrates:

- Automated data ingestion (World Bank datasets)
- Distributed data cleaning using PySpark in Docker
- Analysis & visualization in Jupyter Notebook
- A fully reproducible, containerized workflow

You must select **2 or more datasets**, define a **research question**, and implement the full pipeline.

---

# 🔧 Project Workflow

## 📍 Module 1 — Data Collection & Ingestion
**Objective:** Automatically download datasets in a controlled environment.

### Tasks
- Select 2 World Bank datasets  
- Create `fetch_data.py` to download CSV files  
- Store them in `data/raw/`  
- Use Docker for reproducibility  

### Deliverables
- `Dockerfile` + `requirements.txt`  
- `src/fetch_data.py`  
- Raw datasets inside `data/raw/`  

---

## 📍 Module 2 — Data Cleaning & Integration (PySpark)
**Objective:** Prepare datasets for analysis.

### Tasks
- Load datasets using PySpark  
- Handle missing values, duplicates, incorrect formats  
- Join/merge GDP + Population datasets  
- Store cleaned files in `data/processed/`  

### Deliverables
- `Dockerfile` + `requirements.txt`  
- `src/clean_data.py`  
- Processed data in `data/processed/`  

---

## 📍 Module 3 — Analysis & Visualization (Jupyter Notebook)
**Objective:** Explore the cleaned data to answer the research question.

### Tasks
- Load processed data  
- Perform descriptive statistics, correlations, or regression  
- Visualize with Matplotlib, Seaborn, Plotly  
- Document findings and conclusions  

### Deliverables
- `notebooks/analysis.ipynb`  
- Visual charts and graphs  
- README: problem statement, explanation, conclusion  

---

# 🛠️ Technologies Used
- Python 3  
- PySpark  
- Docker  
- Matplotlib / Seaborn / Plotly  
- Jupyter Notebook  

---

# 📁 Repository Structure

project/
│── data/
│ ├── raw/
│ └── processed/
│── src/
│ ├── fetch_data.py
│ └── clean_data.py
│── notebooks/
│ └── analysis.ipynb
│── docker/
│ ├── Dockerfile.ingest
│ └── Dockerfile.clean
│── requirements.txt
│── .gitignore
│── README.md

