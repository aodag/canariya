#
import venusian


def test_config(target):
    def dec(test):
        def callback(scanner, name, obj):
            scanner.runner.add_test(obj)
        venusian.attach(test, callback)
        return test
    return dec