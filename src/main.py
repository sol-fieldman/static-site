#!/usr/bin/env python3

import os
import shutil

def copy_files(path='static',out='public'):
    if not os.path.exists(path):
        raise Exception(f"path {path} not found!")
    ls = os.listdir(path)
    if os.path.exists(out):
        if os.listdir(out) == ls:
            shutil.rmtree(out)
            print(f"deleting path: {out}")
            os.mkdir(out)
    else:
        os.mkdir(out)
        print(f"creating path: {out}")
    for item in ls:
        newpath = os.path.join(path,item)
        newout = os.path.join(out,item)
        if not os.path.isfile(newpath):
            print(f"creating path: {newout}")
            os.mkdir(newout)
            copy_files(newpath,newout)
        else:
            print(f"copying file: {newpath} to {newout}")
            shutil.copy(newpath,newout)



def main():
    copy_files()

main()
