# 📊 AI Sales Monitoring Dashboard

An **AI-powered Sales Monitoring Dashboard** that allows users to upload datasets (CSV or Excel), automatically clean the data, and generate interactive analytics and visualizations.

The system intelligently detects dataset structure, enables SQL querying, and provides customizable visualizations for quick sales performance analysis.

---

## 🚀 Live Demo
🔗 Streamlit App: [https://dataanalysisagent-vcg88qcz9emtmmtvkjnget.streamlit.app/]


---

# 📌 Problem Statement

Businesses often store sales data in **CSV or Excel files**, but extracting insights requires:

- Data cleaning
- Writing SQL queries
- Creating visual dashboards

This process is **time-consuming and requires technical expertise**.

This project solves the problem by building an **AI-assisted dashboard that automatically analyzes datasets and generates insights.**

---

# 💡 Features

### 📂 Dataset Upload
- Upload **CSV or Excel files**
- Supports datasets up to **200MB**

### 🧹 Automatic Data Cleaning
- Handles missing values
- Detects numeric & categorical columns
- Prepares dataset for analysis

### 📊 Data Preview
- Displays cleaned dataset preview
- Allows users to inspect processed data

### 📈 Sales Performance Monitoring
- Track sales metrics
- Monitor KPIs dynamically

### 📊 Custom Visualizations
Users can create visualizations by selecting:

- X-axis column
- Y-axis numeric metric
- Chart type (Bar, Line, etc.)

### 🗂 SQL Query Execution
Users can run SQL queries directly on the dataset.

Example:

```sql
SELECT region, SUM(revenue)
FROM df
GROUP BY region;
```

### ⬇ Download Cleaned Dataset
Users can export the processed dataset for further analysis.

---

# 🛠 Tech Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy

### Dashboard Framework
- Streamlit

### Data Visualization
- Plotly
- Matplotlib

### Query Engine
- DuckDB / SQLite

### Version Control
- Git
- GitHub

---

# ⚙️ Project Architecture

```
User Upload Dataset
        │
        ▼
Data Cleaning & Preprocessing (Pandas)
        │
        ▼
Data Preview + KPI Monitoring
        │
        ├── Visualization Engine (Plotly)
        │
        └── SQL Query Engine (DuckDB)
        │
        ▼
Download Cleaned Dataset
```

---

# 🧪 Example Workflow

1️⃣ Upload CSV / Excel dataset  
2️⃣ System automatically cleans the data  
3️⃣ Preview cleaned dataset  
4️⃣ Select metrics for monitoring  
5️⃣ Generate interactive visualizations  
6️⃣ Run custom SQL queries  
7️⃣ Download cleaned dataset  

---

# 📸 Dashboard Preview

(Add screenshots here)

Example sections:

- Dataset Upload
- Data Preview
- Sales Monitoring
- Visualization Dashboard
- SQL Query Panel

---

# 🔮 Future Enhancements

- 🤖 AI-powered **automatic insight generation**
- 💬 **Natural Language to SQL queries**
- 📉 **Sales forecasting using Machine Learning**
- 📊 **Anomaly detection in sales data**
- 🔗 Integration with **Power BI / Tableau**
- 👥 Multi-user dashboard collaboration

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Sales-Monitoring-Dashboard.git
```

Navigate to the project folder

```bash
cd AI-Sales-Monitoring-Dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

# 🎯 Use Cases

- Sales performance monitoring
- Business data exploration
- Data analyst dashboards
- Quick dataset visualization
- SQL practice on real datasets

---

# 👩‍💻 Author

**Vinutha S**  
Aspiring **Data Scientist | Data Analyst | AI Enthusiast**

🔗 LinkedIn: [https://www.linkedin.com/in/vinutha-s-1217783b2/]  
🔗 GitHub: [https://github.com/vinu245/DataAnalysisAgent]

---

# ⭐ If you found this project useful

Please consider **starring ⭐ the repository** to support the project.
