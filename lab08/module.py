from decimal import Decimal,ROUND_HALF_UP
def checkout(price,quantity,discount=0):
    price=Decimal(str(price));discount=Decimal(str(discount))
    if not price.is_finite() or price<0:raise ValueError('price')
    if type(quantity) is not int or quantity<1:raise ValueError('quantity')
    if not discount.is_finite() or not 0<=discount<=100:raise ValueError('discount')
    return (price*quantity*(100-discount)/100).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
