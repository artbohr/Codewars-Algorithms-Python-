'''
You will be given the number of angles of a shape with equal sides and angles,

and you need to return the number of its sides, and the measure of the interior angles.

Should the number be equal or less than 2, return:

"this will be a line segment or a dot"

Otherwise return the result in the following format:

"This shape has s sides and each angle measures d degrees"

(replace s with number of sides and d with the measure of the interior angles).

Angle measure should be floored to the nearest integer.

Number of sides will be tested from 0 to 180.
'''

def describe_the_shape(angles):
    if angles <=2:
        return 'this will be a line segment or a dot'
    return 'This shape has {} sides and each angle measures {}'.format(angles, (angles-2)*180//angles)

describe_the_shape(6)
# Returns:'This shape has 6 sides and each angle measures 120'
