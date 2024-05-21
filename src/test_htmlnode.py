#!/usr/bin/env python3

import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._leafnode = LeafNode('p','Sample Text',{"foo":"bar","fizz":"buzz"})
        cls._leafnode_textonly = LeafNode(None, 'Sample Text', None)
        cls._parentnode = ParentNode(
            'parent', [
                cls._leafnode,
                cls._leafnode_textonly,
                cls._leafnode,
                cls._leafnode_textonly
            ]
        )

    @classmethod
    def tearDownClass(cls):
        pass

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            print(LeafNode(None,None,None))
            print(LeafNode(2,"foo",None))

            self._parentnode.props = None
            print(self._parentnode)
            self._parentnode.tag = None
            print(self._parentnode)


    def test_props_to_html(self):
        self.assertEqual(self._leafnode.props_to_html(), ' foo="bar" fizz="buzz"')

    def test_leaf_to_html(self):
        self.assertEqual(
            self._leafnode.to_html(),
            '<p foo="bar" fizz="buzz">Sample Text</p>'
        )
        self.assertEqual(self._leafnode_textonly.to_html(), 'Sample Text')

    def test_parent_to_html(self):
        # Because ParentNode.to_html depends on LeafNode.to_html anyways...
        lazy_long = self._leafnode.to_html()
        lazy_short = self._leafnode_textonly.to_html()
        lazy_very_long = f"<parent>{lazy_long}{lazy_short}" + \
            f"{lazy_long}{lazy_short}</parent>"

        self.assertEqual(
            self._parentnode.to_html(), lazy_very_long
        )

        self.assertEqual(
            ParentNode(
                'great-grandparent',
                [
                    self._leafnode,
                    self._parentnode,
                    ParentNode(
                        'grandparent',
                        [
                            self._parentnode,
                            self._leafnode_textonly
                        ]
                    )
                ]).to_html(),
            f"<great-grandparent>{lazy_long}{lazy_very_long}<grandparent>" + \
            f"{lazy_very_long}{lazy_short}</grandparent></great-grandparent>"
            )
