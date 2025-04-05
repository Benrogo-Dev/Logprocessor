"""
Small extra library to merge metrics dictionaries.

Written in Cython for better performance than would
normally be possible with Python.

IMPORTANT NOTES FOR ANYONE PLANNING TO USE THIS FOR
OTHER PROJECTS:

The fast_merge function is built SPECIFICALLY for the
metrics dictionaries used in Logprocessor. It does not
check for the existence of keys in the results dictionary
before attempting to insert data to increase performance.
This is fine for Logprocessor because the LogMetrics
class ensures that keys can never be mismatched but
please keep this in mind if you intend to repurpose the
code here.
"""

from cython import cdivision
from libc.stdint cimport int64_t

@cdivision(True)
def fast_merge(dict[str, dict[str, int]] new_metrics, dict[str, dict[str, int]] results):
    cdef str metric, key
    cdef int64_t value, val1, val2
    cdef int n, i
    cdef list new_keys

    # Precalculate length and keys of new_metrics to shave
    # off a bit of extra calculating in the main loop
    n = len(new_metrics)
    new_keys = list(new_metrics.keys())

    for i in range(n):
        metric = new_keys[i]
        sub_new = new_metrics[metric]
        sub_results = results[metric]

        for key in sub_new:
            val1 = <int64_t>sub_new[key]
            val2 = 0
            # Use "in" instead of Python's get() function
            if key in sub_results:
                val2 = <int64_t>sub_results[key]
            value = val1 + val2
            sub_results[key] = value