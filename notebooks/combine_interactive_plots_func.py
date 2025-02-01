import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


############################ Interactive Plot Functions for Combined Stocks Data ##################################

# 1. Stock Price Heatmap (Correlation Matrix)
def plot_stock_correlation(stock_dfs, stock_names):
    stock_prices = pd.DataFrame()

    for i, df in enumerate(stock_dfs):
        stock_prices[stock_names[i]] = df['Close']

    correlation_matrix = stock_prices.corr()

    fig = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=stock_names,
        y=stock_names,
        colorscale='Viridis',
        annotation_text=correlation_matrix.round(2).values,
    )
    fig.update_layout(title="Stock Price Correlation Heatmap")
    fig.show()

# 2. Closing Price Comparison (Line Plot)
def plot_combined_stock_prices(stock_dfs, stock_names):
    stock_data = []
    
    for i, df in enumerate(stock_dfs):
        temp_df = df[['Date', 'Close']].copy()
        temp_df['Stock'] = stock_names[i]
        stock_data.append(temp_df)

    all_stocks = pd.concat(stock_data)

    fig = px.line(
        all_stocks, 
        x='Date', 
        y='Close', 
        color='Stock', 
        title="Combined Stock Closing Prices Over Time",
        labels={'Close': 'Stock Price', 'Date': 'Date'},
        line_shape="linear"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Closing Price",
        hovermode="x unified",
        template="plotly_dark"
    )

    fig.show()

# 3. Stocks volume comparison (Line Plot)
def plot_combined_volume(stock_dfs, stock_names):
    stock_data = []

    for i, df in enumerate(stock_dfs):
        temp_df = df[['Date', 'Volume']].copy()
        temp_df['Stock'] = stock_names[i]
        stock_data.append(temp_df)

    all_stocks = pd.concat(stock_data)

    fig = px.line(
        all_stocks, 
        x='Date', 
        y='Volume', 
        color='Stock', 
        title="Combined Trading Volume Over Time",
        labels={'Volume': 'Trading Volume', 'Date': 'Date'},
        line_shape="linear"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Trading Volume",
        hovermode="x unified",
        template="plotly_dark"
    )

    fig.show()

# 4. Stock High Price Comparison (Line Plot)
def plot_combined_high(stock_dfs, stock_names):
    stock_data = []

    for i, df in enumerate(stock_dfs):
        temp_df = df[['Date', 'High']].copy()
        temp_df['Stock'] = stock_names[i]
        stock_data.append(temp_df)

    all_stocks = pd.concat(stock_data)

    fig = px.line(
        all_stocks, 
        x='Date', 
        y='High', 
        color='Stock', 
        title="Combined High Prices Over Time",
        labels={'High': 'Stock High Price', 'Date': 'Date'},
        line_shape="linear"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="High Price",
        hovermode="x unified",
        template="plotly_dark"
    )

    fig.show()

# 5. Stock Low Price Comparison (Line Plot)
def plot_combined_low(stock_dfs, stock_names):
    stock_data = []

    for i, df in enumerate(stock_dfs):
        temp_df = df[['Date', 'Low']].copy()
        temp_df['Stock'] = stock_names[i]
        stock_data.append(temp_df)

    all_stocks = pd.concat(stock_data)

    fig = px.line(
        all_stocks, 
        x='Date', 
        y='Low', 
        color='Stock', 
        title="Combined Low Prices Over Time",
        labels={'Low': 'Stock Low Price', 'Date': 'Date'},
        line_shape="linear"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Low Price",
        hovermode="x unified",
        template="plotly_dark"
    )

    fig.show()
