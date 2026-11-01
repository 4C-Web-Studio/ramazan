Feature: Rational arithmetic
  Background:
    Given a clean arithmetic context
  Scenario Outline: Fraction operations
    Given operands <first> and <second>
    When the operation is <action>
    Then the fraction result equals <answer>
    Examples:
      | first | second | action | answer |
      | 1/3   | 1/6    | plus   | 1/2    |
      | 7/4   | 1/4    | minus  | 3/2    |
      | 2/3   | 3/5    | times  | 2/5    |
      | 5/2   | 5      | over   | 1/2    |
  Scenario: Division by zero
    Given operands 9 and 0
    When the operation is over
    Then division is rejected
