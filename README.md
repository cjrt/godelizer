## Godelizer

<img width="1083" height="637" alt="image" src="https://github.com/user-attachments/assets/938c9749-6ac3-436e-bd0a-22a5ad695397" />

In the 1920s, mathematicians around the world were racing to resolve three fundamental questions lying at the very heart of mathematics.

Is mathematics complete?
Can every true mathematical statement be proven from a finite set of axioms?

Is mathematics consistent?
Can the axioms of mathematics be guaranteed never to lead to a contradiction?

Is mathematics decidable?
Does there exist a procedure that can determine whether any given mathematical statement is provable from the axioms?

Gödelizer is a program that assigns Gödel numbers to user input by encoding mathematical symbols and formulas as natural numbers. The specific numerical assignment of symbols is arbitrary: as long as every symbol is assigned a unique number, the encoding is valid.

For example, assigning the Gödel number 
2 to the symbol 
0 and 1 to the successor symbol S would not break the system. 
However, changing the encoding after formulas have already been generated will make those Gödel numbers incompatible—so it is best to choose an encoding scheme once and stick with it.

## Godel numbers

Gödel numbering was invented by Kurt Gödel in his 1931 paper
*On Formally Undecidable Propositions of Principia Mathematica and Related Systems*.[^1]

Gödel numbers allow mathematics to encode statements and proofs as numbers, enabling mathematics to talk about its own syntax.
This self-reference was essential in proving that sufficiently powerful formal systems are incomplete and cannot prove their own consistency.

### How they work

Godel wanted to use logic and mathematics to answer questions about logic and mathematics.

We take the basic systems of a mathematical system and give each one a unique number, which is its godel number.

<img width="67" height="270" alt="image" src="https://github.com/user-attachments/assets/30d5360c-998f-4610-b928-422578065f38" />

To encode numbers you apply the succesor operator to zero, so for example to write 3 you S(S(S(0))). This makes it possible to represent any positive integer.

To write equations and assign godel numbers to them, example 0 = 0, turn them into their godel numbers 1,5,1 and assign the equation its own godel number by taking the prime numbers starting with the first 2, 
and raise it to the power of the godel number of the equation.

<img width="447" height="452" alt="image" src="https://github.com/user-attachments/assets/603f7f2e-bec7-4309-898c-61310f0ff05e" />

The remarkable feature of Gödel numbering is that it allows all of mathematics to be encoded as numbers.
Not only individual formulas, but entire proofs—and even the axioms themselves—can be represented arithmetically.

For example, Peano’s first axiom,
¬(Sx=0),
can be encoded as a single natural number using the same Gödelization process applied to any other formula.

## Dependencies 

Uses sympy and NiceGUI

https://www.sympy.org/en/index.html

https://nicegui.io/



[^1]: https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf
