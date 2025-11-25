from metaflow import step
from obproject import ProjectFlow

class TestFlow(ProjectFlow):

    @step
    def start(self):
        import numpy as np
        import pydantic as pd
        import pyiceberg as pi

        print("version:", np.__version__)
        print("version:", pd.__version__)
        print("version:", pi.__version__)
        self.next(self.end)

    @step
    def end(self):
        print("Done")

if __name__ == "__main__":
    TestFlow()