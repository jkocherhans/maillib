import unittest
from maillib import utils


class NormalizeSubjectTest(unittest.TestCase):
    def test_basic_re(self):
        self.assertEqual(utils.normalize_subject('RE: test'), 'test')
        self.assertEqual(utils.normalize_subject('Re: test'), 'test')
        self.assertEqual(utils.normalize_subject('re: test'), 'test')

    def test_basic_fwd(self):
        self.assertEqual(utils.normalize_subject('fw: test'), 'test')
        self.assertEqual(utils.normalize_subject('fwd: test'), 'test')

class ListIdsTest(unittest.TestCase):
    def test_basic_list_id(self):
        value = '<django-developers.googlegroups.com>'
        self.assertEqual(utils.extract_list_id(value), 'django-developers.googlegroups.com')

    def test_apple_list_id(self):
        value = 'Discussions regarding native Mac OS X application developments using\n\tCocoa frameworks <cocoa-dev.lists.apple.com>'
        self.assertEqual(utils.extract_list_id(value), 'cocoa-dev.lists.apple.com')


if __name__ == '__main__':
    unittest.main()

