===================
canariya
===================

::

    from testfixtures import compare
    from inspirated import testcase_config, test_config


    @testcase_config(target='your.product.Foo')
    class TestFoo(object):

      @test_config(params=[({'var': 1}, 4)])
      def test_it(self, target, var, expected):
          foo = target()
          result = foo.some_method(var)
          compare(result, expected)
