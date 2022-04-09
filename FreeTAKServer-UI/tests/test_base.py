# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from logging import CRITICAL, disable
disable(CRITICAL)

urls = {
    '': (
        '/fixed_sidebar',
        '/fixed_footer',
        '/plain_page',
        '/page_403',
        '/page_404',
        '/page_500'
    ),
    '/home': (
        '/index',
        '/index2',
        '/index3'
    ),
    '/forms': (
        '/form',
        '/form_advanced',
        '/form_validation',
        '/form_wizards',
        '/form_upload',
        '/form_buttons'
    ),
    '/ui': (
        '/general_elements',
        '/media_gallery',
        '/typography',
        '/icons',
        '/glyphicons',
        '/widgets',
        '/invoice',
        '/inbox',
        '/calendar'
    ),
    '/tables': (
        '/tables',
        '/tables_dynamic'
    ),
    '/data': (
        '/chartjs',
        '/chartjs2',
        '/morisjs',
        '/echarts',
        '/other_charts'
    ),
    '/additional': (
        '/ecommerce',
        '/projects',
        '/project_detail',
        '/contacts',
        '/profile',
        '/pricing'
    )
}

free_access = {'/', '/login', '/page_403', '/page_404', '/page_500'}


def check_pages(*pages):
    def decorator(function):
        def wrapper(user_client):
            function(user_client)
            for page in pages:
                r = user_client.get(page, follow_redirects=True)
                assert r.status_code == 200
        return wrapper
    return decorator


def check_blueprints(*blueprints):
    def decorator(function):
        def wrapper(user_client):
            function(user_client)
            for blueprint in blueprints:
                for page in urls[blueprint]:
                    r = user_client.get(blueprint + page, follow_redirects=True)
                    assert r.status_code == 200
        return wrapper
    return decorator

## Base test
# test the login system: login, user creation, logout
# test that all pages respond with HTTP 403 if not logged in, 200 otherwise


def test_authentication(base_client):
    for blueprint, pages in urls.items():
        for page in pages:
            page_url = blueprint + page
            expected_code = 200 if page_url in free_access else 403
            r = base_client.get(page_url, follow_redirects=True)
            assert r.status_code == expected_code


def test_urls(user_client):
    for blueprint, pages in urls.items():
        for page in pages:
            page_url = blueprint + page
            r = user_client.get(page_url, follow_redirects=True)
            assert r.status_code == 200
    # logout and test that we cannot access anything anymore
    r = user_client.get('/logout', follow_redirects=True)
    test_authentication(user_client)
