grades_path = "../csvs/grades.csv"
import csv


class CSVComprehension:
    def __init__(self, path: str, encoding: str = "utf-8") -> None:
        ""
        with open(path, "r", encoding=encoding) as f:
            self._list = [i for i in csv.reader(f)]


a = CSVComprehension(grades_path)
