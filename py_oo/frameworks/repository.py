from applications.protocols.irepository import IRepository


class Repository(IRepository):

    def save(self, text: str) -> None:
        print("impl repository" + text)
