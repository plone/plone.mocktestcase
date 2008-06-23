Introduction
============

This package contains a unittest test class based on the one from the
``Mocker`` mock library (http://labix.org/mocker).

This class provides support for registering Zope 3 components (utilities,
adapters, subscription adapters and event handlers) from mocks and tearing 
down the global component registry during test tear-down.

There are also a few convenience methods and parameter checkers that are
useful to Zope and Plone testing.

Please see the Mocker documentation for more detail:

    http://labix.org/mocker

See testcase.py for more detail on the mock helper methods.

A test case that mocks a utility may look like this::

    from plone.mocktestcase import MockTestCase
    
    from my.package.interfaces import IMyInterface
    from my.package.foo import testable_method

    class MyTestCase(MockTestCase):
    
        def test_something(self):

            utility_mock = self.mocker.mock()
            self.expect(utility_mock.do_something()).result("foo")
            self.mock_utility(utility_mock, IMyInterface)
        
            # Put mocker into replay mode
            self.replay()
        
            # Verify that testable_method() looks up a utility for 
            # IMyInterface and calls do_something() on it, which returns
            # "foo".
        
            testable_method()
