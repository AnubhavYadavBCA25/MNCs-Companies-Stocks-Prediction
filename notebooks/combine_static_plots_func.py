import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

############################## Functions used to plot combined stocks data (Static Plots) ##################################

# 1. All Stocks Closing Price Comparison (Line Plot)
def plot_all_stocks_closing_price(stock_dfs, stock_names):
    plt.figure(figsize=(12, 6))
    
    for i, df in enumerate(stock_dfs):
        plt.plot(df['Date'], df['Close'], label=stock_names[i], linewidth=2)
    
    plt.title("Closing Price Comparison of All Stocks", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Closing Price", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. Stock Volatility Comparison (Box Plot of Log Returns)
def plot_volatility_boxplot(stock_dfs, stock_names):
    returns_data = pd.DataFrame()

    for i, df in enumerate(stock_dfs):
        returns_data[stock_names[i]] = df['Log_Returns']

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=returns_data, palette="coolwarm")

    plt.title("Stock Volatility Comparison (Log Returns)", fontsize=14)
    plt.ylabel("Log Returns", fontsize=12)
    plt.grid(True)
    plt.show()

# 3. Rolling Average Comparison (Moving Average Trends)
def plot_rolling_average(stock_dfs, stock_names, window=50):
    plt.figure(figsize=(12, 6))

    for i, df in enumerate(stock_dfs):
        plt.plot(df['Date'], df['Close'].rolling(window=window).mean(), label=f"{stock_names[i]} MA-{window}", linewidth=2)

    plt.title(f"Moving Average ({window}-Day) Comparison", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Moving Average Price", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# 4. RSI Trend Across All Stocks (Subplots)
def plot_rsi_trends(stock_dfs, stock_names):
    fig, axes = plt.subplots(len(stock_dfs), 1, figsize=(12, 10), sharex=True)

    for i, df in enumerate(stock_dfs):
        axes[i].plot(df['Date'], df['RSI'], label=stock_names[i], color='purple', linewidth=1.5)
        axes[i].axhline(70, color='red', linestyle='dashed', alpha=0.5)  # Overbought level
        axes[i].axhline(30, color='green', linestyle='dashed', alpha=0.5)  # Oversold level
        axes[i].set_title(f"{stock_names[i]} RSI Trend", fontsize=12)
        axes[i].legend()
        axes[i].grid(True)

    plt.xlabel("Date", fontsize=12)
    plt.tight_layout()
    plt.show()

# 5. MACD & Signal Line Trend (Subplots)
def plot_macd_trends(stock_dfs, stock_names):
    fig, axes = plt.subplots(len(stock_dfs), 1, figsize=(12, 10), sharex=True)

    for i, df in enumerate(stock_dfs):
        axes[i].plot(df['Date'], df['MACD'], label=f"{stock_names[i]} MACD", color='blue', linewidth=1.5)
        axes[i].plot(df['Date'], df['Signal_Line'], label="Signal Line", color='red', linestyle="dashed")
        axes[i].axhline(0, color='black', linestyle='dashed', alpha=0.5)
        axes[i].set_title(f"{stock_names[i]} MACD & Signal Line", fontsize=12)
        axes[i].legend()
        axes[i].grid(True)

    plt.xlabel("Date", fontsize=12)
    plt.tight_layout()
    plt.show()