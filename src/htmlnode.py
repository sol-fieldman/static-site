#!/usr/bin/env python3

class HTMLNode:
    def __init__ (self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implimented")

    def props_to_html(self):
        out = str()
        if not isinstance(self.props,dict):
            return ''
        for key in self.props:
            out += f' {key}="{self.props[key]}"'
        return out

    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__ (self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        if not isinstance(self.value, str): raise ValueError("Must provide value.")

    def to_html(self):
        if self.tag == None:
            return self.value
        elif not isinstance(self.tag, str):
            raise ValueError("Tag must be a string.")

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__ (self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        if not isinstance(self.tag, str): raise ValueError("Must provide tag.")
        if (not isinstance(self.children, list) or len(self.children) == 0):
            raise ValueError("Invalid children list.")

    def to_html(self):
        out = [f"<{self.tag}>"]
        for heir in self.children:
            if isinstance(heir,HTMLNode): out+= heir.to_html()
            elif isinstance(heir,str): out += heir
            else: raise ValueError("Bastard Child!")
        out += [f"</{self.tag}>"]
        return ''.join(out)
