#!/usr/bin/env python3

from textnode import TextNode
from htmlnode import HTMLNode

def main():
    test_textnode = TextNode("This is a test","bold","https://localhost:8080")
    print(test_textnode)
    test_htmlnode = HTMLNode(None,None,None,{"foo":"bar","fizz":"buzz"})
    print(test_htmlnode.props_to_html())

main()
