class MalformedExpressionError(Exception):
    def __str__(self) -> str:
        return 'Malformed expression'


class CantDoTwoOperationsError(Exception):
    def __str__(self) -> str:
        return 'I can only do one operation at a time'