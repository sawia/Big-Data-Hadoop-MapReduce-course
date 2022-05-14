from mrjob.job import MRJob


class MRWordCounter(MRJob):

    def mapper(self, _, line):
        yield 'chars', len(line)
        yield 'words', len(line.split())

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    MRWordCounter.run()
