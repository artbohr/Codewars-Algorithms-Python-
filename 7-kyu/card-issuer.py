def get_issuer(number):
    if len(str(number)) == 13 or len(str(number)) == 16:
        if str(number)[0] == '4':
            return 'VISA'
    if len(str(number)) == 15:
        if str(number)[:2] == '34' or str(number)[:2] == '37':
            return 'AMEX'
    if len(str(number)) == 16:
        if str(number)[:4] == '6011':
            return 'Discover'
        if ['51','52','53','54','55'].count(str(number)[:2]) > 0:
            return 'Mastercard'

    return 'Unknown'

'''
Given a credit card number we can determine who the issuer/vendor
is with a few basic knowns.

Complete the function get_issuer() that will use the values shown
below to determine the card issuer for a given card number. If the number
cannot be matched then the function should return the string Unknown.

| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |

Examples

get_issuer(4111111111111111) == "VISA"
get_issuer(4111111111111) == "VISA"
get_issuer(4012888888881881) == "VISA"
get_issuer(378282246310005) == "AMEX"
get_issuer(6011111111111117) == "Discover"
get_issuer(5105105105105100) == "Mastercard"
get_issuer(5105105105105106) == "Mastercard"
get_issuer(9111111111111111) == "Unknown"
'''
