class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "%s sec" % self.s

    def __repr__(self):
        return "Time(%s)" % self.s

if __name__ == "__main__":
	time1 = Time(12)
	time2 = Time(3456)
	print (time1, time2)            # Python wywołuje str()
	print ([time1, time2])          # Python wywołuje repr()