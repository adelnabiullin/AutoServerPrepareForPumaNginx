from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings
from helpers import upload_file_and_move_it

def add_postgres_repo():
    sudo("echo 'deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main' >> /etc/apt/sources.list.d/pgdg.list")

def install_postgresql():
    pr = {
        'Do you want to continue? [Y/n] ': 'Y'
    }

    with settings(prompts=pr):
        sudo('wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -')
        sudo('apt-get update')
        sudo('sudo apt-get install postgresql-9.4 postgresql-server-dev-9.4')

def set_new_user_for_postgres():
    sudo('sudo -u postgres psql -c "create user deployer with password \'%s\';"' % project_settings.postgresql_settings['pass_for_deployer'])
    sudo('sudo -u postgres psql -c "alter role deployer superuser createrole createdb replication;"')
    sudo('sudo -u postgres psql -c "create user dev with password \'%s\';"' % project_settings.postgresql_settings['pass_for_dev'])
    sudo('sudo -u postgres psql -c "alter role dev superuser createrole createdb replication;"')

def upload_postgresql_conf():
    upload_file_and_move_it('postgresql.conf',
                            '/etc/postgresql/9.4/main/postgresql.conf',
                            True,
                            True,
                            'postgres')
    # file_path = '/tmp/postgresql.conf'
    # sudo('rm -f /etc/postgresql/9.4/main/postgresql.conf')
    # put(project_settings.PROJECT_ROOT + '/config_folder/postgresql.conf', file_path)
    # sudo('cp -p %s /etc/postgresql/9.4/main/postgresql.conf' % file_path)
    # sudo('chown postgres /etc/postgresql/9.4/main/postgresql.conf')
    # run('rm %s' % file_path)

def upload_pg_hba_conf():
    upload_file_and_move_it('pg_hba.conf',
                            '/etc/postgresql/9.4/main/pg_hba.conf',
                            True,
                            True,
                            'postgres')
    # file_path = '/tmp/pg_hba.conf'
    # sudo('rm -f /etc/postgresql/9.4/main/pg_hba.conf')
    # put(project_settings.PROJECT_ROOT + '/config_folder/pg_hba.conf', file_path)
    # sudo('cp -p %s /etc/postgresql/9.4/main/pg_hba.conf' % file_path)
    # sudo('chown postgres /etc/postgresql/9.4/main/pg_hba.conf')
    # run('rm %s' % file_path)

def enable_remote_access_to_postgres():
    upload_postgresql_conf()
    upload_pg_hba_conf()
    # sudo("echo \"listen_addresses='*'\" >> /etc/postgresql/9.4/main/postgresql.conf")
    # allow_string = 'host all deployer  0.0.0.0/00 md5'
    # sudo("echo ''%s' >> /etc/postgresql/9.4/main/pg_hba.conf" % allow_string)

def restart_postgres():
    sudo('service postgresql restart')

def prepare_postgres_to_deploy():
    add_postgres_repo()
    install_postgresql()
    set_new_user_for_postgres()
    enable_remote_access_to_postgres()
    restart_postgres()
