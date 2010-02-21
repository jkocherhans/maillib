from maillib.utils import extract_list_id
import unittest


class ListIdsTest(unittest.TestCase):
    def test_basic_list_id(self):
        value = '<django-developers.googlegroups.com>'
        self.assertEqual(extract_list_id(value), 'django-developers.googlegroups.com')

    def test_apple_list_id(self):
        value = 'Discussions regarding native Mac OS X application developments using\n\tCocoa frameworks <cocoa-dev.lists.apple.com>'
        self.assertEqual(extract_list_id(value), 'cocoa-dev.lists.apple.com')


if __name__ == '__main__':
    unittest.main()

