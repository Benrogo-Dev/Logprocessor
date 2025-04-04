from cython import cdivision
from libc.stdint cimport int64_t

@cdivision(True)
def fast_merge(dict[str, dict[str, int]] new_metrics, dict[str, dict[str, int]] results):
    cdef dict sub_new, sub_results
    cdef str metric, key
    cdef int64_t value
    cdef int n
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
            # Using int64_t here bypasses Python's integer handling
            value = <int64_t>sub_new[key] + <int64_t>sub_results.get(key, 0)

            # Update the result directly without any overhead
            sub_results[key] = value
