#!/usr/bin/env python3

import re

def extract_md_img(txt):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", txt)
    return images

def extract_md_link(txt):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", txt)
    return links
