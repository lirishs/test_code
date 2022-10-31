import unittest

class demo3(unittest.TestCase):
    def setUp(self):
        print("demo3 setUp")   #数据初始化

    def tearDown(self):
        print("demo3 tearDown")

    def test_case02(self):
        print("demo3 testcase02")
        self.assertIn("a", "ab")


class demo4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("demo4 setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("demo4 tearDownClass")

    def setUp(self):
        print("demo2 setUp")   #数据初始化

    def tearDown(self):
        print("demo4 tearDown")

    def test_case01(self):
        print("demo4 testcase01")
        self.assertEqual("1","2","测试失败")

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo3)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(demo4)
    suite_all = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner().run(suite_all)
