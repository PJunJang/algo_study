# 20546 기적의 매매법

# BNP은 가능한 budget안에서 전량 매수 후 판매 x
# Timing은 가능한 budget 안에서 전량 매수 하지만 주가가 3일동안 하락할때만 전량 매수
# 주가가 3일동안 상승하면 전량 매도


def BNP(budget_bnp, prices):
    stock_cnt = 0
    cash = budget_bnp
    for stock in prices:
        if cash >= stock:
            cnt = cash // stock
            stock_cnt += cnt
            cash = cash % stock
    
    asset = stock_cnt * prices[-1] + cash
    return asset
    

def Timing(budget_timing, prices):
    stock_cnt = 0
    cash = budget_timing
    buy_cnt = 0
    sell_cnt = 0
    for i in range(1, len(prices)):
        if prices[i-1] > prices[i]:
            buy_cnt += 1
        elif prices[i-1] <= prices[i]:
            buy_cnt = 0
        if prices[i-1] < prices[i]:
            sell_cnt += 1
        elif prices[i-1] >= prices[i]:
            sell_cnt = 0
        if buy_cnt >= 3:
            if cash >= prices[i]:
                cnt = cash // prices[i]
                stock_cnt += cnt
                cash = cash % prices[i]
        if sell_cnt >= 3:
            if stock_cnt > 0:
                add = stock_cnt * prices[i]
                cash += add
                stock_cnt = 0
    asset = stock_cnt * prices[-1] + cash
    return asset



budget_bnp = int(input())
budget_timing = budget_bnp
prices = list(map(int,input().split()))
bnp = BNP(budget_bnp, prices)
timing = Timing(budget_timing, prices)
if (bnp > timing):
    print("BNP")
elif (bnp == timing):
    print("SAMESAME")
else:
    print("TIMING")
