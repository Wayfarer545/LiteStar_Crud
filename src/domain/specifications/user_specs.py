from abc import ABC, abstractmethod

from infrastructure.db.models import User as UserModel


class UserSpecification(ABC):
    @abstractmethod
    def to_query(self, base_query):
        pass


class UserByIdSpecification(UserSpecification):
    def __init__(self, user_id: int):
        self.user_id = user_id

    def to_query(self, base_query):
        return base_query.where(UserModel.id == self.user_id)


class UserByNameSpecification(UserSpecification):
    def __init__(self, name: str):
        self.name = name

    def to_query(self, base_query):
        return base_query.where(UserModel.name == self.name.lower())
