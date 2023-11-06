from typing import List
import datetime
import sys

class Solution:
    """
    Fibonacci -> but with recursion + memoization
    """
    fib_list = []
    def getFibonacciList(self, n: int) -> List:
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1,1]
        else:
            lst = self.getFibonacciList(n-1)
            lst.append(lst[-1] + lst[-2])
            return lst
        return self.getFibonacciList(n, a, b, fib_list)

    


if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print('running recursinve fib list with memoization')
    print(f'$ memusage python {sys.argv[0]} -u > memory_log.txt')
    print('~'*42)

    solution_obj = Solution()
    print(solution_obj.getFibonacciList(1))
    print('[1]    ->>> expected')

    # import ipdb; ipdb.set_trace()
    print()
    print(solution_obj.getFibonacciList(2))
    print('[1,1]    ->>> expected')

    print("solution_obj.getFibonacciList(3)")
    print(solution_obj.getFibonacciList(3))
    print('[1,1,2]    ->>> expected')
    
    print("solution_obj.getFibonacciList(42)")
    print(solution_obj.getFibonacciList(42))
    # print('[1,1,2]    ->>> expected')