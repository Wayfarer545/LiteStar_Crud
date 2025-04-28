from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship
import datetime as dt
from typing import Optional, List
from pydantic import UUID4
import uuid

from src.infrastructure.db.schemas import UserRole, CameraType, Protocols


def get_id() -> UUID4:
    return uuid.uuid4()

def get_time() -> dt:
    return dt.datetime.now(dt.UTC)


class User(SQLModel, table=True):
    id: UUID4 = Field(default_factory=get_id, primary_key=True, index=True)
    username: str = Field(index=True, unique=True)
    password_hash: str
    role: UserRole
    created_at: dt.datetime = Field(default_factory=get_time)
    updated_at: Optional[dt.datetime] = Field(default=None)
    is_active: bool = Field(default=True)

    presets: List["UserPresets"] = Relationship(back_populates="parent_user", cascade_delete=True)

class CameraTemplateLink(SQLModel, table=True):
    cam_id: UUID4 = Field(foreign_key="camera.id", primary_key=True)
    template_id: UUID4 = Field(foreign_key="template.id", primary_key=True)

class Camera(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("ip", "port", "type", name="unique_ip_port_type"),
    )

    id: UUID4 = Field(default_factory=get_id, primary_key=True)
    name: str = Field(unique=True)
    ip: str = Field(index=True)
    port: int = Field(default=80)
    username: str = Field()
    password: str = Field()
    type: CameraType = Field(default=CameraType.NETIP)
    enabled: bool = Field(default=True)
    archive_enabled: bool = Field(default=True)
    channel: int = Field(default=0)
    url: Optional[str] = Field(default=None)
    group_id: Optional[UUID4] = Field(default=None, foreign_key="group.id", index=True)

    templates: List["Template"] = Relationship(
        back_populates="cameras", link_model=CameraTemplateLink
    )
    group: Optional["Group"] = Relationship(back_populates="cameras")
    presets: List["UserPresets"] = Relationship(back_populates="parent_camera", cascade_delete=True)
    logs: List["CameraLog"] = Relationship(back_populates="camera", cascade_delete=True)

class Template(SQLModel, table=True):
    id: UUID4 = Field(default_factory=get_id, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str] = Field(default=None)
    grid_type: int  # Можно заменить на Enum, если есть конкретные значения

    cameras: List["Camera"] = Relationship(
        back_populates="templates", link_model=CameraTemplateLink
    )

class Group(SQLModel, table=True):
    id: UUID4 = Field(default_factory=get_id, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str] = Field(default=None)
    is_stream_enabled: bool = Field(default=True)
    is_archive_enabled: bool = Field(default=True)

    cameras: List["Camera"] = Relationship(back_populates="group", cascade_delete=True)

class UserPresets(SQLModel, table=True):
    user_id: UUID4 = Field(foreign_key="user.id", primary_key=True)
    camera_id: UUID4 = Field(foreign_key="camera.id", primary_key=True)
    stream_protocol_id: Protocols = Field(default=Protocols.HLS)

    parent_camera: "Camera" = Relationship(back_populates="presets")
    parent_user: "User" = Relationship(back_populates="presets")

class CameraLog(SQLModel, table=True):
    id: int = Field(primary_key=True)
    text: Optional[str] = Field(default=None)
    errstring: Optional[str] = Field(default=None)
    errno: int = Field(default=-1)
    state: int = Field(default=-1)
    crtime: dt.datetime = Field(default_factory=get_time)
    camera_id: UUID4 = Field(foreign_key="camera.id", index=True)

    camera: "Camera" = Relationship(back_populates="logs")

class Module(SQLModel, table=True):
    id: UUID4 = Field(default_factory=get_id, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str] = Field(default=None)
    url: str = Field(unique=True)
    token: Optional[str] = Field(default=None)
    module_type: str = Field(default="cvflow")  # "cvflow" или "oncam"

class AppSetting(SQLModel, table=True):
    key: str = Field(primary_key=True, unique=True)
    value: Optional[str] = Field(default=None)