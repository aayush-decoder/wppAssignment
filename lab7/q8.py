import random as rd

class Decoder:
    chunks = []
    result = set()

    def __init__(self, code):
        self.code = code

    def decode(self):
        for k in range(100):
            var = rd.randint(1,2)
            self.chunks = []
            for i in range(0, len(self.code), var):
                self.chunks.append(self.code[i:i+rd.randint(1,2)])
                if var ==2:
                    i+=1
            if '0' in self.chunks or any(int(chunk) > 26 for chunk in self.chunks):
                continue
            self.result.add("".join([chr(int(chunk)+64) for chunk in self.chunks]))
        print(self.result)

decoder = Decoder("11106")
decoder.decode()