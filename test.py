import tabula
import shutil


class Statement:

    def __init__(self, file):
        self.file = file
        self.csv_file = self.file.replace(".pdf", ".csv")

    def pdf_to_csv(self):
        # Read a PDF File
        pdf = tabula.read_pdf(self.file, pages='all')[0]
        # convert PDF into CSV
        tabula.convert_into(self.file, self.csv_file, output_format="csv", pages='all')

    def backup(self):
        pass

    def parse_csv(self):
        with open(self.csv_file, 'r') as file:
            for line in file:
                print(line.split(','))


def main():
    s = Statement("")

    s.parse_csv()



