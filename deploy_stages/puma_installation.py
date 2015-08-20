from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def upload_puma_manager_script():
    upload_file_and_move_it('puma-manager.conf', '/etc/init/puma-manager.conf ')

def upload_puma_script():
    upload_file_and_move_it('puma.conf', '/etc/init/puma.conf')

def create_puma_projects_manager():
    sudo('touch /etc/puma.conf')

def prepare_puma_for_deploy():
    upload_puma_manager_script()
    upload_puma_script()
    create_puma_projects_manager()
