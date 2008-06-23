import mocker

import zope.component
import zope.component.testing

from plone.mocktestcase import dummy

class MockTestCase(mocker.MockerTestCase):
    """Base class for mocker-based mock tests. There are convenience methods
    to make mock testing easier.
    """
    
    # Ensure that we tear down the CA after each test method

    def tearDown(self):
        super(MockTestCase, self).tearDown()
        zope.component.testing.tearDown(self)
    
    # For the lazy
    
    def replay(self):
        self.mocker.replay()
    
    # Helper to create a dummy object with a particular __dict__
    
    def create_dummy(self, **kw):
        return dummy.Dummy(**kw)
    
    # Help register mock components. The tear-down method will
    # wipe the registry each time.
    
    def mock_utility(self, mock, provides, name=u""):
        """Register the mock as a utility providing the given interface 
        """
        zope.component.provideUtility(provides=provides, component=mock, name=name)
    
    def mock_adapter(self, mock, provides, adapts, name=u""):
        """Register the mock as an adapter providing the given interface 
        and adapting the given interface(s)
        """
        zope.component.provideAdapter(factory=mock, adapts=adapts, provides=provides, name=name)
    
    def mock_subscription_adapter(self, mock, provides, adapts):
        """Register the mock as a utility providing the given interface 
        """
        zope.component.provideSubscriptionAdapter(factory=mock, provides=provides, adapts=adapts)
    
    def mock_handler(self, mock, adapts):
        """Register the mock as a utility providing the given interface 
        """
        zope.component.provideHandler(factory=mock, adapts=adapts)
    
    # Matcher functions
    
    def match_provides(self, interface):
        """A function parameter matches that checks whether the given
        interface is provided by the function argument, e.g.

            some_mock = self.mocker.mock()
            some_mock.foo(self.match_provides(IFoo))
        
        This will ensure that foo() is called on some_mock with an object
        that provides IFoo.
        """
        return mocker.MATCH(lambda x: interface.providedBy(x))

    def match_type(self, type):
        """A function parameter matches that checks whether the function
        argument is an instance of the given type, e.g.:

            some_mock = self.mocker.mock()
            some_mock.foo(self.match_isinstance(basestring))
        
        This will ensure that foo() is called on some_mock with an object
        that is a string
        """
        return mocker.MATCH(lambda x: isinstance(x, type))