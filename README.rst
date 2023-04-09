This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

Introduction
============

LEGACY: Do not use this any longer, better use the Python mock module!

This package contains a unittest test class based on the one from the
``Mocker`` mock library (http://labix.org/mocker).

This class provides support for registering Zope 3 components (utilities,
adapters, subscription adapters and event handlers) from mocks and tearing
down the global component registry during test tear-down.

There are also a few convenience methods and parameter checkers that are
useful to Zope and Plone testing.

Please see the Mocker documentation for more detail:

    http://labix.org/mocker

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

The following helper methods are available:

   self.replay()
     Puts the mock into replay mode.

   self.create_dummy(**kw)
     Return a dummy object that is *not* a mock object, just a dumb object
     with whatever attributes or methods you pass as keyword arguments.
     To make a dummy method, pass a function object or a lambda, e.g.
     self.create_dummy(id="foo", absolute_url=lambda:'http://example.org/foo')

   self.mock_utility(mock, provides, name=u"")
     Register the given mock object as a global utility providing the given
     interface, with the given name (defaults to the unnamed default utility).

   self.mock_adapter(mock, provides, adapts, name=u"")
     Register the given mock object as a global adapter providing the given
     interface and adapting the given interfaces, with the given name
     (defaults to the unnamed default adapter).

   self.mock_subscription_adapter(mock, provides, adapts)
     Register the given mock object as a global subscription adapter providing
     the given interface and adapting the given interfaces.

   self.mock_handler(mock, adapts)
     Register the given mock object as a global event subscriber for the
     given event types.

   self.mock_tool(mock, name)
     Create a getToolByName() mock (using 'replace' mode) and configure it so
     that code calling getToolByName(context, name) obtains the given mock
     object. Can be used multiple times: the getToolByName() mock is created
     lazily the first time this method is called in any one test fixture.

   self.match_provides(interface)
     A custom matcher that can be used to check whether an argument to a mock
     call provides the given interface. Uses interface.providedBy(arg).

   self.match_type(type)
     A custom matcher that can be used to check whether an argument to a mock
     call is if the given type. Uses isinstance(arg, type).
