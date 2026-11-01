from decimal import Decimal
import pytest
from lab06.module import checkout
@pytest.mark.parametrize('price,quantity,discount,total',[(10,2,0,'20.00'),('19.99',3,10,'53.97'),(5,1,100,'0.00'),('1.005',1,0,'1.01')])
def test_payment(price,quantity,discount,total):assert checkout(price,quantity,discount)==Decimal(total)
@pytest.mark.parametrize('price,quantity,discount',[(-1,1,0),(1,0,0),(1,True,0),(1,1,101),(1,1,-1),('NaN',1,0)])
def test_bad_payment(price,quantity,discount):
    with pytest.raises(ValueError):checkout(price,quantity,discount)
