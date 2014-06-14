from zope.interface import implementer
from .interfaces import ITestCase


@implementer(ITestCase)
class TestCase(object):
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description

    def run(self, result):
        result.start_test(self)
        try:
            self.func()
        except AssertionError as e:
            result.add_failure(self, e)
        except Exception as e:
            result.add_error(self, e)
        else:
            result.add_success(self)
        result.stop_test(self)