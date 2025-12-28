from kripto.cipher_base import CipherAlgorithm


class PlayfairCipher(CipherAlgorithm):

    def generate_matrix(self, key):
        key = key.upper().replace("J", "I")
        matrix = []
        used = set()

        for c in key:
            if c.isalpha() and c not in used:
                matrix.append(c)
                used.add(c)

        for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if c not in used:
                matrix.append(c)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_pos(self, matrix, char):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c

    def prepare_text(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0

        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'X'
            if a == b:
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        return pairs

    def encrypt(self, text, key):
        matrix = self.generate_matrix(key)
        pairs = self.prepare_text(text)
        result = ""

        for a, b in pairs:
            r1, c1 = self.find_pos(matrix, a)
            r2, c2 = self.find_pos(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
            elif c1 == c2:
                result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]

        return result

    def decrypt(self, text, key):
        matrix = self.generate_matrix(key)
        result = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.find_pos(matrix, a)
            r2, c2 = self.find_pos(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
            elif c1 == c2:
                result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]

        return result
