from fabric.api import env, run, cd
import os


# Remote server configuration
env.hosts = ['losinhos.com']
env.user = 'root'
env.password = os.environ['HOSTP']
env.app_dir = '/var/www/blog/'


def publish():
    with cd(env.app_dir):
        run('git fetch')
        run('git reset origin/master')
        run('git checkout .')
