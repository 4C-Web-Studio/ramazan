from fractions import Fraction
from behave import given,when,then
from lab11.calculator import evaluate
@given('a clean arithmetic context')
def initialize(context):context.failure=None
@given('operands {first} and {second}')
def operands(context,first,second):context.first,context.second=first,second
@when('the operation is {action}')
def action(context,action):
    try:context.answer=evaluate(context.first,action,context.second)
    except ZeroDivisionError as failure:context.failure=failure
@then('the fraction result equals {answer}')
def result(context,answer):assert context.failure is None and context.answer==Fraction(answer)
@then('division is rejected')
def rejected(context):assert isinstance(context.failure,ZeroDivisionError)
