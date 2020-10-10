import sys
from typing import Any, ByteString, Sequence, Tuple, Type, TypeVar, Union

from .descriptor import Descriptor, DescriptorBase, FieldDescriptor

class Error(Exception): ...
class DecodeError(Error): ...
class EncodeError(Error): ...

class _ExtensionDict:
    def __getitem__(self, extension_handle: DescriptorBase) -> Any: ...
    def __setitem__(self, extension_handle: DescriptorBase, value: Any) -> None: ...

_M = TypeVar("_M", bound=Message)  # message type (of self)

if sys.version_info < (3,):
    _Serialized = Union[bytes, buffer, unicode]
else:
    _Serialized = ByteString

class Message:
    DESCRIPTOR: Descriptor
    def __deepcopy__(self, memo=...): ...
    def __eq__(self, other_msg): ...
    def __ne__(self, other_msg): ...
    def MergeFrom(self: _M, other_msg: _M) -> None: ...
    def CopyFrom(self: _M, other_msg: _M) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: _Serialized) -> int: ...
    def ParseFromString(self, serialized: _Serialized) -> int: ...
    def SerializeToString(self, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> Sequence[Tuple[FieldDescriptor, Any]]: ...
    def HasExtension(self, extension_handle): ...
    def ClearExtension(self, extension_handle): ...
    def ByteSize(self) -> int: ...
    @classmethod
    def FromString(cls: Type[_M], s: _Serialized) -> _M: ...
    @property
    def Extensions(self) -> _ExtensionDict: ...
    # Intentionally left out typing on these three methods, because they are
    # stringly typed and it is not useful to call them on a Message directly.
    # We prefer more specific typing on individual subclasses of Message
    # See https://github.com/dropbox/mypy-protobuf/issues/62 for details
    def HasField(self, field_name: Any) -> bool: ...
    def ClearField(self, field_name: Any) -> None: ...
    def WhichOneof(self, oneof_group: Any) -> Any: ...
    # TODO: check kwargs
    def __init__(self, **kwargs) -> None: ...
