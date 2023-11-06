# filename: plot_stock_price.py
import matplotlib.pyplot as plt

# Assuming you have the stock price data in a list or numpy array called 'stock_prices'
# and the corresponding dates in a list or numpy array called 'dates'

# Plotting the stock price change YTD
plt.plot(dates, stock_prices)

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Change YTD')

# Saving the plot as an image
plt.savefig('stock_price_ytd.png')

# Displaying the plot
plt.show()