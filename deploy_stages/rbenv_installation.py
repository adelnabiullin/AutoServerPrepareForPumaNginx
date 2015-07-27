from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def prepare_to_install_rbenv():
    pr = {
        'Do you want to continue? [Y/n] ': 'Y'
    }

    sudo('apt-get update')

    with settings(prompts=pr):
        sudo('apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev')

def install_rbenv():
    run('git clone git://github.com/sstephenson/rbenv.git .rbenv')
    run("echo 'export PATH=\"$HOME/.rbenv/bin:$PATH\"' >> ~/.bashrc")
    run("echo 'eval \"$(rbenv init -)\"' >> ~/.bashrc")

def install_rbenv_build():
    run(u'git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build')
    run(u"echo 'export PATH=\"$HOME/.rbenv/plugins/ruby-build/bin:$PATH\"' >> ~/.bashrc")

def install_rbenv_gemset():
    run('git clone git://github.com/jf/rbenv-gemset.git $HOME/.rbenv/plugins/rbenv-gemset')

def install_rbenv_vars():
    with cd('~/.rbenv/plugins'):
        run('git clone https://github.com/sstephenson/rbenv-vars.git')

def full_install_rbenv():
    prepare_to_install_rbenv()
    install_rbenv()
    install_rbenv_build()
    install_rbenv_gemset()
    install_rbenv_vars()
