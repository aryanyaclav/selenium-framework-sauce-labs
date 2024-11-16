import unittest

test_modules = ["tests.login_test"]

suite = unittest.TestSuite()

for module in test_modules:
    try:
        mod = __import__(module, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(module))

unittest.TextTestRunner().run(suite)