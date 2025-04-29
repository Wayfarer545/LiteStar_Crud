

class SqlUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, user: UserEntity) -> UserEntity:
        db_user = UserModel(
            username=user.username,
            password_hash=user.password_hash,
            role=user.role
        )
        self.session.add(db_user)
        await self.session.flush()
        user.id = db_user.id
        return user

    async def get(self, spec: UserSpecification) -> UserEntity | None:
        statement = spec.to_query(select(UserModel))
        result = await self.session.exec(statement)
        if result:
            user = result.first()
            return UserEntity(**user.model_dump())

    async def get_list(self) -> list[UserEntity]:
        statement = select(UserModel)
        result = await self.session.exec(statement)
        return [UserEntity(**user.model_dump()) for user in result.all()]

    async def update(self, user: UserEntity) -> UserEntity:
        db_user = await self.session.get(UserModel, user.id)
        if db_user:
            db_user.username = user.username
            db_user.password_hash = user.password_hash
            await self.session.flush()
        return user

    async def delete(self, user_id: UUID4) -> None:
        db_user = await self.session.get(UserModel, user_id)
        if db_user:
            await self.session.delete(db_user)
            await self.session.flush()