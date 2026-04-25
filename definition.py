import os

import pandas


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "data.csv")

        df = pandas.read_csv(file_path)
        return tuple(df.loc[df['word'] == self.term]['definition'])