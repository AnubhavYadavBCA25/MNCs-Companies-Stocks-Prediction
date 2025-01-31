# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

############################# Functions used to plot all stocks data (Static Plots) #############################

# 1. Closing Price Trend
def plot_closing_price(df, stock_name):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label="Closing Price", color='blue', linewidth=2)
    
    plt.title(f'{stock_name} Closing Price Trend', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Closing Price', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. Stocks Returns Distribution (Histogram & KDE Plot)
def plot_returns_distribution(df, stock_name):
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Log_Returns'], bins=50, kde=True, color='purple')

    plt.title(f'{stock_name} Returns Distribution', fontsize=14)
    plt.xlabel('Log Returns', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True)
    plt.show()

# 3. Box Plot of Closing Prices (Outlier Detection)
def plot_boxplot_closing(df, stock_name):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df['Close'], color='cyan')
    
    plt.title(f'{stock_name} Closing Price Box Plot', fontsize=14)
    plt.ylabel('Closing Price', fontsize=12)
    plt.grid(True)
    plt.show()

# 4. Pairplot for Feature Relationships
def plot_pairplot(df):
    sns.pairplot(df[['Close', 'Volume', 'Log_Returns', 'RSI', 'MACD']], diag_kind='kde', corner=True)
    plt.show()

# 5. Correlation Heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[['Close', 'Volume', 'Log_Returns', 'RSI', 'MACD', 'Signal_Line']].corr(), 
                annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

    plt.title("Feature Correlation Heatmap", fontsize=14)
    plt.show()