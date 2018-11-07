from nose_parameterized import parameterized
import unittest

login_data = [(1, 3, 4), (1, 2, 1)]


class TestAdd(unittest.TestCase):
    """
        参数化
    """
    # @parameterized.expand([(1, 3, 4), (1, 2, 1)])
    # def test_add(self, a, b, c):
    #     self.assertEqual(a + b, c)

    @unittest.skipIf(True, '这是测试代码，不需要执行')
    @parameterized.expand(login_data)
    def test_add(self, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == '__main__':
    unittest.main()
