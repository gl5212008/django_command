

def foo(*aaa, **bbb):
    # print(args[0])
    print(bbb)


if __name__ == '__main__':
    # foo(*[1, 2, 3])
    foo(**{"name": "alex", "age": 9000})
    foo(name="alex", age=9000)
