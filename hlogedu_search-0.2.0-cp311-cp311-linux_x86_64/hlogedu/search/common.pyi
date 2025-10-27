from dataclasses import dataclass

@dataclass(frozen=True)
class ClassParameter:
    name: str
    type: type
    default: str | None = ...
    help: str = ...
