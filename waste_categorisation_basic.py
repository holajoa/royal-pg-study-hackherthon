"""This is a simple implementation of the waste categorising game."""


# wastes and categories to be paired together
wastes = [1, 2, 3, 4]
cats = ['a', 'b', 'c', 'd']

sol = ['1a', '2b', '3c', '4d']    # solutions


def verify_answer(a, ans):
    if int(a[0]) not in wastes:
        raise ValueError(f'{a[0]} is not an available waste')
    elif a[1] not in cats:
        raise ValueError(f'{a[1]} is not an available category')
    for wc in ans:
        if wc:
            if int(a[0]) == wc[0]:
                raise ValueError(
                        f'waste {wc[0]} already paired with category {wc[1]}'
                    )
            if a[1] == wc[1]:
                raise ValueError(
                        f'category {wc[1]} already paired with waste {wc[0]}'
                    )


def start():
    print('wastes:', wastes)
    print('categories:', cats)
    ans = []
    count = 0
    while count < len(wastes):
        a = input(
            "Make a pair! (eg. input '1a' to assign category a to waste 1)"
        )
        try:
            verify_answer(a, ans)
        except ValueError as ve:
            print(ve)
        else:
            ans.append(a)
            count += 1

    if sorted(ans) == sol:
        print('U r correct!')
    else:
        print('Please try again:(')


fdbk = input('Welcome! Start a new game? (Y)')
if fdbk == 'Y':
    start()
else:
    print('Bye-bye!')
