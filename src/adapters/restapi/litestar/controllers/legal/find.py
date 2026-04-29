from litestar import Controller, get
from adapters import ExtLegalEntityInfo
import uuid
from .dto import *
from domain import *

class FindController(Controller):

    path = '/find'

    @get()
    # async def input(self, input: LegalEntityModel) -> str:
    async def find(self, tin: str | None = None, psrn: str | None = None) -> LegalEntityDTO:
        #   Читаем данные из бд (если есть)
        if tin is not None:
            le = LegalEntity()
            le.find_by_tin(tin)
        elif psrn is not None:
            le = RusLegalEntity()
            le.find_by_psrn(psrn)
        else:
            pass #  Закончить с ошибкой
        #   Если данных нет или они могли устареть
        if le.id is None:
        #       загружаем данные из внешних источников
            data = ExtLegalEntityInfo(tin or psrn)
        #   Если загруженные данные более свежие по дате внешнего источника
        #       обновляем данные в объекта в БД
        if tin:
            res = str(tin)
        elif psrn:
            res = str(psrn)
        else:
            res = None
        return LegalEntityDTO(uuid.uuid4(), data.tin, data.psrn, data.shortname, data.fullname)
