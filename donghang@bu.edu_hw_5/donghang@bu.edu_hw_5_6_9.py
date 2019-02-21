# Conversions between feet and meters


# Converts from feet to meters
def footToMeter(foot):

    meter = 0.305 * foot
    return meter


# Converts from meters to feet
def meterToFoot(meter):

    foot = meter / 0.305
    return foot


def main():

    print("{0:<9} {1:<9} |     {1:<9} {0:<9}".format("Feet", "Meters"))
    j = 20
    for i in range(1, 11):
        print("{0:<9.1f} {1:<9.3f} |     {2:<9.1f} {3:<9.3f}".format(i, footToMeter(i), j, meterToFoot(j)))
        j += 6


main()
