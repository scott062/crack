class Solution:
    def maxProfit(self, prices):
        profits = self.generate_all_possible_profits(prices)
        days = len(profits)
        max_gain = 0

        for buy_day in range(days):
            for sell_day in range(days):
                current_profit = profits[buy_day][sell_day]
                if current_profit > 0: # Optimized to only consider profitable days
                    # Find remaining possible profits after the sell day
                    for remaining_profits in profits[sell_day:]:
                        best_possible_remaining = max(remaining_profits) + current_profit
                        if best_possible_remaining > max_gain:
                            max_gain = best_possible_remaining
        return max_gain

    def generate_all_possible_profits(self, prices):
        # output ex. [[0,1,-1], [3,0,0], [0,0,0]]
        # [             ________buy day 1_____           ,          ________buy day 2_____           ,           ________buy day 3_____             ]
        #             /            |           \                  /            |           \                   /            |           \
        #            /             |            \                /             |            \                 /             |            \
        #           /              |             \              /              |             \               /              |             \
        # [      [sell day 1,  sell day 2,  sell day3]   ,   [sell day 1,  sell day 2,  sell day3]   ,   [sell day 1,  sell day 2,  sell day3]      ]

        days = len(prices)
        all_profits = []
        for buy_day in range(days):
            possible_profits = []
            for sell_day in range(days):
                profit = 0
                if sell_day > buy_day: # Only consider days after buy day for profit calculation
                    profit = prices[sell_day] - prices[buy_day]
                possible_profits.append(profit)
            all_profits.append(possible_profits)
        return all_profits
