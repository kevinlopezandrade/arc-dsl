from typing import (
    Any,
    Callable,
    Container,
    FrozenSet,
    Iterable,
    List,
    Protocol,
    Sized,
    Tuple,
    TypeVar,
    Union,
)

Boolean = bool
Integer = int
Coordinate = Tuple[Integer, Integer]
Numerical = Union[Integer, Coordinate]
IntegerSet = FrozenSet[Integer]
Grid = Tuple[Tuple[Integer]]
Cell = Tuple[Integer, Coordinate]
Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Coordinates = FrozenSet[Coordinate]
IndicesSet = FrozenSet[Coordinates]
Patch = Union[Object, Coordinates]
Element = Union[Object, Grid]
Piece = Union[Grid, Patch]
TupleTuple = Tuple[Tuple]
ContainerContainer = Container[Container]

_T = TypeVar("_T")


# Custom Protocol
class IterableContainer(Iterable[_T], Container[_T], Sized, Protocol[_T]):
    # We define init here to make it compatible with the current containers.
    def __init__(self, __iterable: Iterable[_T]) -> None:
        ...
