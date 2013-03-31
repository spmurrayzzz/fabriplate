import re
import json
import os
import functools
from fabric.api import (
    task,
    env,
    run,
    sudo,
    local,
)


def only(*roles):
    '''Decorator to restrict tasks to a set of roles'''
    def _dec(fn):
        @functools.wraps(fn)
        def _wrapper(*args, **kwargs):
            role_dict = get_role()
            for role in roles:
                if role == role_dict['role']:
                    return fn(*args, **kwargs)
        return _wrapper
    return _dec


def get_role():
    '''Get role dictionary from hosts.json'''
    for role in globals()['roles']:
        for ip in role['hosts']:
            if ip == globals()['env'].host_string:
                return role


# ----------
# TASKS
# ----------


@task
def default():
    role = get_role()
    for task in role['default_tasks']:
        globals()[task]()


@task
@only('spmurraydev')
def whoami():
    run('uname -a')


# ----------

roles = json.load(
    open('roles.json', 'r')
)
env.roledefs = {}
for host in roles:
    env.roledefs.update({
        host['role']: host['hosts']
    })
