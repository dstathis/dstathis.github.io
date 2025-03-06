#!/usr/bin/env python3

# Copyright 2024 Dylan Stephano-Shachter
# See CODE_LICENSE file for licensing details.

import os
import pathlib
import shutil
import tomllib

import jinja2

def main():
    posts = []
    posts_dir = pathlib.Path('posts/dylaneats')
    for post_file in posts_dir.iterdir():
        with post_file.open('rb') as f:
            post = tomllib.load(f)
        posts.append(post)
    posts.sort(key=lambda x: x['name'])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), autoescape=False)
    index = env.get_template('index.html')
    with pathlib.Path('index.html').open('w') as f:
        f.write(index.render(posts=posts))


if __name__ == '__main__':
    main()
