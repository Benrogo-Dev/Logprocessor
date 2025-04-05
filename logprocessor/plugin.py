"""
Base class and loader for post-processing
plugins.

Plugins can be added from any directory and
must contain plugin classes (subclasses of
LogProcessorPlugin).

These plugins execute independently of each
other in the order they are loaded by this
script. The classes will each be passed the
metrics dictionary generated after processing
the log files.
"""