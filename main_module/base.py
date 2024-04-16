from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from dataclasses import dataclass

class Base(DeclarativeBase, MappedAsDataclass):
    pass