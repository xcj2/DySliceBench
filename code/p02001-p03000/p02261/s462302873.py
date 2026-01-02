import copy

class suit():
    def __init__(self, card):
        self.s = card
    def value(self):
        return int(self.s[1])

def bubblesort(seq):
    for i in range(len(seq)):
        for j in reversed(range(i + 1, len(seq))):
            if seq[j].value() < seq[j - 1].value() :
                seq[j], seq[j - 1] = seq[j - 1], seq[j]

    return seq

def selectionsort(seq):
    for i in range(len(seq)):
        mini = i
        for j in range(i, len(seq)):
            if seq[j].value() < seq[mini].value():
                mini = j

        seq[i], seq[mini] = seq[mini], seq[i]

    return seq

def is_stable(inp, out):
    for i in range(len(inp)):
        if inp[i] != out[i]:
            return "Not stable"
    return "Stable"

def main():
    cards = list()
    n = int(input())

    for card in input().split():
        cards.append(suit(card))

    seq1 = copy.copy(cards)
    seq2 = copy.copy(cards)

    seq1 = bubblesort(seq1)
    seq2 = selectionsort(seq2)

    print(seq1[0].s, end="")
    for i in range(1, len(seq1)):
        print(" " + seq1[i].s, end = "")
    print("\nStable")

    print(seq2[0].s, end="")
    for i in range(1, len(seq2)):
        print(" " + seq2[i].s, end = "")
    print("\n" + is_stable(seq1, seq2), end="")
    print()

main()
