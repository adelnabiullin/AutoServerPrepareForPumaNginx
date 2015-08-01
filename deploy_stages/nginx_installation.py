from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def install_nginx():
    pr = {
        'Do you want to continue? [Y/n] ': 'Y'
    }
    with settings(prompts=pr):
        sudo('apt-get install nginx')

def prepare_nginx_for_deploy():
    install_nginx()
