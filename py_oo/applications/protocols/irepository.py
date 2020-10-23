class IRepository:
    def save(self, text: str) -> None:
        raise NotImplementedError()
