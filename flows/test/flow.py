from metaflow import step, kubernetes
from obproject import ProjectFlow

cp="c5-2x-task"

class TestFlow(ProjectFlow):

    @kubernetes(compute_pool=cp)
    @step
    def start(self):
        import numpy as np
        import pydantic as pd
        import pyiceberg as pi

        print("version:", np.__version__)
        print("version:", pd.__version__)
        print("version:", pi.__version__)
        self.next(self.end)

    @kubernetes(compute_pool=cp)
    @step
    def end(self):
        print("Done")

if __name__ == "__main__":
    TestFlow()