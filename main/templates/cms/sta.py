# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import re
import sys


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.html':
                L.append(os.path.join(root, file))
    return L


if __name__ == "__main__":
    # print(file_name(r"C:\Users\Python\Desktop\e1hjid\admin"))
    cj = set()
    for f in file_name(os.getcwd()):
        with open(f, "r+", encoding="utf-8") as html:
            for row in html:
                l = re.findall("<(?:link|script|img).*", row)
                if l:
                    # print(f.split("\\")[-1], l[0])

                    url = re.search("(?:href|src)=\"([\\\./\-\w]*)\"", l[0])
                    if url:
                        # print(f.split("\\")[-1], url.group(1).fin)
                        cj.add((url.group(1), url.group(1).split(
                            "/")[-1], url.group(1).split(".")[-1]))

    # 拷贝引用文件
    # print([i[0] for i in cj])
    for p in ["css", "js", "png", "jpg"]:
        pt = os.getcwd() + "\\" + p
        if not os.path.exists(pt):
            os.mkdir(pt)

    for path in cj:
        print(path)
        try:
            with open(path[0], "rb+") as form:
                with open(os.getcwd() + "\\" + path[2] + "\\" + path[1], "wb+") as to:
                    while True:
                        data = form.readline()
                        if not data:
                            break
                        to.write(data)
        except FileNotFoundError:
            print("\n>>>>>>>>>>>   can not find ", path[0])
