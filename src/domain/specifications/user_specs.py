from abc import ABC, abstractmethod

from pydantic import UUID4
from infrastructure.db.models import User as UserModel


class UserSpecification(ABC):
    @abstractmethod
    def to_query(self, base_query):
        pass


class UserByIdSpecification(UserSpecification):
    def __init__(self, user_id: UUID4):
        self.user_id = user_id

    def to_query(self, base_query):
        return base_query.where(UserModel.id == self.user_id)


class UserByNameSpecification(UserSpecification):
    def __init__(self, username: str):
        self.username = username

    def to_query(self, base_query):
        return base_query.where(UserModel.username == self.username.lower())
