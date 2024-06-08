# Copyright 2024 The RE2 Authors.  All Rights Reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

from enum import IntEnum


class Error(RuntimeError):
    ...


def CharLenToBytes(buffer: bytes, pos: int, len: int) -> int:
    ...

def BytesToCharLen(buffer: bytes, pos: int, endpos: int) -> int:
    ...


class RE2:
    class Anchor(IntEnum):
        UNANCHORED = ...
        ANCHOR_START = ...
        ANCHOR_BOTH = ...

    class Options:
        class Encoding(IntEnum):
            UTF8 = ...
            LATIN1 = ...

        def __init__(self) -> None:
            ...

        max_mem: int
        encoding: Encoding
        posix_syntax: bool
        longest_match: bool
        log_errors: bool
        literal: bool
        never_nl: bool
        dot_nl: bool
        never_capture: bool
        case_sensitive: bool
        perl_classes: bool
        word_boundary: bool
        one_line: bool

    def __init__(self, buffer: bytes, options: Options) -> None:
        ...

    def ok(self) -> bool: ...
    def error(self) -> bytes: ...
    def options(self) -> Options: ...
    def NumberOfCapturingGroups(self) -> int: ...
    def NamedCapturingGroups(self) -> list[tuple[bytes, int]]: ...
    def ProgramSize(self) -> int: ...
    def ReverseProgramSize(self) -> int: ...
    def ProgramFanout(self) -> list[int]: ...
    def ReverseProgramFanout(self) -> list[int]: ...
    def PossibleMatchRange(self, maxlen: int) -> tuple[bool, bytes, bytes]: ...

    def Match(
        self,
        anchor: Anchor,
        buffer: bytes,
        pos: int,
        endpos: int,
    ) -> list[tuple[int, int]]:
        ...

    @staticmethod
    def QuoteMeta(buffer: bytes) -> bytes: ...

    class Set:

        def __init__(self, anchor: RE2.Anchor, options: RE2.Options) -> None:
            ...

        def Add(self, buffer: bytes) -> int: ...
        def Compile(self) -> bool: ...
        def Match(self, buffer: bytes) -> list[int]: ...

    class Filter:

        def __init__(self) -> None:
            ...

        def Add(self, buffer: bytes, options: RE2.Options) -> int: ...
        def Compile(self) -> bool: ...
        def Match(self, buffer: bytes, potential: bool) -> list[int]: ...
        def GetRE2(self, index: int) -> RE2: ...
