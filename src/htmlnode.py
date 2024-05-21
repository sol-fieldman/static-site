#!/usr/bin/env python3

class HTMLNode:
    def __init__ (self,tag=None, value=None, children=None, props=None):
        self.__tag = tag
        self.__value = value
        self.__children = children
        self.__props = props

    def to_html(self):
        raise Exception("Not yet implemented.")

    def props_to_html(self):
        out = str()
        for key in self.__props:
            out += f' {key}="{self.__props[key]}"'
        return out

    def __repr__(self):
        return f"HTMLnode({self.__tag}, {self.__value}, {self.__children}, {self.__props})"
