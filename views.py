from aiohttp import web
from celery.result import AsyncResult

from tasks import fib, app


async def fib_view(request):
    value = int(request.match_info.get('value', 5))
    task = fib.delay(value)

    return web.json_response(data={'id': str(task.id)})


async def task_status_view(request):
    task_id = request.match_info.get('id')
    task = AsyncResult(task_id, app=app)
    if task.ready():
        return web.json_response(data={'status': 'finished', 'result': task.get()})
    else:
        return web.json_response(data={'status': 'processing'})


