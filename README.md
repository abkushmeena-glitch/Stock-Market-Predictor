# 📈 Stock Market Predictor using LSTM & Streamlit

A Machine Learning based Stock Market Prediction web application that forecasts stock closing prices using an **LSTM (Long Short-Term Memory)** neural network. The application allows users to enter any valid stock ticker symbol, visualize historical stock trends, compare actual vs predicted prices, and analyze moving averages through an interactive Streamlit dashboard.

---

## 🚀 Features

- 🔍 Search any stock using its ticker symbol (e.g., AAPL, GOOG, TSLA, MSFT)
- 📅 Select the number of recent trading days (30 / 60 / 90 or custom upto 2500)
- 📈 Interactive stock history visualization
- 💰 Displays:
  - Company Name
  - Ticker Symbol
  - Latest Closing Price
  - Daily Percentage Change
- 📊 Moving Average Analysis
  - MA50
  - MA100
  - MA200
- 🤖 LSTM-based Stock Price Prediction
- 📉 Actual Price vs Predicted Price comparison
- 🌐 User-friendly Streamlit Web Application

---

## 🖥️ Demo

### Dashboard

- Search any stock
- View historical data
- Analyze trends
- Compare predictions with actual prices

---

## 📸 Screenshots

### Home Dashboard

  <img width="1713" height="941" alt="Screenshot_7-8-2026_232216_localhost" src="https://github.com/user-attachments/assets/5ee6471d-976c-4dbc-80a5-0f212f924b9c" />


### Stock Analysis

> *(Add Screenshot Here)*

### Price Prediction

> *(Add Screenshot Here)*

---

## 🛠️ Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- LSTM Neural Network
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- yFinance

---

## 📂 Project Structure

```
Stock-Market-Predictor/
│
├── DATA/
│   ├── app.py
│   ├── Stock Predictions Model.keras
│   ├── Train_Model.py
│   ├── Forecastfinal.py
│   ├── Database.py
│   └── Graphs.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Stock-Market-Predictor.git
```

```bash
cd Stock-Market-Predictor
```

---

### Create Virtual Environment

Windows

```bash
python -m venv tfenv
```

Activate

```bash
tfenv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
streamlit run DATA/app.py
```

---

## 📊 Machine Learning Workflow

```
Historical Stock Data
          │
          ▼
Download using yFinance
          │
          ▼
Data Preprocessing
          │
          ▼
Normalization (MinMaxScaler)
          │
          ▼
Sequence Generation
          │
          ▼
LSTM Neural Network
          │
          ▼
Prediction
          │
          ▼
Visualization & Analysis
```

---

## 📈 Model Details

Model Type

- Long Short-Term Memory (LSTM)

Input Features

- Closing Price

Sequence Length

- 100 Days

Loss Function

- Mean Squared Error (MSE)

Optimizer

- Adam Optimizer

Framework

- TensorFlow / Keras

---

## 📷 Visualizations

The application generates:

- Historical Stock Price
- Moving Average (50 Days)
- Moving Average (100 Days)
- Moving Average (200 Days)
- Original vs Predicted Stock Price

---

## 🎯 Future Improvements

- Live Stock Price Updates
- Candlestick Charts
- Technical Indicators (RSI, MACD, Bollinger Bands)
- Next-Day Price Prediction
- Multi-stock Comparison
- Portfolio Tracker
- News Sentiment Analysis

---

## 📚 Learning Outcomes

Through this project I learned:

- Deep Learning using LSTM
- Time Series Forecasting
- Stock Market Data Analysis
- Data Visualization
- Streamlit Web Application Development
- TensorFlow & Keras
- Model Deployment

---

## 👨‍💻 Author

**Avkush Meena**

Bachelor of Technology (B.Tech)

Machine Learning Internship Project

---

## 📜 License

This project is developed for educational and learning purposes.
