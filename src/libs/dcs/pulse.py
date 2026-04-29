from collections.abc import Callable
from threading import Timer
# from datetime import datetime, timedelta
from typing import Any, Iterable, Mapping
# from requests import get, post
# import json
import winsound


class DistributedClient:

    def __init__(self, name='unknown-app', content=None, timeout=10, check=None) -> None:
        self.name = name
        self._content = content
        self.timeout = timeout
        self.health_check = check
        self.thread = DistributedThread(self.timeout, self.pulse)
        self.thread.start()

    def pulse(self):
        try:
            if self.health_check is not None and self.health_check():
                winsound.MessageBeep(type=winsound.MB_OK)
            else:
                winsound.MessageBeep(type=winsound.MB_ICONQUESTION)
            self.name = self.name
            # response = post(
            #     url=f'{self.argus_url}/add',
            #     headers={'Content-Type': 'application/json; charset=UTF-8'},
            #     data=json.dumps({'appname':self.app_name, 'host':f'{self.http_host}', 'port':f'{self.http_port}'}))
            # response.raise_for_status()
        except Exception as e:
            # Пишем событие о недоступнсоти
            print(f'<{str(e)}>'.replace('\n', '  '))

    def cancel(self):
        self.thread.cancel()


class DistributedThread(Timer):

    def __init__(
            self, interval: float,
            function: Callable[..., object],
            args: Iterable[Any] | None = None,
            kwargs: Mapping[str, Any] | None = None) -> None:
        super().__init__(interval, function, args, kwargs)

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
