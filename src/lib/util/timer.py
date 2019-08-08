############################################################
##############               Timer                 #########
############################################################
"""
Usage:
    timer = Timer()
    timer.start("jobID")
    print("jobID takes {} ms".format(timer.stop("jobID"))
"""

import time

class Timer(object):

    """timer class"""
    starts = {} # {key: start_time}
    ends   = {} # {key: end_time}


    def __init__(self):
        pass

    def start(self, key):
        """start timer for key
        Args:
            key: 

        Return: 
        """
        assert key not in self.starts, "{} already started!".format(key)
        self.starts[key] = time.time()
        self.ends.pop(key, None)


    def stop(self, key):
        """stop timer for key
        Args:
            key: 

        Return: elapsed time 
        """
        assert key in self.starts, "{} not started!".format(key)
        now = time.time()
        self.ends[key] = now 
        elapsed = now - self.starts.pop(key)
        return elapsed 

    def stop_and_report(self, key):
        """
        Args:
            key: 

        Return: 
        """
        elapsed = self.stop(key)
        print("{:16}:  {:.3f} s".format(key, elapsed))
