from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings
from helpers import upload_file_and_move_it

def upload_sidekiq_manager_script():
    upload_file_and_move_it('sidekiq-manager.conf', '/etc/init/sidekiq-manager.conf ')

def upload_sidekiq_script():
    upload_file_and_move_it('sidekiq.conf', '/etc/init/sidekiq.conf')

def create_sidekiq_projects_manager():
    sudo('touch /etc/sidekiq.conf')

def prepare_sidekiq_for_deploy():
    upload_sidekiq_manager_script()
    upload_sidekiq_script()
    create_sidekiq_projects_manager()
