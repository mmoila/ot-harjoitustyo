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

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def autopep(ctx):
    ctx.run("autopep8 --in-place --recursive src")