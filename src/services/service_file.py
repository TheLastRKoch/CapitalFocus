
class FileService:

    def read_textfile(self, filepath):
        with open(filepath) as f:
            return "\n".join(f.readlines())

    def write_textfile(self, filepath, text):
        with open(filepath, 'w') as f:
            f.write(text)
