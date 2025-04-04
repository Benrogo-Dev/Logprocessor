import unittest
from logprocessor.libs.fast_metric_merge import fast_merge

class TestMetrics(unittest.TestCase):
    def setUp(self):
        print(f"\nRunning test: {self.id()}")
    
    # Test that metrics are merged correctly
    def test_merge(self):
        initial_metrics = {
            "metric1": {"id1": 10},             # Check handling of single values
            "metric2": {"id2": 20, "id3": 21},  # Check handling of multiple values
            "metric3": {},                      # Check handling of empty values
        }
        added_metrics = {
            "metric1": {"id1": 5, "id5": 7},
            "metric2": {"id2": 6},
            "metric3": {"id6": 8}
        }
        target_metrics = {
            "metric1": {"id1": 15, "id5": 7},
            "metric2": {"id2": 26, "id3": 21},
            "metric3": {"id6": 8}
        }
        fast_merge(added_metrics, initial_metrics)
        self.assertEqual(initial_metrics, target_metrics, "Metrics dictionaries were not merged correctly.")

if __name__ == "__main__":
    unittest.main()