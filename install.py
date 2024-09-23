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
    run('rpm --import grafana-gpg.key')
    run('cp grafana.repo /etc/yum.repos.d/grafana.repo')
    run('dnf install -y nginx certbot python3-certbot-nginx python3.11 grafana-agent mimirtool')
    run('systemctl enable nginx')
    run('systemctl enable grafana-agent')
    print('Writing config...')
    with open('nginx.conf') as f:
        conf = f.read()
    conf = conf.replace('{% repo_dir %}', os.getcwd())
    with open('/etc/nginx/nginx.conf', 'w') as f:
        f.write(conf)
    run('certbot certonly -d dylaneats.com,www.dylaneats.com -n --nginx')
    run('systemctl restart nginx')
    with open('password.txt') as f:
        password = f.read()
    run('cp grafana-agent.yaml /etc/grafana-agent.yaml')
    run(f'sed -i "s/%%password%%/{password}/g" /etc/grafana-agent.yaml')
    run('systemctl restart grafana-agent')


if __name__ == '__main__':
    main()
