class StockSpanner:

    stack_prices = []
    idx = -1

    def __init__(self):
        self.stack_prices = []
        self.idx = -1

    def next(self, price: int) -> int:
        while len(self.stack_prices) > 0 and self.stack_prices[-1][0] <= price:
            self.stack_prices.pop()

        self.idx += 1
        span = self.idx - (-1 if len(self.stack_prices) == 0 else self.stack_prices[-1][1])

        self.stack_prices.append((price, self.idx))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)