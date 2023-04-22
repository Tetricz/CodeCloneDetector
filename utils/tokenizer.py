import os, keyword
import tokenize

class tokenizer:

    def tokenize_python(self, filePath, filename):
        """
        Tokenizes python source code.
        Insuring standardization of variable names and function names.
        """
        varTokenDictionary = {}
        tokens = None
        nonKeywordTokens = []
        with tokenize.open(filePath + "/" + filename) as f:
            tokens = tokenize.generate_tokens(f.readline)
            for token in tokens:
                if token[0] is 1:
                    if not keyword.iskeyword(token[1]):
                        nonKeywordTokens.append(token)
                        if token[1] not in varTokenDictionary:
                            varTokenDictionary[token[1]] = f"var{len(varTokenDictionary) + 1}"

        tokenFileName = filename.split(".")[0] + "_tokens.txt"
        fileData = ""
        # TODO: Write this to be more efficient
        # Utilize bytearrays or something instead of immutable strings
        with open(filePath + "/" + filename) as f:
            for lineNumber, line in enumerate(f):
                for token in nonKeywordTokens:
                    if token[2][0] == lineNumber + 1:
                        linediff = len(token[4]) - len(line)
                        line = line[0:token[2][1]-linediff] + varTokenDictionary[token[1]] + line[token[3][1]-linediff:]
                fileData += line

        with open(filePath + "/" + tokenFileName, "w") as f:
            f.write(fileData)

        #print(fileData)
        #print(varTokenDictionary)
        return tokenFileName

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    tokenizer.tokenize_python(filePath="../testfiles/preprocessed_check_polygon/", filename="check_triangle.py")


