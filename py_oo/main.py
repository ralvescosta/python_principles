from applications.usecase import UseCase
from frameworks.repository import Repository

repo = Repository()
case = UseCase(repo)

case.printing("Printando do repository")