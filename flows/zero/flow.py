from metaflow import Parameter, card, resources, step
from obproject import ProjectFlow


class ZeroScalableFlow(ProjectFlow):  # pyright: ignore
    # by default run with 1% of data
    pct = Parameter("pct", default=1, type=int)

    @card
    @step
    def start(self):
        print("loading data...")
        from mymodule import load_data

        self.countries = load_data(n=self.pct)  # pyright: ignore
        self.next(self.train, foreach="countries")

    @resources(cpu=1, memory=1024)
    @card
    @step
    def train(self):
        print("training model...")
        from mymodule import scoring_function

        self.score, self.country = scoring_function(self)
        self.next(self.join)

    @card
    @step
    def join(self, inputs):
        print("joining training runs...")
        from mymodule import join_step

        self.best = join_step(inputs)
        self.next(self.end)

    @step
    def end(self):
        print(self.best, "produced best results")


if __name__ == "__main__":
    ZeroScalableFlow()


# Notes:
# ProjectFlow type-> FlowMutator(obproject.projectbase.project_pypi)
# FlowSpec type-> <class 'metaflow.flowspec.FlowSpecMeta'>
