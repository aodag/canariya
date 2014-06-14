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

    def start_test(self, test, values):
        pass

    def stop_test(self, test):
        pass

    def add_success(self, test, values):
        print("OK", end=" ")
        print(str(test).format(values=values))

    def add_failure(self, test, exc, values):
        print("NG {exc}".format(exc=exc), end=" ")
        print(str(test).format(values=values))

    def add_error(self, test, exc, values):
        print("ERR {exc}".format(exc=exc), end=" ")
        print(str(test).format(values=values))



class TestRunner(object):
    def __init__(self):
        self.registry = AdapterRegistry()

    def scan(self, module):
        module = maybe_dotted(module)
        scanner = venusian.Scanner(runner=self)
        scanner.scan(module)

    def add_test(self, test, values=(), target=None, description=None):
        name = test.__name__
        description = description or test.__doc__
        case = TestCase(name, test, description, values=values, target=target)
        self.registry.register([], ITestCase, name, case)

    def get_tests(self):
        for test in self.registry.lookupAll([], ITestCase):
            yield test

    def run_tests(self):
        result = TextTestResult()
        for name, test in self.get_tests():
            test.run(result)