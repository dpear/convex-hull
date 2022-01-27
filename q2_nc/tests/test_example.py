from unittest import TestCase, main
import pandas as pd
import pandas.testing as pdt

from q2_nc._example import samples_of_interest


class ExampleTests(TestCase):
    def setUp(self):
        self.data = pd.DataFrame([['foo', '1234', 'bar'],
                                  ['taco', '9606', 'baz'],
                                  ['bing', '111', 'stuff']],
                                 columns=['A', 'host_tax_id', 'C'])

    def test_samples_of_interest(self):
        exp = pd.Series([False, True, False], name='host_tax_id')
        obs = samples_of_interest(self.data)
        pdt.assert_series_equal(obs, exp)


if __name__ == '__main__':
    main()
