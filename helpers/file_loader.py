class FileLoader:
    @staticmethod
    def load_file_to_str(filepath: str) -> str:
        """
        Loads a file to a string
        :param filepath: The path to the file
        :return: The file as a string
        """
        with open(filepath, 'r') as file:
            return file.read()
