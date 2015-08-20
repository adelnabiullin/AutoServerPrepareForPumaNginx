from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def sidekiq_installation():
    run('gem install sidekiq')

def upload_upstart_script():
    upload_file_and_move_it('sidekiq.conf', '/etc/init/sidekiq.conf')

def upload_yml_configuration():
    run('mkdir -p ~/sidekiq_config')
    upload_file_and_move_it('sidekiq_conf.yml', '~/sidekiq_config/sidekiq_conf.yml')

def prepare_sidekiq_for_deploy():
    sidekiq_installation()
    upload_upstart_script()
    upload_yml_configuration()
