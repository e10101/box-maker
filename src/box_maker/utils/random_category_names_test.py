from absl.testing import absltest

from box_maker.utils import random_category_names

class RandomCategoryNamesTest(absltest.TestCase):
    def test_num_of_category_names(self):
        self.assertLen(random_category_names(10), 10)
        self.assertLen(random_category_names(12), 12)
        self.assertLen(random_category_names(0), 0)

    def test_with_index(self):
        pass

    def test_seed(self):
        pass

    def test_different_words(self):
        random_category_names(10)
        pass

if __name__ == '__main__':
    absltest.main()