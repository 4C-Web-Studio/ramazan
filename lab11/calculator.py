from fractions import Fraction
import operator
OPERATIONS={'plus':operator.add,'minus':operator.sub,'times':operator.mul,'over':operator.truediv}
def evaluate(first,action,second):
    return OPERATIONS[action](Fraction(first),Fraction(second))
