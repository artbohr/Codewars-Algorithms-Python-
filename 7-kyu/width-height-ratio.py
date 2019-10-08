def calculate_ratio(w,h):
    c_gcd = gcd(w,h)
    ar_w,ar_h = w//c_gcd,h//c_gcd
    return '{}:{}'.format(ar_w,ar_h) if ar_w and ar_h else 'You threw an error'
    
def gcd (a,b):
    if b==0:
        return a
    return gcd (b,a%b)

'''
We all use 16:9, 16:10, 4:3 etc. ratios every day. Main task is to determine image
 ratio by its width and height dimensions.

Function should take width and height of an image and return a ratio string (ex."16:9").
 If any of width or height entry is 0 function should throw an exception (or return Nothing).

'''