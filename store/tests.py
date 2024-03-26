from django.test import TestCase

# Create your tests here.
import pytest

from .models import Book

@pytest.mark.django_db
def test_create_book():
    assert 200