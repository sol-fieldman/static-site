#!/usr/bin/env python3

class TextNode:
    def __init__ (self,text,text_type,url):
        self.text = text
        if not isinstance(self.text,str): raise TypeError("Must input node text.")

        self.text_type = text_type
        if not isinstance(self.text_type,str): raise TypeError("Invalid text type.")

        self.url = url
        if not isinstance(self.url,str): raise TypeError("Invalid url.")

    def __eq__ (self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__ (self):
        return f"Textnode({self.text}, {self.text_type}, {self.url})"
