import unittest

class StringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip('skip one case fornow')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hell world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    myCase = unittest.TestLoader().loadTestsFromTestCase(StringMethods)
    print (type(myCase))
    # r = unittest.TextTestRunner(verbosity=0).run(myCase)
    # print (r.failures[0][0].id())