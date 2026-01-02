count = int(input());
data = input().split(" ");

def bubble_sort(data):
    # print(data);
    count = len(data);
    for i in range(count):
        for j in range(count - 1, i, -1):
            if data[j][1] < data[j - 1][1]:
                data[j], data[j - 1] = data[j - 1], data[j];
        # print(data);

def selection_sort(data):
    count = len(data);
    # print(data);
    for i in range(count - 1):
        minI = i;
        for j in range(i + 1, count):
            if data[j][1] < data[minI][1]:
                minI = j;
        if i != minI:
            data[i], data[minI] = data[minI], data[i];
        # print(data);

def show(data):
    print(" ".join(data));

A = list(data);
bubble_sort(A);
show(A);
print("Stable");

B = list(data);
selection_sort(B);
show(B);
if A == B:
    print("Stable");
else:
    print("Not stable");
