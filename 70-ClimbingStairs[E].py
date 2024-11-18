# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Solution: Fibonacci sequence - for each step n, you can either come from step n-1 (one step) or step n-2 (2 steps)
# Therefore, total numbers to reach step n: steps_to_n = steps_to[n-1] + steps_to[n-2]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1:
            return 1
        
        two_prev = 1
        prev = 1

        for i in range(2, n+1):
            current = two_prev + prev
            two_prev = prev
            prev = current
        
        return prev




    
