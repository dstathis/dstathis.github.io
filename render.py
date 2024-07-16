#!/usr/bin/env python3

# Copyright 2024 Dylan Stephano-Shachter
# See CODE_LICENSE file for licensing details.

import pathlib
import shutil
import tomllib

import jinja2

def main():
    posts = []
    posts_dir = pathlib.Path('posts')
    for post_file in posts_dir.iterdir():
        with post_file.open('rb') as f:
            post = tomllib.load(f)
        posts.append(post)

    web_dir = pathlib.Path('www')
    web_dir.mkdir(exist_ok=True)
    os.symlink('../images', web_dir / 'images')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), autoescape=False)
    index = env.get_template('index.html')
    with (web_dir / 'index.html').open('w') as f:
        f.write(index.render(posts=posts))
    shutil.copy("templates/styles.css", web_dir / "styles.css")


if __name__ == '__main__':
    main()
