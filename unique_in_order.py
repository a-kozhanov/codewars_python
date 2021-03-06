"""
https://www.codewars.com/kata/unique-in-order/train/python

Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    if type(iterable) == int:
        print(type(iterable))
    else:
        s = ''.join([iterable[i] for i in range(len(iterable) - 1) if iterable[i + 1] != iterable[i]] + [iterable[-1]])
        return list(s)


if __name__ == "__main__":
    print(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
    print(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
    print(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
    print(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])


