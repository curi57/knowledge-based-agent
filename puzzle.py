from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# new symbols to complete knowledge0
ASaysAKnight = Symbol("A says he's AKnight")
ASaysAKnave = Symbol("A says he's AKnave")
ASaysBKnave = Symbol("A says B is a Knave")
BSaysBKnave = Symbol("B says he's Knave")


# Puzzle 0 
# A says "I am both a knight and a knave."
knowledge0 = And(
        # A é cavaleiro se e somente se não é patife
        Biconditional(AKnight, Not(AKnave)),
        # A diz que é cavaleiro e patife
        Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 0 
# A says "I am both a knight and a knave."
#true_premise = Biconditional(ASaysAKnight, Not(ASaysAKnave))
#aSays = And(ASaysAKnight, ASaysAKnave)
#lie = Not(true_premise)
#knowledge0 = And(
#        aSays,  
#        Implication(lie, AKnave)
#)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)), 
    Biconditional(BKnight, Not(BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnight))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
 
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
        
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        #("Puzzle 2", knowledge2),
        #("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()