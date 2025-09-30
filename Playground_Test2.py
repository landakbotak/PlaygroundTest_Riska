import math

def calculateCashback(amount):
# cashback 1% for transaction >= 100_000, otherwise 0
    # if (amount > 100000): # wrong point
    if (amount >= 100000): # corrected answer
        return math.floor(amount * 0.01)
    else:
        return 0
    
print('Amount ',calculateCashback (100000))
print('Amount ',calculateCashback (99999))
print('Amount ',calculateCashback (100001))

# Test Case
