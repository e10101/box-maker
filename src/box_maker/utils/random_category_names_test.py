from absl.testing import absltest

from box_maker.utils import random_category_names


class RandomCategoryNamesTest(absltest.TestCase):
    def test_num_of_category_names(self):
        '''Should return correct length by settings.'''
        self.assertLen(random_category_names(10), 10)
        self.assertLen(random_category_names(12), 12)
        self.assertLen(random_category_names(0), 0)

    def test_with_index(self):
        '''Should append index by flagging.'''
        result_with_index = random_category_names(10, seed=1, with_index=True)
        result_without_index = random_category_names(10, seed=1, with_index=False)

        self.assertEqual(len(result_with_index), len(result_without_index))

        for idx, w, wo in zip(
                range(len(result_with_index)),  # index
                result_with_index,  # with
                result_without_index,  # without
        ):
            # e.g.
            # w: fluorescent-puffin-07
            # wo: fluorescent-puffin
            # idx: 7
            self.assertEqual(str(w)[:-3], str(wo))
            self.assertEqual(str(idx+1).zfill(2), str(w)[-2:])

    def test_default_with_index_value(self):
        '''The default value of `with_index` should be True.'''
        result_default = random_category_names(2, seed=1)
        result_with_index_true = random_category_names(2, seed=1, with_index=True)

        self.assertEqual(result_default, result_with_index_true)

    def test_seed(self):
        '''Should use `seed` to control randomness.'''
        result_seed_0 = random_category_names(10, seed=0)
        result_seed_1 = random_category_names(10, seed=1)
        result_seed_1_again = random_category_names(10, seed=1)

        self.assertNotEqual(result_seed_0, result_seed_1)
        self.assertEqual(result_seed_1, result_seed_1_again)

    def test_default_seed_value(self):
        '''The default value of `seed` should be None.'''
        self.assertNotEqual(
            random_category_names(2),
            random_category_names(2)
        )

    def test_different_words(self):
        '''Should able to use `words` to control category name's length.'''
        def all_should_between(arr, min, max):
            for item in arr:
                self.assertBetween(
                    len(str(item).split('-')),
                    min,
                    max,
                    'item: {}'.format(str(item))
                )

        words1 = random_category_names(100, seed=1, with_index=False, words=1)
        words2 = random_category_names(100, seed=1, with_index=False, words=2)
        words3 = random_category_names(100, seed=1, with_index=False, words=3)
        words4 = random_category_names(100, seed=1, with_index=False, words=4)
        words5 = random_category_names(100, seed=1, with_index=False, words=5)
        words10 = random_category_names(100, seed=1, with_index=False, words=10)

        # Min words should be 2
        self.assertEqual(words1, words2)

        all_should_between(words2, 2, 2)  # brown-fox
        all_should_between(words3, 3, 4)  # robin-of-infinite-feminism or flat-successful-husky
        all_should_between(words4, 5, 5)  # heavenly-stylish-moose-of-excitement

        # Max words should be 4
        self.assertEqual(words4, words5)
        self.assertEqual(words4, words10)


if __name__ == '__main__':
    absltest.main()
