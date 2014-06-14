import venusian
from zope.interface.adapter import AdapterRegistry
from zope.dottedname.resolve import resolve
from .case import TestCase
from .interfaces import ITestCase


def maybe_dotted(d):
    if isinstance(d, str):
        return resolve(d)
    return d

def run_tests(module):
    module = maybe_dotted(module)
    registry = AdapterRegistry()
    scanner = venusian.Scanner(registry=registry)
    scanner.scan(module)


class TextTestResult(object):
    def __init__(self):
        pass

    def start_test(self, test):
        print(test)

    def stop_test(self, test):
        print(test)

    def add_success(self, test):
        print("OK")


class TestRunner(object):
    def __init__(self):
        self.registry = AdapterRegistry()

    def scan(self, module):
        module = maybe_dotted(module)
        scanner = venusian.Scanner(runner=self)
        scanner.scan(module)

    def add_test(self, test):
        name = test.__name__
        description = test.__doc__
        case = TestCase(name, test, description)
        self.registry.register([], ITestCase, name, case)

    def get_tests(self):
        for test in self.registry.lookupAll([], ITestCase):
            yield test

    def run_tests(self):
        result = TextTestResult()
        for name, test in self.get_tests():
            test.run(result)