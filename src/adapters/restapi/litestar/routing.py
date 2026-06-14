from litestar import Litestar
from .controllers import controllers


class WebApp(Litestar):

    name = None

    def health_check(self):
        self.name = None
        return True


web_app = WebApp(route_handlers=[controllers])
