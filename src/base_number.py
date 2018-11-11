# Ricky Galliani

 
def decimal_to_base(decimal_number, base):
    '''
    Returns decimal_number as a number in the base system.
    '''    
    if decimal_number == 0:
        return BaseNumber('0', base)
    digits = []
    while decimal_number > 0:
	digits.insert(0, decimal_number % base)
	decimal_number = decimal_number // base
    return BaseNumber(''.join(map(str, digits)), base)


class BaseNumber:

    def __init__(self, digits, base):
	self.digits = digits  # str
        self.base = base      # int


    def __str__(self):
        return "BaseNumber(digits={}, base={})".format(self.digits, self.base)
    
    
    def as_decimal(self):
    	'''
	Returns base_number, a number in the base system, as a decimal number.
	'''
	n = 0
    	for d in self.digits:
            n = self.base * n + int(d)
    	return n
 
