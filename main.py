from aiohttp import web
from views import fib_view, task_status_view

app = web.Application()
app.add_routes([
    web.post('/api/fib/{value}', fib_view),
    web.get('/api/tasks/{id}', task_status_view),
])


if __name__ == '__main__':
    web.run_app(app)

