def bubble_sort(sequence):
    for i in range(len(sequence)):
        for j in range(len(sequence)-1, i, -1):
            if int(sequence[j-1][1]) > int(sequence[j][1]):
                sequence[j], sequence[j-1] \
                    = sequence[j-1], sequence[j]
    return sequence


def selection_sort(sequence):
    for i in range(len(sequence)):
        mini = i
        for j in range(i, len(sequence)):
            if int(sequence[j][1]) < int(sequence[mini][1]):
                mini = j
        sequence[i], sequence[mini] = sequence[mini], sequence[i]
    return sequence   


def main():
    input()
    cards = input().split()
    bubble = bubble_sort(cards[:])
    selection = selection_sort(cards[:])
    stable = sorted(cards, key=lambda card: int(card[1]))
    print(' '.join(bubble))
    print('Stable' if bubble == stable else 'Not stable')
    print(' '.join(selection))
    print('Stable' if selection == stable else 'Not stable')


if __name__ == "__main__":
    main()

