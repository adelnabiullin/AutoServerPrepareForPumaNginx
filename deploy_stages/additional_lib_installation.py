from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def install_rubinus_dependies():
    sudo('sudo apt-get install -y bison \
zlib1g-dev libssl-dev libreadline-dev libncurses5-dev')
    sudo('apt-get install -y ruby-dev llvm')

def install_all_dependies():
    install_rubinus_dependies()
