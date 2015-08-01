from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings
from helpers import upload_file_and_move_it

def prepare_for_compile():
    pr = {
        'Do you want to continue? [Y/n] ': 'Y'
    }
    with settings(prompts=pr):
        sudo('apt-get install tcl8.5')

def get_redis():
    run('wget http://download.redis.io/redis-stable.tar.gz')
    run('tar xvzf redis-stable.tar.gz')

def make_install_redis():
    with cd('redis-stable'):
        sudo('make')
        sudo('make test')

def move_redis():
    with cd('redis-stable'):
        sudo('cp src/redis-server /usr/local/bin')
        sudo ('cp src/redis-cli /usr/local/bin')

def upload_config():
    sudo('mkdir /etc/redis/')
    upload_file_and_move_it('redis.conf', '/etc/redis/redis.conf')

def upload_upstart_script():
    upload_file_and_move_it('redis-server.conf', '/etc/init/redis-server.conf')

def make_dirs():
    sudo('mkdir -p /var/www/other')
    sudo('mkdir /var/www/log')

def prepare_redis_for_deploy():
    prepare_for_compile()
    get_redis()
    make_install_redis()
    move_redis()
    upload_config()
    upload_upstart_script()
    make_dirs()
