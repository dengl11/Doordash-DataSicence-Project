import unittest
from util import parse_utc_timestamp, diff_timestamps, add_timestamp_by_seconds

class Test(unittest.TestCase):

    def test_time_parser(self):
        seconds = diff_timestamps("2015-02-25 02:22:30", "2015-02-25 02:22:31")
        self.assertAlmostEqual(seconds, 1)

        seconds = diff_timestamps("2015-02-25 02:21:30", "2015-02-25 02:22:30")
        self.assertAlmostEqual(seconds, 60)

        seconds = diff_timestamps("2014-02-25 02:21:30", "2015-02-25 02:21:30")
        self.assertAlmostEqual(seconds, 365 * 24 * 3600)

    def test_time_elapse(self):
        elapsed = add_timestamp_by_seconds("2015-02-25 02:22:30", 1)
        self.assertEqual(elapsed, "2015-02-25 02:22:31")

        elapsed = add_timestamp_by_seconds("2015-02-25 02:22:30", 365 * 24 * 3600)
        self.assertEqual(elapsed, "2016-02-25 02:22:30")
if __name__ == "__main__":
    unittest.main()

