#!/usr/bin/env python3

import re
from md_parser import *
from htmlnode import *
from textnode import *

class ValidBlocks:
    p = "p"
    h = []
    for i in range(1,7):
        h.append(f"h{i}")
    code = "code"
    blockquote = "blockquote"
    ul = "ul"
    ol = "ol"

def block_to_type(block):
    corrected_block = block.strip()
    block_lines = block.splitlines()
    if corrected_block[0] == "#":
        headingno = len(re.findall(r'#',corrected_block[:6])) - 1
        return ValidBlocks.h[headingno]
    elif corrected_block[0:3] == "```" and corrected_block[-4:-1] == "```":
        return ValidBlocks.code
    elif corrected_block[0] == ">":
        for line in block_lines:
            if not line.startswith(">"):
                return ValidBlocks.p
        return ValidBlocks.blockquote
    elif corrected_block[0:2] == "* " or corrected_block[0:2] == "- ":
        for line in block_lines:
            if not (line.startswith("* ") or line.startswith("- ")):
                return ValidBlocks.p
        return ValidBlocks.ul
    elif corrected_block[0].isnumeric() and corrected_block[1:3] == '. ':
        for line in block_lines:
            if not (line[0].isnumeric() and line[1:3] == '. '):
                return ValidBlocks.p
        return ValidBlocks.ol
    else:
        return ValidBlocks.p

def block_to_html(block, block_type):
    raw_content = text_to_textnodes(block.lstrip("#> "))
    parsed_content = []
    if block_type == ValidBlocks.ul or block_type == ValidBlocks.ol:
        parsed_content = li_to_html(block, block_type)
    else:
        for node in raw_content:
            parsed_content.append(text_node_to_html_node(node))
    return ParentNode(block_type,parsed_content)

def li_to_html(block, block_type):
    items = block.splitlines()
    children = []
    if block_type == ValidBlocks.ul: i = 2
    elif block_type == ValidBlocks.ol: i = 3
    for item in items:
        text = item[i:]
        content = block_to_html(text, "li")
        children.append(content)
    return children

def md_to_html(txt):
    blocks = md_to_blocks(txt)
    html_blocks = []
    for block in blocks:
        block_type = block_to_type(block)
        html_blocks.append(block_to_html(block, block_type))
    return ParentNode('div',html_blocks)

def extract_title(txt):
    page = md_to_html(txt)
    body = page.children[0]
    if body.tag != ValidBlocks.h[0]:
        raise SyntaxError("Title missing!")
    return body.children[0].value
