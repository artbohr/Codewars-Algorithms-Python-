def printer_error(s):
    return '{}/{}'.format(str(len([x for x in s if ord(x) > 109])),len(s))

'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer
has to use colors which, for the sake of simplicity, are named with letters from a to m.

You have to write a function printer_error which given a string will output the
error rate of the printer (letter outside the range a-m) as a string representing
a rational whose numerator is the number of errors and the denominator the length
of the control string. Don't reduce this fraction to a simpler expression.

#Examples:
s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
'''
