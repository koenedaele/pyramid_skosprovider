# -*- coding: utf8 -*-

from __future__ import unicode_literals

from pyramid.config import Configurator

from pyramid.compat import (
    ascii_native_,
    string_types
)

import json

from webtest import TestApp

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from pyramid_skosprovider.tests import (
    trees
)

def skosmain(global_config, **settings):
    """ 
    This function returns a Pyramid WSGI application.
    """
    
    # Set up pyramid
    config = Configurator(settings=settings)

    config.include('pyramid_skosprovider')

    skosregis = config.get_skos_registry()
    skosregis.register_provider(trees)

    return config.make_wsgi_app()

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        settings = {}
        app = skosmain({}, **settings)
        self.testapp = TestApp(app)

    def tearDown(self):
        del self.testapp

class RestFunctionalTests(FunctionalTests):

    def test_get_conceptschemes_json(self):
        res = self.testapp.get('/conceptschemes', {'Accept': 'application/json'})
        self.assertEqual('200 OK', res.status)
        self.assertIn('application/json', res.headers['Content-Type'])
        data = json.loads(res.body.decode('utf-8'))
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    def test_get_conceptschemes_trees_concepts_json(self):
        res = self.testapp.get(
            '/conceptschemes/TREES/concepts', 
            {'Accept': 'application/json'}
        )
        self.assertEqual('200 OK', res.status)
        self.assertIn('application/json', res.headers['Content-Type'])
        self.assertIsInstance(res.headers['Content-Range'], string_types)
        self.assertEqual('items 0-2/3', res.headers['Content-Range'])
        data = json.loads(res.body.decode('utf-8'))
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
