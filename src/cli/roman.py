import sys
import logging
import argparse

logger = logging.getLogger(__name__)
roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


def main():

    parser = argparse.ArgumentParser(description="Calculates fibonacci")
    parser.add_argument("val", help="Input for either function")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()

    logging.basicConfig()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
    if args.quiet:
        logger.setLevel(logging.WARN)

    conversions = {
        int: int_to_roman,
        str: roman_to_int,
    }

    fallback = lambda x: "Not a valid input..."

    try:
        val = int(args.val)
    except ValueError:
        pass

    print(conversions.get(type(val), fallback)(val))


def roman_to_int(r):

    r = str(r)
    reverse_roman = {v: k for k, v in roman.items()}
    last_two = r[-2:]

    if len(last_two) == 0:
        return 0
    if len(last_two) == 1:
        return reverse_roman[last_two]

    before_last, last = last_two
    r = r[:-2]

    if before_last and reverse_roman[before_last] < reverse_roman[last]:
        return roman_to_int(
            r) + reverse_roman[last] - reverse_roman[before_last]

    return roman_to_int(r + before_last) + reverse_roman[last]


def int_to_roman(n):

    n = int(n)
    res = ""
    nn = n

    for step in reversed([*roman.keys()]):

        times = n // step

        if not times:
            continue

        if times > 3:
            replacement = list(int_to_roman(nn + 1))
            popped = replacement.pop()
            return "".join(replacement) + roman[1] + popped

        else:
            for _ in range(times):
                res += roman[step]

        n = n % step

    return res


if __name__ == '__main__':
    main()
