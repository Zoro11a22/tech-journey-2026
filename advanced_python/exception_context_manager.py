class FileProcessor:
    def __enter__(self):
        print("Opening file...")
        return self

    def process(self):
        print("Processing file...")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error while processing file.")
            print(exc_type.__name__)
            print(exc_value)
            return True
        else:
            print("File processed successfully.")

with FileProcessor() as fp:
    fp.process()

with FileProcessor() as fp:
    fp.process()
    int("abc")