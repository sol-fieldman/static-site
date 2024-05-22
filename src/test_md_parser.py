#!/usr/bin/env python3

import unittest
from md_parser import *

class Test_Parsing(unittest.TestCase):

    def setUp(self):
        self.text_with_img = "The quick brown fox ![fox](https://foo.bar/fox.jpg)" +\
            " jumps over the lazy dog ![dog](https://foo.bar/dog.jpg)"
        self.text_with_link = "I use [backend courses](https://boot.dev)" +\
            " to inflate [my ego](https://github.com/sol-fieldman)"

    def test_img_extract(self):
        self.assertEqual(
            extract_md_img(self.text_with_img),
            [
                ("fox", "https://foo.bar/fox.jpg"),
                ("dog", "https://foo.bar/dog.jpg")
            ]
        )

    def test_link_extract(self):
        self.assertEqual(
            extract_md_link(self.text_with_link),
            [
                ("backend courses", "https://boot.dev"),
                ("my ego", "https://github.com/sol-fieldman")
            ]
        )
