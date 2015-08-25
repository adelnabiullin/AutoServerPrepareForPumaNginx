from fabric.api import local, lcd, settings, run, sudo, env, put, cd
import settings as project_settings

def set_swap_thing():
    sudo('dd if=/dev/zero of=/swapfile bs=1024 count=512k')
    sudo('mkswap /swapfile')
    sudo('swapon /swapfile')

def add_string_to_file_with_echo():
    run_with = 'sh -c "echo \'%s\' >> /etc/fstab"'
    echo_string = '/swapfile       none    swap    sw      0       0'
    sudo(run_with % echo_string)

    run('echo 0 > /proc/sys/vm/swappiness')

def set_chown():
    run('echo 0 > /proc/sys/vm/swappiness')
    sudo('chown root:root /swapfile')
    sudo('chmod 0600 /swapfile')

def install_swap():
    set_swap_thing()
    add_string_to_file_with_echo()
    set_chown()
