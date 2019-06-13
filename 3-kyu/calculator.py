class Calculator(object):
    operators = {'*':1,'/':1,'+':2,'-':2}
    actions = {'*': lambda x,y: x*y,'/': lambda x,y: x//y,'+': lambda x,y: x+y,'-': lambda x,y: x-y}
    priority = 1
    output = []

    def evaluate(self, string):
        return Calculator.calc(string.split())

    def calc(arr):
        for idx, value in enumerate(arr):
            if value in Calculator.operators and Calculator.operators[value] == Calculator.priority:
                tmp1, tmp2 = Calculator.flt_or_int(arr[idx-1]), Calculator.flt_or_int(arr[idx+1])
                arr[idx-1:idx+2] = [Calculator.actions[value](tmp1,tmp2)]
                return Calculator.calc(arr)

        if Calculator.priority > 1:
            Calculator.priority=1
            return Calculator.flt_or_int(arr[0])
        else:
            Calculator.priority+=1
            return Calculator.calc(arr)

    def flt_or_int(num):
        if isinstance(num,(int,float)):
            return num
        if '.' in num:
            return float(num)
        return int(num)

'''
*Can't Use EVAL*

Create a simple calculator that given a string of operators (+ - * and /) and
 numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have a
 higher priority and should be performed left-to-right. Additions and subtractions
 have a lower priority and should also be performed left-to-right.

'''
