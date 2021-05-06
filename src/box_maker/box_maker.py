import pascal_voc_writer
import logging
import sys

from box_maker.utils import random_category_names

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

        self._category_names = random_category_names(self._num_of_categories, self._seed)

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
