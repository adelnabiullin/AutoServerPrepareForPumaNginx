from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def change_root_user_pass():
    pr = {
        'Enter new UNIX password: ': project_settings.root_password,
        'Retype new UNIX password: ': project_settings.root_password
    }

    with settings(prompts=pr):
        sudo('passwd')

def add_user_to_server():
    pr = {
        'Enter new UNIX password: ': project_settings.deployer_info['pass'],
        'Retype new UNIX password: ': project_settings.deployer_info['pass'],
        'Full Name []: ': project_settings.deployer_info['full_name'],
        'Room Number []: ': project_settings.deployer_info['room_number'],
        'Work Phone []: ': project_settings.deployer_info['work_phone'],
        'Home Phone []: ': project_settings.deployer_info['home_phone'],
        'Other []: ': project_settings.deployer_info['other'],
        'Is the information correct? [Y/n] ': 'Y'
    }
    with settings(prompts=pr):
        sudo('adduser deployer')
    sudo("echo 'deployer ALL=(ALL:ALL) ALL' >> /etc/sudoers")
    allow_nopass = "deployer ALL=NOPASSWD: ALL"
    sudo("echo '%s' >> /etc/sudoers" % allow_nopass)

def deny_root_user():
    sudo("echo 'PermitRootLogin no' >> /etc/ssh/sshd_config")
    sudo("echo 'UseDNS no' >> /etc/ssh/sshd_config")
    sudo("echo 'AllowUsers deployer' >> /etc/ssh/sshd_config")

def reload_ssh():
    sudo ('reload ssh')

def push_key():
    keyfile = '/tmp/deployer.pub'
    run('mkdir -p /home/deployer/.ssh')
    put('~/.ssh/id_rsa.pub', keyfile)
    run('cat %s >> /home/deployer/.ssh/authorized_keys' % keyfile)
    run('rm %s' % keyfile)

def set_permissions_for_ssh():
    sudo("chown -R deployer:deployer /home/deployer/.ssh")
