import unittest
import program

class TestProgram(unittest.TestCase):
    def test_start(self):
        result=program.start=str
        self.assertTrue(result,str)
    def test_stop(self):
        result=program.stop=str
        self.assertTrue(result,str)
    def test_accelerator(self):
        result=program.accelerator=float
        self.assertEqual(result,float)
    def test_gear(self):
        result=program.gear=str
        self.assertTrue(result,str)


if __name__ == "__main__":
    unittest.main()