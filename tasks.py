from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/1', backend='redis://localhost:6379/2')


@app.task
def fib(value):
    if value < 2:
        return 1
    return fib(value - 1) + fib(value - 2)


