from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def build(ctx):
    ctx.run("python3 src/build.py")

@task
def test(ctx):
    ctx.run("pytest src")