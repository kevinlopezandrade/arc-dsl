from typing import (
    List,
    Union,
    Tuple,
    Any,
    Container,
    Callable,
    FrozenSet,
    Iterable
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
