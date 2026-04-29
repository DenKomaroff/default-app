from dataclasses import dataclass
from litestar.dto import DataclassDTO
from uuid import UUID
from datetime import date


@dataclass
class LegalEntityDTO:
    #   (BaseModel):
    id: UUID
    tin: str | None = None
    psrn: str | None = None
    name: str | None = None
    fullname: str | None = None
    created: date | None = None
    liquidated: date | None = None

# @dataclass
# class User:
#     name: str
#     email: str
#     age: int
#     id: UUID = field(default_factory=uuid4)


class  LegalEntityWriteDTO(DataclassDTO[LegalEntityDTO]): ...
    # config = DTOConfig(exclude={"id"})


class  LegalEntityReadDTO(DataclassDTO[LegalEntityDTO]): ...
