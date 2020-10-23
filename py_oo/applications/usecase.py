from bussiness.iusecase import IUseCase
from applications.protocols.irepository import IRepository


class UseCase(IUseCase):
    _repository: IRepository

    def __init__(self, repository: IRepository):
        self._repository = repository

    def printing(self, text: str) -> None:
        self._repository.save(text)
