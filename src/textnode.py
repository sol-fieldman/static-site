#!/usr/bin/env python3
from enum import Enum

class ValidTextTypes(str, Enum):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

class TextNode:
    def __init__ (self,text,text_type,url):
        self.text = text
        self.text_type = text_type
        if not isinstance(self.text_type,str): raise TypeError("Invalid text type.")

        self.url = url
        if not isinstance(self.url, str): self.url = ''
        if ' ' in self.url: raise ValueError("Invalid URL. URLs do not have spaces")
        if self.url[:8] != 'https://' and self.url[:7] != 'http://':
            raise ValueError("Invalid URL. Please add http(s):// to prefix.")

    def __eq__ (self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    used_type = text_node.text_type.lower()
    if used_type == ValidTextTypes.text_type_text:
        return LeafNode(None,text_node.text)
    elif used_type == ValidTextTypes.text_type_bold:
        return LeafNode('b',text_node.text)
    elif used_type == ValidTextTypes.text_type_italic:
        return LeafNode('i',text_node.text)
    elif used_type == ValidTextTypes.text_type_code:
        return LeafNode('code',text_node.text)

    elif used_type == ValidTextTypes.text_type_link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    elif used_type == ValidTextTypes.text_type_image:
        return LeafNode('img','',{"src": text_node.url, "alt": text_node.text})
    else: raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != ValidTextTypes.text_type_text:
            new_nodes.append(node)
            continue
        new_segments = []
        old_segments = node.text.split(delimiter)
        if len(old_segments)%2 == 0: raise SyntaxError("Open markdown section")
        for n in range(len(old_segments)):
            if old_segments[n] == "": continue
            if n%2 == 0:
                new_segments.append(
                    TextNode(old_segments[n],ValidTextTypes.text_type_text)
                )
            else:
                new_segments.append(
                    TextNode(old_segments[n],text_type)
                )
        new_nodes.extend(new_segments)
    return new_nodes
