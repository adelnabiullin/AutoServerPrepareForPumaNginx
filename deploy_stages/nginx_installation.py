from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def install_nginx():
    pr = {
        'Do you want to continue? [Y/n] ': 'Y'
    }
    with settings(prompts=pr):
        sudo('apt-get install nginx')

def remove_nginx_default_sites_config():
    sudo('rm /etc/nginx/sites-available/default')
    sudo('touch /etc/nginx/sites-available/default')

    sudo("chown root:root /etc/nginx/sites-available/default")

def prepare_nginx_for_deploy():
    install_nginx()
    remove_nginx_default_sites_config()
