from unittest import TestCase, main


class PartitionTests(TestCase):
    def test_clades_of_interest(self):
        # in a postorder traversal
        # yield the set of ncbi taxonomy ids for a clade
        # such that the clade is interesting
        self.fail()

    def test_is_this_clade_interesting(self):
        # determine if a clade is intersting based off:
        # - the number of samples represented
        # - the total number of samples
        self.fail()

    def test_number_of_samples_in_clade(self):
        # compute the number of samples represented by a clade
        self.fail()

    def test_construct_binary_labels(self):
        # construct a pandas series
        # representing which samples are "within the clade of interest"
        # and which samples are "not within the clade of interest"
        self.fail()


if __name__ == '__main__':
    main()
