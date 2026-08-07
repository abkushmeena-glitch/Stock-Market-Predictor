import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

def plot_moving_averages(data):
    ma_50_days = data['Close'].rolling(50).mean()
    ma_100_days = data['Close'].rolling(100).mean()
    ma_200_days = data['Close'].rolling(200).mean()

    # Price vs MA50
    st.subheader('Price vs MA50')
    fig1, ax1 = plt.subplots()
    ax1.plot(data.index, data['Close'], 'g',linewidth = 0.5, label='Close Price')
    ax1.plot(data.index, ma_50_days, 'r',linewidth = 1, label='MA 50 Days')
    ax1.legend()
    st.pyplot(fig1)
    
    # Price vs MA50 vs MA100
    st.subheader('Price vs MA50 vs MA100')
    fig2, ax2 = plt.subplots()
    ax2.plot(data.index, data['Close'], 'g',linewidth = 0.5, label='Close Price')
    ax2.plot(data.index, ma_50_days, 'r',linewidth = 1, label='MA 50 Days')
    ax2.plot(data.index, ma_100_days, 'b',linewidth = 1, label='MA 100 Days')
    ax2.legend()
    st.pyplot(fig2)
    
    # Price vs MA100 vs MA200
    st.subheader('Price vs MA100 vs MA200')
    fig3, ax3 = plt.subplots()
    ax3.plot(data.index, data['Close'], 'g',linewidth = 0.5, label='Close Price')
    ax3.plot(data.index, ma_100_days, 'r',linewidth = 1, label='MA 100 Days')
    ax3.plot(data.index, ma_200_days, 'b',linewidth = 1, label='MA 200 Days')
    ax3.legend()
    st.pyplot(fig3)

def prepare_and_predict_data(data_scaled, model, scaler):
    x = []
    y = []

    for i in range(100, len(data_scaled)):
        x.append(data_scaled[i-100:i])
        y.append(data_scaled[i, 0])

    x = np.array(x)
    y = np.array(y)

    # Safety check
    if len(x) == 0:
        return None, None, None

    y_predict = model.predict(x, verbose=0)

    # Convert back to original prices
    y_predict = scaler.inverse_transform(y_predict)
    y = scaler.inverse_transform(y.reshape(-1,1))

    return x, y, y_predict

def predict_future_prices(model, last_100_days, scaler):
    future_prices = []
    current_batch = last_100_days.reshape((1, 100, 1))
    
    for _ in range(365):  # Predict for the next 365 days
        future_price = model.predict(current_batch)
        future_prices.append(future_price[0][0])
        current_batch = np.append(current_batch[:, 1:, :], [[future_price]], axis=1)

    future_prices = np.array(future_prices) * scaler.scale_[0]  # Convert scaled price back to INR
    return future_prices

# Load pre-trained model
model = load_model('DATA\Stock Predictions Model.keras')

# Streamlit UI
st.header('Stock Market Predictor')
stock = st.text_input('Enter Stock Symbol', 'GOOG')

days = st.number_input(
    "Number of Trading Days",
    min_value=30,
    max_value=2500,
    value=30,
    step=10
)
usd_to_inr = 95.17  # Conversion rate

# Fetch and convert data
inception_data = yf.download(stock, period="1mo")
inception_data['Close'] = inception_data['Close'] * usd_to_inr
st.subheader('Stock History')
st.line_chart(inception_data['Close'])

if st.button('Run the Model'):
    data = yf.download(stock, period="10y")

    ticker = yf.Ticker(stock)
    info = ticker.info

    company_name = info.get("longName", stock)

    # st.subheader(company_name)
    # st.caption(f"Ticker : {stock.upper()}")

    latest_close = float(data['Close'].iloc[-1])
    previous_close = float(data['Close'].iloc[-2])

    # st.metric(
    #     label="Latest Closing Price",
    #     value=f"₹{latest_close:,.2f}"
    # )

    change = latest_close - previous_close
    percent_change = (change / previous_close) * 100

    # st.metric(
    #     label="Today's Change",
    #     value=f"{percent_change:.2f}%",
    #     # delta=f"{change:.2f}"
    # )

    col1, col2, col3 = st.columns([2.8, 1.3, 1.3])

    with col1:
        st.subheader(f"{company_name}")
        st.write(f"**Ticker:** {stock}")

    with col2:
        st.metric(
            "Latest Price",
            f"₹{latest_close:.2f}"
        )

    with col3:
        st.metric(
            "Today's Change",
            f"{percent_change:.2f}%",
            delta=f"{change:.2f} ₹"
        )

    # if change >= 0:
    #     st.success(f"🟢 +₹{change:.2f}")
    # else:
    #     st.error(f"🔴 -₹{abs(change):.2f}")


    dates = data.index
    data['Close'] = data['Close'] * usd_to_inr
    st.subheader('Stock Data (Last 30 Trading Days)')
    st.write(data.tail(days))



    # Prepare data
    data_train = pd.DataFrame(data['Close'][0: int(len(data) * 0.80)])
    data_test = pd.DataFrame(data['Close'][int(len(data) * 0.80):])
    scaler = MinMaxScaler(feature_range=(0, 1))
    full_data = pd.concat([data_train.tail(100), data_test], ignore_index=True)
    full_data_scaled = scaler.fit_transform(full_data)

    # Plotting moving averages
    plot_moving_averages(data)

    # Prepare and predict data
    x_test, y_test, y_predict = prepare_and_predict_data(full_data_scaled, model, scaler)
    if x_test is None:
        st.error("Not enough data available for prediction.")
        st.stop()

    prediction_dates = dates[-len(y_test):]
    # Plotting predictions
    st.subheader('Actual Price vs Predicted Price')
    # Show only last 30 trading days
    last_days = days

    prediction_dates = prediction_dates[-last_days:]
    actual_prices = y_test.flatten()[-last_days:]
    predicted_prices = y_predict.flatten()[-last_days:]

    fig4, ax4 = plt.subplots(figsize=(15,6))

    ax4.plot(prediction_dates,
            actual_prices,
            color='green',
            linewidth=2,
            label='Actual Price')

    ax4.plot(prediction_dates,
            predicted_prices,
            color='red',
            linewidth=2.5,
            label='Predicted Price')

    ax4.set_title(f"{stock} Stock Price Prediction using LSTM (last {last_days} trading days)")

    ax4.set_xlabel("Date")
    ax4.set_ylabel("Price (INR)")

    fig4.autofmt_xdate(rotation=30)

    ax4.legend()
    ax4.grid(True, alpha=0.3)

    st.pyplot(fig4)

    # Button to predict future prices
    if st.button('Price Prediction'):
        last_100_days = full_data_scaled[-100:, :]
        future_prices = predict_future_prices(model, last_100_days, scaler)
        st.subheader('Predicted Stock Prices for the Next Year')
        future_dates = pd.date_range(start=datetime.now(), periods=365)
        plt.figure(figsize=(10, 5))
        plt.plot(future_dates, future_prices, 'r', label='Predicted Future Prices')
        plt.title('Future Stock Prices Prediction')
        plt.xlabel('Date')
        plt.ylabel('Price (INR)')
        plt.legend()
        st.pyplot()