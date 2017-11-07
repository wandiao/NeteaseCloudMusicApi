from fabric.api import (
  task,
  local,
  env,
  roles,
  cd,
  run,
)
env.roledefs = {
  'prod': ['root@39.108.123.68']
}

@task
@roles('prod')
def deploy(reset=False):
  with cd('~/node-demo/NeteaseCloudMusicApi/'):
    if reset:
        run('git reset --hard HEAD~1')
    else:
        run('git checkout -- .')
    run('git checkout dev')
    run('git pull --rebase origin dev')
    run('pm2 restart all')