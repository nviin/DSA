# Best Time to Buy and Sell Stock

def Best_Time_to_Buy_and_Sell_Stock(price_ranges):
    min_price = float('inf')
    max_profit = 0

    for i in price_ranges:
        if i<min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    
    return (max_profit)  

if __name__ == "__main__":
    print(Best_Time_to_Buy_and_Sell_Stock([7, 1, 5, 3, 6, 4]))