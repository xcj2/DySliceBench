items = {}
recipes = {}


def reset():
    items.clear()
    recipes.clear()


def algorithm():
    while True:
        item_number = int(input())
        if item_number == 0:
            break
        reset()

        for _ in range(item_number):
            item, price = input().split()
            items[item] = int(price)

        recipe_number = int(input())
        for _ in range(recipe_number):
            recipe = input().split()
            r = []
            for i in range(int(recipe[1])):
                r.append(recipe[i + 2])
            recipes[recipe[0]] = r

        for _ in range(len(recipes)):
            for k, v in recipes.items():
                total = 0
                for i in range(len(v)):
                    total += items[v[i]]
                items[k] = items[k] if items[k] < total else total

        target = input()
        print(items[target])


def main():
    algorithm()


if __name__ == '__main__':
    main()