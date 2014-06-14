#
import venusian


def test_config(target, values=(None,), description=None):
    def dec(test):
        def callback(scanner, name, obj):
            scanner.runner.add_test(
                obj, target=target, values=values, description=description)
        venusian.attach(test, callback)
        return test
    return dec