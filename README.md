# 📊 Week 1 Project – IoT Sensor Data Analysis

This project is part of the **AICTE Edunet Internship (Week 1 Milestone)**.  
We work with **IoT sensor datasets** to perform data cleaning, exploratory analysis, and build a **baseline predictive model**.

---

## 📂 Dataset Description

The provided datasets include:

1. **25th Relay and Temp measurement.csv**
   - `time` – timestamp
   - `U (heating)` – relay/heating control signal
   - `y (Tin)` – indoor temperature (°C)

2. **SolarIradOutdoorIndoor.csv**
   - `Solar irradiance` – solar energy level
   - `Wind speed [m/s]` – wind speed
   - `OutTemp` – outdoor temperature (°C)

3. **DoubletTestDataSet.ods**
   - `Time` – test time (s)
   - `Uenergy` – energy input
   - `Tink` – indoor temperature (°C)

---

## ⚙️ Steps Performed

- **Data Cleaning**  
  - Converted timestamps to proper datetime  
  - Handled missing/inconsistent values  
  - Normalized sensor values  

- **Exploratory Data Analysis (EDA)**  
  - Visualized temperature trends over time  
  - Plotted Solar Irradiance vs Outdoor Temperature  
  - Generated correlation heatmaps  

- **Machine Learning (Baseline Model)**  
  - Built a **Linear Regression model**  
  - Predicted `OutTemp` using `Solar irradiance` & `Wind speed`  
  - Evaluated using R² score and Mean Squared Error  

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/gunit05/Enter-Week-1.git
   cd Enter-Week-1


   pip install pandas matplotlib seaborn scikit-learn odfpy

   jupyter notebook Week1_Project.ipynb


