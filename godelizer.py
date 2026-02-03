import sympy as sp

MATHS_OPERATORS = {
    # from these 5 self reference is assured, they encode the system of basic aritmetic
    "0": 1,
    "S": 2,
    "+": 3,
    "x": 4,
    "=": 5,
}


def godel_number(expr):


    tokens = expr.split()
    primes = list(sp.primerange(2, 2 + 10 * len(tokens)))

    godelnum = 1
    for i, token in enumerate(tokens):
        input = MATHS_OPERATORS[token]
        godelnum *= primes[i] ** input

    return godelnum