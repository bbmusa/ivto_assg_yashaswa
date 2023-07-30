
"""
Created on Sun Jul 30 02:24:38 2023

@author: yswav
"""
import tulipy as ti
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Investo:
    def __init__(self,df):
        df = Investo.strategy(self, df)
        df = Investo.signal(self, df)
        Investo.bt(self, df)
        
    def strategy(self,df):
        #strategy
        obv = np.where(df['close'].diff() > 0, df['volume'], -df['volume']).cumsum()
        """
        On balance Volume:
            on days where price went up, that day's volume is added to the cumulative OBV total. 
            If price went down, then that day's volume is subtracted from the OBV total.
        Simple but effective gives good results and also work as conformation sign,
        Along with exit strategy gives better results.
        """
        
        min_value = np.min(obv)
        max_value = np.max(obv) 
        
        obv = 2 * (obv - min_value) / (max_value - min_value)
        ema = ti.ema(obv,30)
        diff = ti.ema(obv-ema,8)
        df['obv'] = diff
        return df
    
    
    def signal(self,df):
        #signal calculation
        df['signal'] = 0  
        
        for i in range(1, len(df)):
            if df['obv'][i] > 0 and df['obv'][i - 1] <= 0:
                df.at[i, 'signal'] = 1
            elif df['obv'][i] < 0 and df['obv'][i - 1] >= 0:
                df.at[i, 'signal'] = -1
        def convert_signal(signal):
            if signal == 1:
                return 'Buy'
            elif signal == -1:
                return 'Sell'
            else:
                return 'Hold'
        
        df['signal'] = df['signal'].apply(convert_signal)
        return df

    def bt(self, df):
        initial_balance = 100000
        balance = initial_balance
        position = 0
        buy_price = 0
        num_trades = 0
        num_winning_trades = 0
        total_profit = 0
        max_profit_pct = 0
        max_loss_pct = 0
    
        def calculate_portfolio_value(balance, position, current_price):
            return balance + (position * current_price)
    
        for i in range(len(df)):
            signal = df['signal'][i]
            close_price = df['close'][i]
    
            if signal == 'Buy' and position == 0:
                position = balance // close_price
                buy_price = close_price
                balance -= (position * close_price)
    
            elif signal == 'Sell' and position > 0:
                balance += (position * close_price)
                position = 0
    
            # Calculate profit/loss for each trade
            if position > 0:
                trade_profit = (close_price - buy_price) / buy_price * 100
            else:
                trade_profit = 0  # No profit or loss for non-active trades
    
            total_profit += trade_profit
    
            if trade_profit > max_profit_pct:
                max_profit_pct = trade_profit
            elif trade_profit < max_loss_pct:
                max_loss_pct = trade_profit
    
            if trade_profit > 0:
                num_winning_trades += 1
    
            num_trades += 1
    
        # Calculate signal win percentage
        signal_win_percentage = (num_winning_trades / num_trades) * 100
    
        # Calculate average profit and average loss % (initial capital)
        avg_profit_pct = total_profit / num_trades
    
        # Calculate total % profit
        final_balance = round(calculate_portfolio_value(balance, position, df['close'].iloc[-1]))
        total_pct_profit = (final_balance-initial_balance )/1000
    
        print(f"Initial Balance: {initial_balance}")
        print(f"Final Balance: {final_balance}")
        print(f"Total % Profit: {total_pct_profit}%")
        print(f"Signal Win Percentage: {signal_win_percentage}%")
        print(f"Avg win % (Initial Capital): {avg_profit_pct:.2f}%")
        print(f"Max Profit % (Initial Capital): {max_profit_pct:.2f}%")
        print(f"Max Loss % (Initial Capital): {max_loss_pct:.2f}%")
 
    
