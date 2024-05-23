#!/usr/bin/env python3

import re
from md_parser import *
from htmlnode import *

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
    if corrected_block[0] == "#":
        headingno = len(re.findall(r'#',corrected_block[:6])) - 1
        return ValidBlocks.h[headingno]
    elif corrected_block[0:3] == "```" and corrected_block[-4:-1] == "```":
        return ValidBlocks.code
    elif corrected_block[0:2] == "* " or corrected_block[0:2] == "- ":
        return ValidBlocks.ul
    elif corrected_block[0].isnumeric() and corrected_block[1:3] == '. ':
        return ValidBlocks.ol
    else:
        return ValidBlocks.p
