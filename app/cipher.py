"""
At first, I created the cipher app with a single basic feature, which is a function that encodes a string based on the provided inputs.
However, I took into consideration the single responsibility principle and separated the Caesar and Substitution Cipher.
Doing so makes the application more abstract and flexible.

Also it's not a conventional practice in Python,
however I included an abstract interface class to be used by the cipher implementation classes.
"""

import string
from abc import ABC, abstractmethod
from typing import Dict, Union


class CipherInterface(ABC):
    """Cipher interface."""

    @abstractmethod
    def cipher(self, m: str) -> str:
        """Cipher word function"""


class CaesarCipher(CipherInterface):
    def __init__(self, shift: int):
        self.shift = shift

    # private / helper functions

    def __cipher_char(self, c: str) -> str:
        # Check if character is a special character
        if c not in string.ascii_letters:
            return c

        # Check if character to cipher is uppercase
        is_upper = c.isupper()

        # Get integer to subtract when converting
        # character int to map index
        subtractor = 65 if is_upper else 97

        # Get shifted index of character
        index = (ord(c) - subtractor + self.shift) % 26

        return string.ascii_letters[index + (26 if is_upper else 0)]

    # public functions

    def cipher(self, m: str) -> str:
        if not (-26 < self.shift < 26):
            raise ValueError("Shift value must be between -25 to +25")

        return "".join([self.__cipher_char(c) for c in m])


class SubstitutionCipher(CipherInterface):
    def __init__(self, character_map: Dict):
        self.character_map = character_map

    # public functions

    def cipher(self, m: str) -> str:
        return "".join([self.character_map.get(c, c) for c in m])


def cipher(m: str, n: Union[int, Dict]) -> str:
    """Main function for encoding and decoding string."""

    cipher_map: CipherInterface = {
        int: CaesarCipher,
        dict: SubstitutionCipher,
    }

    try:
        cipher_client = cipher_map[type(n)]
    except KeyError:
        raise ValueError("Input not supported")

    return cipher_client(n).cipher(m)
