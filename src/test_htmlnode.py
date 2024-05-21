#!/usr/bin/env python3

import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._leafnode = LeafNode('p','Sample Text',{"foo":"bar","fizz":"buzz"})
        cls._leafnode_textonly = LeafNode(None, 'Sample Text', None)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            print(LeafNode(None,None,None))

    def test_props_to_html(self):
        self.assertEqual(self._leafnode.props_to_html(), ' foo="bar" fizz="buzz"')

    def test_leaf_to_html(self):
        self.assertEqual(
            self._leafnode.to_html(),
            '<p foo="bar" fizz="buzz">Sample Text</p>'
        )
        self.assertEqual(self._leafnode_textonly.to_html(), 'Sample Text')
