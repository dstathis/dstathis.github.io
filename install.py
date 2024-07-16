#!/usr/bin/env python3

# Copyright 2024 Dylan Stephano-Shachter
# See CODE_LICENSE file for licensing details.

import os
import subprocess


def run(cmd):
    print(f'+ {cmd}')
    subprocess.run(cmd, shell=True)


def main():
    run('dnf install -y epel-release')
    run('dnf upgrade -y')
    run('dnf install -y nginx certbot python3-certbot-nginx')
    print('Writing config...')
    with open('nginx.conf') as f:
        conf = f.read()
    conf = conf.replace('{% repo_dir %}', os.getcwd())
    with open('/etc/nginx/nginx.conf', 'w') as f:
        f.write(conf)
    run('certbot certonly --nginx')
    run('systemctl restart nginx')


if __name__ == '__main__':
    main()
