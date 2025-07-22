#!/usr/bin/env python3

# Copyright 2024 Dylan Stephano-Shachter
# See CODE_LICENSE file for licensing details.

import os
import pathlib
import shutil
import tomllib

import jinja2

def main():
    de_posts = []
    de_posts_dir = pathlib.Path('posts/dylaneats')
    for post_file in de_posts_dir.iterdir():
        with post_file.open('rb') as f:
            post = tomllib.load(f)
        de_posts.append(post)
    de_posts.sort(key=lambda x: x['name'])

    ath_posts = []
    ath_posts_dir = pathlib.Path('posts/athens')
    for post_file in ath_posts_dir.iterdir():
        with post_file.open('rb') as f:
            post = tomllib.load(f)
        ath_posts.append(post)
    ath_posts.sort(key=lambda x: x['name'])

    greece_coffee_posts = []
    greece_coffee_posts_dir = pathlib.Path('posts/greece_coffee')
    for post_file in greece_coffee_posts_dir.iterdir():
        with post_file.open('rb') as f:
            post = tomllib.load(f)
        greece_coffee_posts.append(post)
    greece_coffee_posts.sort(key=lambda x: x['name'])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), autoescape=False)
    index = env.get_template('index.html')
    with pathlib.Path('index.html').open('w') as f:
        f.write(index.render(posts=de_posts))
    athens = env.get_template('athens.html')
    with pathlib.Path('athens.html').open('w') as f:
        f. write(athens.render(posts=ath_posts))
    greece_coffee = env.get_template('greece_coffee.html')
    with pathlib.Path('greece_coffee.html').open('w') as f:
        f. write(greece_coffee.render(posts=greece_coffee_posts))


if __name__ == '__main__':
    main()
