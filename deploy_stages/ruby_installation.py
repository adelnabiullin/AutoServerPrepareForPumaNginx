from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def install_ruby_by_rbenv():
    run('rbenv install -v %s' % project_settings.ruby_version)
    run('rbenv global %s' % project_settings.ruby_version)
# Bunlder gem installation
def install_bundler():
    run('gem install bundler')

# Nodejs installation
def install_nodejs():
    pr = {
        'Press [ENTER] to continue or ctrl-c to cancel adding it': '',
        'Do you want to continue? [Y/n] ': 'Y'
    }

    with settings(prompts=pr):
        sudo('add-apt-repository ppa:chris-lea/node.js')
        sudo('apt-get update')
        sudo('apt-get install nodejs')

# Preparing Ruby enviroment for deploy
def prepare_ruby_for_deploy():
    install_ruby_by_rbenv()
    install_nodejs()
    install_bundler()
