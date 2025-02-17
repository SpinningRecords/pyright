# This sample tests the case where a method is overriding an overloaded method.

from typing import Any, Generic, Literal, TypeVar, overload

_T = TypeVar("_T")


class Parent1(Generic[_T]):
    @overload
    def m1(self, x: Literal[True]) -> int:
        ...

    @overload
    def m1(self, x: Literal[False]) -> float:
        ...

    @overload
    def m1(self, x: _T) -> _T:
        ...

    def m1(self, x: bool | _T) -> int | float | _T:
        return x


class Child1_1(Parent1[str]):
    @overload
    def m1(self, x: bool) -> int:
        ...

    @overload
    def m1(self, x: str) -> str:
        ...

    def m1(self, x: bool | str) -> int | str:
        return x


class Child1_2(Parent1[str]):
    def m1(self, x: Any) -> Any:
        return x


class Child1_3(Parent1[str]):
    @overload
    def m1(self, x: bool) -> int:
        ...

    @overload
    def m1(self, x: str) -> str:
        ...

    def m1(self, x: bool | str) -> int | float | str:
        return x


class Child1_4(Parent1[str]):
    @overload
    def m1(self, x: str) -> str:
        ...

    @overload
    def m1(self, x: bool) -> int:
        ...

    # This should generate an error because the overloads are
    # in the wrong order.
    def m1(self, x: bool | str) -> int | float | str:
        return x


class Child1_5(Parent1[str]):
    @overload
    def m1(self, x: Literal[True]) -> int:
        ...

    @overload
    def m1(self, x: Literal[False]) -> float:
        ...

    @overload
    def m1(self, x: bytes) -> bytes:
        ...

    # This should generate an error because the overloads are
    # in the wrong order.
    def m1(self, x: bool | bytes) -> int | float | bytes:
        return x


class Child1_6(Parent1[bytes]):
    @overload
    def m1(self, x: Literal[True]) -> int:
        ...

    @overload
    def m1(self, x: Literal[False]) -> float:
        ...

    @overload
    def m1(self, x: bytes) -> bytes:
        ...

    def m1(self, x: bool | bytes) -> int | float | bytes:
        return x
