from __future__ import unicode_literals

import uuid

import pytest

import coid


@pytest.mark.parametrize('prefix,encoding', [
    (None, 'hex'),
    ('krazee-', 'hex'),
    (None, 'hex'),
    (None, 'base58'),
    ('eyez-', 'base58'),
    (None, 'base62'),
    ('killa-', 'base62'),
])
def test_codec(prefix, encoding):
    id = uuid.uuid4()
    codec = coid.Id(prefix=prefix, encoding=encoding)
    assert id == codec.decode(codec.encode(id))
