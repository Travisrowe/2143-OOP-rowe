'''
Travis Rowe
2/2/2016
'''

def __add__(self,rhs):

    '''
    @function: __add__
    @description: changes the addition symbol to allow the addition of fractions. It also prints out an improper fraction as a whole number.
    @param: "Left-hand fraction"
    @param: "Right-hand fraction"
    @returns: Either returns a mixed number equivalent to the sum of the two parameters or a proper fraction equivalent to the same thing
    '''
    sdenom = self.denominator #stores "left" denominator for safekeeping
    rhsdenom = rhs.denominator #stores "right" denominator...
    self.numerator *= rhsdenom 
    rhs.numerator *= sdenom
    self.denominator *= rhsdenom
    x = self.numerator + rhs.numerator
    y = self.denominator

    if(x>y):	#if the fraction is improper
        whlNum = int(x/y)	#stores the whole number
        properNumerator = x%y    #stores the corrected numerator
        return "%s %s/%s" % (whlNum, properNumerator, y)
    else:
        return fraction(x,y)
