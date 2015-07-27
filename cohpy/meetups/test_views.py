from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from meetups.views import home_page


def test_root_url_resolves_to_home_page():
    found = resolve('/')
    assert found.func == home_page

def test_home_page_returns_correct_html():
    request = HttpRequest()
    response = home_page(request)
    expected_html = render_to_string('meetups/home.html')
    assert response.content.decode() == expected_html