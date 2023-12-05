import matplotlib.pyplot as plt
import random
import numpy as np

def martingale(money: float, min_bet=1, p=18/37):
    """
    Simulate the Martingale betting strategy.

    Parameters:
    - money (float): Initial amount of money.
    - min_bet (float): Minimum bet amount. Default is 1.
    - p (float): Probability of winning. Default is 18/37, which corresponds to a European roulette wheel.

    Returns:
    Displays a plot of the simulation results.
    """
    starting_money = money
    gain = money - starting_money
    flag = True
    y2 = [gain]
    i = 0
    bet = min_bet

    while flag:
        draw = random.random()
        money -= bet

        # If the draw is greater than the winning probability, the bet is won
        if draw > p:
            money += bet * 2
            bet = min_bet
        else:
            # If the bet is lost, double the bet for the next round
            bet = bet * 2

        gain = money - starting_money
        y2.append(gain)
        i += 1

        # If the money goes below 0, stop the simulation
        if money < 0:
            flag = False

    # Plot the results
    plt.plot([k for k in range(i + 1)], y2)
    plt.xlabel('Number of Bets')
    plt.ylabel('Net Gain')
    plt.title('Martingale Betting Strategy Simulation')
    plt.show()
    
# Example : martingale(1000,min_bet=1, p=18/37)
