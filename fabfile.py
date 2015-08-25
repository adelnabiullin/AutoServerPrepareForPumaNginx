from fabric.api import local, lcd, settings, run, sudo, env, put, cd

# Deploy stages
import settings as project_settings
from deploy_stages.user_setup import *
from deploy_stages.rbenv_installation import *
from deploy_stages.ruby_installation import *
from deploy_stages.postgres_installation import *
from deploy_stages.nginx_installation import *
from deploy_stages.redis_installation import *
from deploy_stages.sidekiq_installation import prepare_sidekiq_for_deploy
from deploy_stages.puma_installation import prepare_puma_for_deploy
from deploy_stages.swap_installation import install_swap
from deploy_stages.additional_lib_installation import install_all_dependies
env.shell = "/bin/bash -l -i -c"

def root_user():
    env.hosts = [project_settings.host]
    env.password = project_settings.root_init_password

def deployer_user():
    replace_name = project_settings.host.split('@')[0]
    env.hosts = [project_settings.host.replace(replace_name, 'deployer')]
    env.user = 'deployer'
    env.password = project_settings.deployer_info['pass']

def test_app():
    with settings(warn_only=True):
        with lcd(project_settings.app_local_dir):
            result = local('rake test:controllers', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def run_as_root_user():
    change_root_user_pass()
    add_user_to_server()
    deny_root_user()
    push_key()
    reload_ssh()
    install_swap()

# Run this command as deployer
def run_as_deployer():
    full_install_rbenv()
    prepare_ruby_for_deploy()
    prepare_postgres_to_deploy()
    prepare_nginx_for_deploy()
    prepare_redis_for_deploy()
    prepare_sidekiq_for_deploy()
    prepare_puma_for_deploy()
    install_all_dependies()
