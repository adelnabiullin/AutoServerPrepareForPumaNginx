from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def upload_upstart_script():
    upload_file_and_move_it('sidekiq.conf', '/etc/init/sidekiq.conf')

def prepare_sidekiq_for_deploy():
    upload_upstart_script()
