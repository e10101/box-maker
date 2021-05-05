import logging
import coolname

from .re_seed import re_seed


def random_category_names(num, seed=None, with_index=True, words=2):
    logging.debug('_random_category_names: {}, {}'.format(num, seed))
    if seed is not None:
        re_seed(seed)

    num_of_leading_zero = len(str(num))
    words = max(2, min(4, words))

    def output(i):
        if with_index:
            return '{}-{}'.format(
                coolname.generate_slug(words),
                str(i+1).zfill(num_of_leading_zero)
            )
        else:
            return '{}'.format(coolname.generate_slug(words))

    return [output(i) for i in range(num)]
