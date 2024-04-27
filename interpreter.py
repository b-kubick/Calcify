# from tokenizer import Token, INTEGER, PLUS, MINUS, MUL, DIV, EOF
from tokenizer import INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF

"""
Grammar:

expr: term ((PLUS | MINUS ) term)*
term: factor ((MUL | DIV) factor)*
factor: (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN (handles unary operators - negative numbers)

"""

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) // self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)


# class Interpreter(object):
#     def __init__(self, lexer):
#         self.lexer = lexer
#         # set current token to the first token taken from the input
#         self.current_token = self.lexer.get_next_token()
#
#     def error(self):
#         raise Exception('Invalid syntax')
#
#     def eat(self, token_type):
#         # compare the current token type with the passed token
#         # type and if they match then "eat" the current token
#         # and assign the next token to the self.current_token,
#         # otherwise raise an exception.
#         if self.current_token.type == token_type:
#             self.current_token = self.lexer.get_next_token()
#         else:
#             self.error()
#
#     def factor(self):
#         """factor : INTEGER | LPAREN expr RPAREN"""
#         token = self.current_token
#         if token.type == INTEGER:
#             self.eat(INTEGER)
#             return token.value
#         elif token.type == LPAREN:
#             self.eat(LPAREN)
#             result = self.expr()
#             self.eat(RPAREN)
#             return result
#
#     def term(self):
#         """term : factor ((MUL | DIV) factor)*"""
#         result = self.factor()
#
#         while self.current_token.type in (MUL, DIV):
#             token = self.current_token
#             if token.type == MUL:
#                 self.eat(MUL)
#                 result = result * self.factor()
#             elif token.type == DIV:
#                 self.eat(DIV)
#                 result = result / self.factor()
#
#         return result
#
#     def expr(self):
#         """Arithmetic expression parser / interpreter.
#
#         calcify>  14 + 2 * 3 - 6 / 2
#         17
#
#         expr   : term ((PLUS | MINUS) term)*
#         term   : factor ((MUL | DIV) factor)*
#         factor : INTEGER
#         """
#         result = self.term()
#
#         while self.current_token.type in (PLUS, MINUS):
#             token = self.current_token
#             if token.type == PLUS:
#                 self.eat(PLUS)
#                 result = result + self.term()
#             elif token.type == MINUS:
#                 self.eat(MINUS)
#                 result = result - self.term()
#
#         return result
