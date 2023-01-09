import sys
import time


def countdown_timer():
    """Auxiliary timer function. Simulates production time. """
    for remaining in range(5, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("Please hold while production in progress. {:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rProduction complete! \n")
