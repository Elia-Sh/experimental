from typing import List
import datetime
import sys

class Solution:
    """
    Fibonacci -> return a list of fib numbers of size of n
    """
    def getFibonacciList(self, n: int) -> List:
        fib_list = [1,1]    # initializing for simple cases

        if n < 1:
            print('ERROR - cant get the 0 or negative fib number')
            return []
        if n == 1:
            return fib_list[:1] # only fist element
        if n == 2:
            return fib_list
        
        # all other cases can loop over n
        for i in range(1, n-1):
            current_element = fib_list[i-1] + fib_list[i]
            fib_list.append(current_element)
        return fib_list



if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print('running fib - loop and list - no recursion')
    print('Example of execution with memory sample - ')
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