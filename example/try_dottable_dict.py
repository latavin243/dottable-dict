from dottable_dict import DottableDict


def main():
    raw_dict = {"a": "aa", "b": 2}
    d = DottableDict(**raw_dict)
    # same as: d = DottableDict(a="aa", b=2)
    print(d)  # {'a': 'aa', 'b': 2}
    print(d.a)  # aa
    print(d.b)  # 2
    del d.a
    print(d)  # {'b': 2}


if __name__ == "__main__":
    main()
