from argparse import ArgumentTypeError


def check_positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise ArgumentTypeError('{} is not a positive value'.format(value))
    return ivalue


def extract_numbers(num_str):
    """Extract all available numerical values from passed string.

    :rtype: list
    """
    _num_str = num_str.strip('[ ]').replace('[', '').replace(']', '').replace('\n', '').replace('\\', '')
    return list(map(float, _num_str.split()))
