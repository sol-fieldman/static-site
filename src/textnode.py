#!/usr/bin/env python3
from htmlnode import *

class ValidTextTypes:
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

class TextNode:
    def __init__ (self,text,text_type=ValidTextTypes.text,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.test_self()

    def test_self(self):
        if not isinstance(self.text_type,str): raise TypeError("Invalid text type.")
        if not isinstance(self.url, str):
            self.url = ''
        else:
            if ' ' in self.url: raise ValueError("Invalid URL. URLs do not have spaces")
            if len(self.url) != 0 and self.url[:8] != 'https://' and self.url[:7] != 'http://':
                raise ValueError("Invalid URL. Please add http(s):// to prefix.")

    def __eq__ (self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__ (self):
        self.test_self()
        return f'TextNode("{self.text}", "{self.text_type}", "{self.url}")'

def text_node_to_html_node(text_node):
    used_type = text_node.text_type.lower()
    if used_type == ValidTextTypes.text:
        return LeafNode(None,text_node.text)
    elif used_type == ValidTextTypes.bold:
        return LeafNode('b',text_node.text)
    elif used_type == ValidTextTypes.italic:
        return LeafNode('i',text_node.text)
    elif used_type == ValidTextTypes.code:
        return LeafNode('code',text_node.text)

    elif used_type == ValidTextTypes.link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    elif used_type == ValidTextTypes.image:
        return LeafNode('img','',{"src": text_node.url, "alt": text_node.text})
    else: raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != ValidTextTypes.text:
            new_nodes.append(node)
            continue
        new_segments = []
        old_segments = node.text.split(delimiter)
        if len(old_segments)%2 == 0: raise SyntaxError("Open markdown section")
        for n in range(len(old_segments)):
            if old_segments[n] == "": continue
            if n%2 == 0:
                new_segments.append(
                    TextNode(old_segments[n],ValidTextTypes.text)
                )
            else:
                new_segments.append(
                    TextNode(old_segments[n],text_type)
                )
        new_nodes.extend(new_segments)
    return new_nodes
