from FileManipulator import FileManipulator
import os.path


def __main__():
    # Path declaration block
    input_path = os.path.normpath(r"/home/zj/Documents/Projects/Personal/XlsToXlsx/Example")
    output_path = os.path.normpath(input_path + "_new")

    # Converting block
    converter = FileManipulator(output_path, input_path)

    converter.copy_directory(input_path, output_path)

    # creates a list of .xls files
    xls_files = converter.find_files("(.*?).xls$")

    converter.xls_to_xlsx(xls_files)

__main__()
