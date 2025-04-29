from litestar.exceptions import NotFoundException


class UserNotFoundError(NotFoundException):
    """user not found."""
    def __init__(self, detail: str = "user not found"):
        self.status_code = 404
        self.detail = detail
        super().__init__(self.detail)



