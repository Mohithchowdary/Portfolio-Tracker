
# 📊 Portfolio Tracker v1.0
![Screenshot 2024-09-21 120746](https://github.com/user-attachments/assets/4e3a255b-60ad-4801-9739-ece1d3ba67c1)
visit: https://docs.google.com/spreadsheets/d/17NIDF4VCKtWN2gvJMExut1_3lX0IAfU-HenGHTI9eXg/edit?usp=sharing

Welcome to the **Portfolio Tracker v1.0**, a comprehensive tool designed to help investors seamlessly track and manage their cryptocurrency and stock portfolios in real-time. The project integrates with APIs such as CoinMarketCap, Google Finance, and platforms like Binance and Zerodha to provide detailed analytics and real-time insights into your investments.

## 🚀 Features

- **Cryptocurrency Portfolio Tracking**
  - Get real-time data using the CoinMarketCap API.
  - Track key metrics like market price, % change, and profit/loss for popular cryptocurrencies such as Bitcoin, Ethereum, and BNB.
  - Platforms Supported: **Binance**.

- **Stock Portfolio Management**
  - Real-time stock data fetched using Google Finance API.
  - Track performance of Indian stocks like Reliance, Hindustan Copper, and Tata Power.
  - Platforms Supported: **Zerodha** via Kite Connect API.

- **Automated Calculation of Profit/Loss**
  - Automatically compute your current holdings' value, comparing them to invested amounts and market prices.
  - Hourly % changes provide an up-to-date overview of your portfolio performance.

- **Integration with Google Sheets**
  - All data is automatically stored and updated in a Google Spreadsheet, providing a snapshot of both stock and crypto portfolios.

- **Visual Data Representation**
  - Well-structured and clear flow diagrams illustrate how data is fetched and computed from different APIs.

## 🛠️ Tech Stack

- **Frontend:** Google Sheets for visualization and presentation.
- **Backend:** Python for fetching and processing data.
- **APIs:** 
  - CoinMarketCap (for cryptocurrency data).
  - Google Finance (for stock data).
  - Kite Connect (for Zerodha integration).
- **Platform Integration:**
  - **Binance** for crypto trading.
  - **Zerodha** for stock trading.

## 📊 Flow Diagrams
![PortfolioTracker_v1 pptx](https://github.com/user-attachments/assets/58ee3a68-2be8-4c55-abb9-b4802d62f869)

### Crypto Portfolio
![PortfolioTracker_v1 pptx (1)](https://github.com/user-attachments/assets/03025986-7ec7-4ee3-b155-df98e1dcff43)

### Stock Portfolio
![PortfolioTracker_v1 pptx (2)](https://github.com/user-attachments/assets/14786eef-fef4-42b2-a569-f710fc5d6f07)

These diagrams visually represent how data is fetched from CoinMarketCap and Google Finance APIs and how the Portfolio Tracker calculates the profit and loss for each asset.

## 📁 Project Structure

- `portfolio_tracker.py`: The core Python script that fetches and processes data from APIs.
- `google_sheets_integration.py`: Automates the process of exporting data to Google Sheets.
- `/screenshots/`: Includes visual representations and flow diagrams of the project (use the diagrams shown above for a detailed understanding).

## 📝 Google Spreadsheet Integration

All your portfolio data is updated and stored in a Google Spreadsheet for easy reference and tracking. Check out the live data [here](https://docs.google.com/spreadsheets/d/17NIDF4VCKtWN2gvJMExut1_3lX0IAfU-HenGHTI9eXg/edit?gid=0#gid=0).

## 🚀 Getting Started

To set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mohithchowdary/Portfolio-Tracker.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - CoinMarketCap API key for fetching crypto data.
   - Google Finance API for stock data.
   - Binance and Zerodha (Kite Connect) API for trading platforms.

4. Run the Python scripts:
   ```bash
   python portfolio_tracker.py
   ```

5. View your portfolio data in the Google Spreadsheet.

## 🤝 Contributing

Feel free to submit pull requests to improve the functionality or add new features. All contributions are welcome!

## 📞 Contact

For inquiries or discussions, feel free to connect via [LinkedIn](https://www.linkedin.com/in/mohithchowdary/) or raise an issue in the GitHub repository.
