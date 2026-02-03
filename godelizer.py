import sympy as sympymath

MATHS_OPERATORS = {
    # arithmetic primitives, techniqually all you need ---
    "0": 1,        # zero
    "S": 2,        # successor
    "+": 3,        # addition
    "×": 4,        # multiplication
    "=": 5,        # equality

    "¬": 6,        # not
    "∧": 7,        # and
    "∨": 8,        # or
    "→": 9,        # implies(if)
    "↔": 10,       # if and only if

    "∀": 11,       # for all
    "∃": 12,       # there exists

    # variables
    "x": 13,
    "y": 14,
    "z": 15,

    "(": 16,
    ")": 27,
    ",": 28,

    "<": 19,
    "≤": 20,
    ">": 21,
    "≥": 22,

    "⊤": 23,       # true
    "⊥": 24,       # false
}

CODE_TO_OPERATOR = {code: token for token, code in MATHS_OPERATORS.items()}

def godel_number(expr):

    tokens = expr.split()
    primes = list(sympymath.primerange(2, 2 + 10 * len(tokens)))

    godelnum = 1
    for i, token in enumerate(tokens):
        input = MATHS_OPERATORS[token]
        godelnum *= primes[i] ** input

    return godelnum


def godel_number_decoder(godelnum):
    if godelnum == 1:
        return "0"

    # factor the gödel number into primes and exponents
    factorisation = sympymath.factorint(godelnum)

    # reconstruct tokens in order of the increasing primes as orignally defined (2, 3, 5, 7, ...)
    tokens = []
    for prime in sorted(factorisation.keys()):
        exponent = factorisation[prime]
        try:
            token = CODE_TO_OPERATOR[exponent]
        except KeyError:
            raise ValueError(f"No matching operator for Gödel exponent {exponent}")
        tokens.append(token)

    return " ".join(tokens)