import unittest

class demo1(unittest.TestCase):
    def setUp(self):
        print("demo1 setUp")   #数据初始化

    def tearDown(self):
        print("demo1 tearDown")

    def test_case02(self):
        print("demo1 testcase02")
        self.assertIn("a", "ab")


class demo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("demo2 setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("demo2 tearDownClass")

    def setUp(self):
        print("demo2 setUp")   #数据初始化

    def tearDown(self):
        print("demo2 tearDown")

    def test_case01(self):
        print("demo2 testcase01")
        self.assertEqual("1","2","测试失败")

if __name__ == '__main__':
    test_dir = "./"
    discover_case = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    unittest.TextTestRunner().run(discover_case)