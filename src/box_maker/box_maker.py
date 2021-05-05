import pascal_voc_writer
import random
import logging
import sys
from coolname import generate_slug


def _re_seed(seed=0):
    random.seed(seed)


def _random_category_names(num, seed=None, with_index=True):
    logging.debug('_random_category_names: {}, {}'.format(num, seed))
    if seed is not None:
        _re_seed(seed)

    def output(i):
        if with_index:
            return '{}-{}'.format(generate_slug(2), str(i+1).zfill(num_of_leading_zero))
        else:
            return '{}'.format(generate_slug(2))

    num_of_leading_zero = len(str(num))
    return [output(i) for i in range(num)]


class BoxMaker:
    def __init__(self,
                 num_of_categories,
                 verbose=False,
                 seed: int = None,
                 count: int = 10,
                 **kwargs):
        if verbose:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug('seed: {}'.format(seed))

        self._seed = seed
        self._count = count
        self._num_of_categories = num_of_categories

        self._category_names = _random_category_names(self._num_of_categories, self._seed)

        logging.debug('self._category_names: {}'.format(str(self._category_names)))

    def test(self):
        writer = pascal_voc_writer.Writer(
            path='hello.jpg',
            width=600,
            height=400,
        )

        writer.addObject(
            name='category1',
            xmin=10,
            ymin=20,
            xmax=30,
            ymax=40,
        )

        writer.save('this.xml')

    def hello(self):
        print('Hello world!')
