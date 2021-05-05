import logging
from coolname import generate_slug
from .re_seed import re_seed


def random_category_names(num, seed=None, with_index=True):
    logging.debug('_random_category_names: {}, {}'.format(num, seed))
    if seed is not None:
        re_seed(seed)

    num_of_leading_zero = len(str(num))

    def output(i):
        if with_index:
            return '{}-{}'.format(generate_slug(2), str(i+1).zfill(num_of_leading_zero))
        else:
            return '{}'.format(generate_slug(2))

    return [output(i) for i in range(num)]
