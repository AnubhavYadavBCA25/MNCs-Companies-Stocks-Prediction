import plotly.express as px
import plotly.graph_objects as go

############################### Functions used to plot all stocks data (Interactive Plots) ################################

# 1. Interactive Closing Price Trend
def plot_close_price(df, stock_name):
    fig = px.line(df, x='Date', y='Close', title=f'{stock_name} Closing Price Trend',
                  labels={'Close': 'Closing Price', 'Date': 'Date'}, template="plotly_dark")
    
    fig.update_traces(line=dict(color='cyan', width=2))
    fig.update_layout(xaxis_rangeslider_visible=True)
    
    return fig

# 2. Stock Volatility Analysis (Rolling Std Dev + Bollinger Bands)
def plot_volatility_bollinger(df, stock_name, window=20):
    df['Rolling_Mean'] = df['Close'].rolling(window).mean()
    df['Upper_Band'] = df['Rolling_Mean'] + 2 * df['Close'].rolling(window).std()
    df['Lower_Band'] = df['Rolling_Mean'] - 2 * df['Close'].rolling(window).std()

    fig = go.Figure()

    # Plot Close Price
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price', line=dict(color='cyan')))

    # Bollinger Bands
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Upper_Band'], name='Upper Band', line=dict(color='red', dash='dot')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Lower_Band'], name='Lower Band', line=dict(color='red', dash='dot')))
    
    fig.update_layout(title=f'{stock_name} Volatility & Bollinger Bands', template="plotly_dark")
    
    return fig

# 3. MACD & Signal Line Trend (Crossovers & Buy/Sell Signals)
def plot_macd_signal(df, stock_name):
    fig = go.Figure()
    
    # MACD Line
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD'], name='MACD Line', line=dict(color='orange')))
    
    # Signal Line
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Signal_Line'], name='Signal Line', line=dict(color='blue')))
    
    fig.update_layout(title=f'{stock_name} MACD & Signal Line', template="plotly_dark")
    
    return fig

# 4. RSI Trend (Overbought & Oversold Levels)
def plot_rsi(df, stock_name):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], name='RSI', line=dict(color='lime')))
    
    # Overbought & Oversold Levels
    fig.add_hline(y=70, line=dict(color='red', dash='dot'), annotation_text="Overbought (70)")
    fig.add_hline(y=30, line=dict(color='blue', dash='dot'), annotation_text="Oversold (30)")
    
    fig.update_layout(title=f'{stock_name} RSI Trend', template="plotly_dark")
    
    return fig

# 5. Volume Analysis (Trend & Moving Average)
def plot_volume_analysis(df, stock_name, window=20):
    df['Rolling_Volume'] = df['Volume'].rolling(window).mean()
    
    fig = go.Figure()
    
    # Volume
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume', marker_color='purple'))
    
    # Moving Average
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Rolling_Volume'], name='Moving Average', line=dict(color='cyan')))
    
    fig.update_layout(title=f'{stock_name} Volume Analysis', template="plotly_dark")

    return fig