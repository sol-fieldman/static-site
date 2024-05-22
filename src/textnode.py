#!/usr/bin/env python3

from htmlnode import *
from md_parser import *

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
    out_nodes = []
    for node in old_nodes:
        if node.text_type != ValidTextTypes.text:
            out_nodes.append(node)
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
        out_nodes.extend(new_segments)
    return out_nodes

def split_nodes_img(old_nodes):
    out_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        images = extract_md_img(node.text)
        if len(images) == 0:
            out_nodes.append(node)
            continue
        image_tup = images.pop()
        new_texts = node.text.split(f"![{image_tup[0]}]({image_tup[1]})",1)
        if new_texts[1] == "":
            new_nodes = [
                TextNode(image_tup[0],ValidTextTypes.image,image_tup[1]),
            ]
        else:
            new_nodes = [
                TextNode(image_tup[0],ValidTextTypes.image,image_tup[1]),
                TextNode(new_texts[1],node.text_type)
            ]

        new_nodes = split_nodes_img([TextNode(new_texts[0],node.text_type)]) + \
            new_nodes
        out_nodes.extend(new_nodes)
    return out_nodes

def split_nodes_link(old_nodes):
    out_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        links = extract_md_link(node.text)
        if len(links) == 0:
            out_nodes.append(node)
            continue
        link_tup = links.pop()
        new_texts = node.text.split(f"[{link_tup[0]}]({link_tup[1]})",1)
        if len(new_texts) == 2 and new_texts[1] == "":
            new_nodes = [
                TextNode(link_tup[0],ValidTextTypes.link,link_tup[1]),
            ]
        else:
            new_nodes = [
                TextNode(link_tup[0],ValidTextTypes.link,link_tup[1]),
                TextNode(new_texts[1],node.text_type)
            ]

        new_nodes = split_nodes_link([TextNode(new_texts[0],node.text_type)]) + \
            new_nodes
        out_nodes.extend(new_nodes)
    return out_nodes

def text_to_textnodes(txt):
    nodes = [TextNode(txt)]
    nodes = split_nodes_delimiter(nodes,"**",ValidTextTypes.bold)
    nodes = split_nodes_delimiter(nodes,"*",ValidTextTypes.italic)
    nodes = split_nodes_delimiter(nodes,"`",ValidTextTypes.code)
    nodes = split_nodes_img(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

print(text_to_textnodes("nesting is **very** *scary*"))
