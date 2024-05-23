#!/usr/bin/env python3

import os
import shutil
from md_parser import *
from block_parser import *

def copy_files(path='static',out='public'):
    if not os.path.exists(path):
        raise Exception(f"path {path} not found!")
    ls = os.listdir(path)
    os.mkdir(out)
    print(f"creating path: {out}")
    for item in ls:
        newpath = os.path.join(path,item)
        newout = os.path.join(out,item)
        if not os.path.isfile(newpath):
            copy_files(newpath,newout)
        else:
            print(f"copying file: {newpath} to {newout}")
            shutil.copy(newpath,newout)

def generate_page(origin, template, dest):
    print(f"generating file: {dest} from {origin}")
    origin_file = open(origin)
    origin_content = origin_file.read()
    origin_file.close()
    parsed_origin_content = md_to_html(origin_content)
    title = extract_title(origin_content)

    template_file = open(template)
    template_content = template_file.read()
    template_file.close()

    parsed_content = template_content.replace('{{ Title }}',title)
    parsed_content = parsed_content.replace('{{ Content }}',parsed_origin_content.to_html())

    dest_path = os.path.dirname(dest)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    dest_file = open(dest, "w")
    dest_file.write(parsed_content)
    dest_file.close()

def generate_pages_r(origin, template, dest):
    ls = os.listdir(origin)
    for item in ls:
        entry = os.path.join(origin,item)
        exit_point = os.path.join(dest,item)
        if os.path.isfile(entry):
            filename = item.strip('md')
            filename += ('html')
            exit_point = os.path.join(dest,filename)
            generate_page(entry, template, exit_point)
        else:
            if len(os.listdir(entry)) == 0:
                continue
            generate_pages_r(entry,template,exit_point)

def main():
    print("deleting public dir...")
    if os.path.exists("public"):
        shutil.rmtree("public")
    generate_pages_r("content","template.html","static")
    copy_files()

main()
