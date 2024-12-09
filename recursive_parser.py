import re

def evaluate_expression(expression: str) -> float:
    """
    Evaluates a mathematical expression recursively, handling addition, subtraction,
    multiplication, division, and parentheses.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        float: The result of the evaluation.
    """
    def parse_term(tokens):
        """Parses terms, handling multiplication and division."""
        value = parse_factor(tokens)
        while tokens and tokens[0] in ('*', '/'):
            operator = tokens.pop(0)
            if not tokens:
                raise ValueError("Invalid expression: missing operand after operator.")
            next_value = parse_factor(tokens)
            if operator == '*':
                value *= next_value
            elif operator == '/':
                if next_value == 0:
                    raise ValueError("Division by zero.")
                value /= next_value
        return value

    def parse_factor(tokens):
        """Parses factors, handling parentheses and numbers."""
        if not tokens:
            raise ValueError("Invalid expression: unexpected end of input.")
        if tokens[0] == '(':
            tokens.pop(0)  # Remove '('
            value = parse_expression(tokens)
            if not tokens or tokens.pop(0) != ')':
                raise ValueError("Mismatched parentheses.")
            return value
        try:
            return float(tokens.pop(0))
        except ValueError:
            raise ValueError("Invalid number.")

    def parse_expression(tokens):
        """Parses expressions, handling addition and subtraction."""
        value = parse_term(tokens)
        while tokens and tokens[0] in ('+', '-'):
            operator = tokens.pop(0)
            if not tokens:
                raise ValueError("Invalid expression: missing operand after operator.")
            next_value = parse_term(tokens)
            if operator == '+':
                value += next_value
            elif operator == '-':
                value -= next_value
        return value

    # Tokenize the expression
    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/()]', expression.replace(' ', ''))
    if not tokens:
        raise ValueError("Empty expression.")
    
    result = parse_expression(tokens)
    if tokens:  # There should be no remaining tokens
        raise ValueError("Invalid syntax.")
    return result
