import unittest

# import test case module
import loginTest
import productTest

# initial test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add test case to the test suite
suite.addTests(loader.loadTestsFromModule(loginTest))
suite.addTests(loader.loadTestsFromModule(productTest))

# initial a runner
runner = unittest.TextTestRunner(verbosity=1)

result = runner.run(suite)