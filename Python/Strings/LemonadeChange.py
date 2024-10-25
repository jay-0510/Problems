class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0  # Track the count of $5 and $10 bills
        
        for bill in bills:
            if bill == 5:
                five += 1  # If the customer pays with $5, no change needed
            elif bill == 10:
                if five > 0:  # If the customer pays with $10, give one $5 as change
                    five -= 1
                    ten += 1
                else:
                    return False  # If no $5 bill available, return False
            else:  # The customer pays with $20
                if ten > 0 and five > 0:  # Prefer giving one $10 and one $5 as change
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise, give three $5 bills as change
                    five -= 3
                else:
                    return False  # If neither option is available, return False
        
        return True  # If all customers are served successfully, return True