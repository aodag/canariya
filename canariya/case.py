from zope.interface import implementer
from .interfaces import ITestCase


@implementer(ITestCase)
class TestCase(object):
    def __init__(self, name, func, description, values=(None), target=None):
        self.name = name
        self.func = func
        self.values = values
        self.target = target
        self.description = description

    def run(self, result):
        for values in self.values:
            result.start_test(self, values)
            try:
                if isinstance(values, dict):
                    self.func(**values)
                else:
                    self.func()
            except AssertionError as e:
                result.add_failure(self, e, values)
            except Exception as e:
                result.add_error(self, e, values)
            else:
                result.add_success(self, values)
            result.stop_test(self)

    def __str__(self):
        return self.name + (self.description if self.description else "")