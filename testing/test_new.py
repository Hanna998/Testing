import sys
from unittest import TestCase
from unittest.mock import create_autospec, Mock, patch

foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}