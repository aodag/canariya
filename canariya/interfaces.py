from zope.interface import Interface


class ITestCase(Interface):
    """ test case """

    def run(result):
        """ run test """