from fabric.api import env, run, cd, settings
import os


# Remote server configuration
env.hosts = ['losinhos.com']
env.user = 'root'
env.password = os.environ['HOSTP']
env.www_dir = '/var/www/'
env.app_dir = '/var/www/blog/'


def install_pelican():
    run('pip install pelican markdown')


def gen_output():
    with cd(env.app_dir):
        run('pelican content')


def clone():
    with settings(warn_only=True):
        with cd(env.www_dir):
            run('git clone https://github.com/csarcom/blog.git')


def publish():
    with cd(env.app_dir):
        run('git fetch')
        run('git reset origin/master')
        run('git checkout .')


def deploy():
    clone()
    install_pelican()
    publish()
    gen_output()
