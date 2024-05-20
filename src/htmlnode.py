#!/usr/bin/env python3

class HTMLNode:
    def __init__ (self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception("Not yet implemented.")

    def props_to_html(self):
        out = str()
        for key in self.props:
            out += f' {key}="{self.props[key]}"'
        return out

    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {props})"
