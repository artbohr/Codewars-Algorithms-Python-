# Kata Instructions are located after the code.

import re

def balance(book):
    balance = expenses = 0
    output = []

    for x in book.splitlines():
        x = re.sub(r'([^\s\w.])+', '', x)
        if balance == 0 : balance = float(x)
        if len(x) < 1: continue

        if (len(x.split(" ")) > 1):
            balance -= float(x.split(" ")[2])
            expenses += float(x.split(" ")[2])
            output.append("{} {} {} Balance {}"
            .format(x.split(" ")[0],x.split(" ")[1],"%.2f" % float(x.split(" ")[2]),"%.2f" % balance))
        else: output.append("{}".format("%.2f" % float(x)))


    return ("Original Balance: {}\r\nTotal expense  {}\r\nAverage expense  {}"
    .format("\r\n".join(output), "%.2f" % expenses, "%.2f" % (expenses/(len(output)-1))))


'''
You are given a (small) check book as a - sometimes - cluttered
 (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"

The first line shows the original balance. Each other line (when not blank)
 gives information: check number, category, check amount.

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution.
 They are there so you can see them and how many of them you need):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"

On each line of the report you have to add the new balance and then in the last two lines
 the total expense and the average expense. So as not to have a too long result
 string we don't ask for a properly formatted result.

'''
