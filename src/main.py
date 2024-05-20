#!/usr/bin/env python3

from textnode import TextNode

def main():
    test = TextNode("This is a test","bold","https://localhost:8080")
    print(test)
    print(type(test.url))

main()
