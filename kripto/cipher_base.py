from abc import ABC, abstractmethod

class CipherAlgorithm(ABC):

    @abstractmethod
    def encrypt(self, plaintext, key):
        pass

    @abstractmethod
    def decrypt(self, ciphertext, key):
        pass
