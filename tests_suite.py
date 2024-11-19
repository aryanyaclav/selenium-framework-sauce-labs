import unittest
import HtmlTestRunner

test_modules = ["tests.login_test", 
                "tests.add_to_cart",
                "tests.logout_test"]

suite = unittest.TestSuite()

for module in test_modules:
    try:
        mod = __import__(module, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(module))

# Configure the HTMLTestRunner
runner = HtmlTestRunner.HTMLTestRunner(
    output='test_reports',      # Directory to save the report
    report_name='TestReport',   # Custom report name
    combine_reports=True,       # Combine all reports into a single file
    add_timestamp=True          # Append timestamp to the report name
)

# Run the test suite
runner.run(suite)

#unittest.TextTestRunner().run(suite)