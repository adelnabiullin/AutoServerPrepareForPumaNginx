from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def upload_file_and_move_it(name_of_file,
                            path_to_remote_file,
                            need_to_remove=False,
                            need_to_chmod=False,
                            chmoded_user='deployer'):
    file_path = '/tmp/%s' % name_of_file
    put(project_settings.PROJECT_ROOT + '/config_folder/%s' % name_of_file,
        file_path)
    if need_to_remove:
        sudo('rm -f %s' % path_to_remote_file)

    sudo('cp -p %s %s' % (file_path, path_to_remote_file))

    if need_to_chmod:
        sudo('chown %s %s' % (chmoded_user, path_to_remote_file))

    run('rm %s' % file_path)
