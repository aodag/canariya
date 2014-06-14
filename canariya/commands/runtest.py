from ..runner import TestRunner


class RunTestCommand(object):
    def __init__(self):
        self.runner = TestRunner()

    def __call__(self, args):
        self.runner.scan(args.module)
        print(list(self.runner.get_tests()))
        self.runner.run_tests()