#!/usr/bin/env python3

from enum import Enum
from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class ValidTextTypes(str, Enum):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    text_type_heading1 = "heading1"
    text_type_heading2 = "heading2"
    text_type_heading3 = "heading3"

def text_node_to_html_node(text_node):
    used_type = text_node.text_type.lower()
    if used_type == ValidTextTypes.text_type_heading1:
        return LeafNode('h1',text_node.text)
    elif used_type == ValidTextTypes.text_type_heading2:
        return LeafNode('h2',text_node.text)
    elif used_type == ValidTextTypes.text_type_heading3:
        return LeafNode('h3',text_node.text)

    elif used_type == ValidTextTypes.text_type_text:
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


def main():
    test_textnode = TextNode("This is a test","Bold","https://localhost:8080")
    print(test_textnode)
    test_htmlnode = HTMLNode(None,None,None,{"foo":"bar","fizz":"buzz"})
    print(test_htmlnode.props_to_html())
    print(text_node_to_html_node(test_textnode))

main()
