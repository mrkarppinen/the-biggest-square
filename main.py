
import sys

def find_biggest_square(towers):
    # sort towers based on height
    towers.sort(key=lambda pair: pair[1], reverse = True)

    # indexes list will hold tower indexes
    indexes = [None] * len(towers)
    biggestSquare = 0

    # loop thorough ordered towers list
    for tower in towers:
        height = tower[1]
        index = tower[0]

        if (height <= biggestSquare):
            # if already found square with size height * height
            # return biggestSquare as towers are getting shorter
            return biggestSquare

        indexes[index] = index

        # indexes list will contain towers taller than this tower
        # check how many neighbour towers are already in the list
        # so the biggestSquare after this tower is added to list is
        # neighborougs * height
        size = tower_sequence(indexes, index, height)
        if ( size > biggestSquare ):
            biggestSquare = size

    return None


def tower_sequence(items, i, maxLength):
    leftNeighbours = neighbours(items, i, -1, max(0, i-maxLength) )

    if (leftNeighbours + 1 == maxLength):
        return maxLength

    rightNeighbours = neighbours(items, i, 1, min(len(items)-1, i + (maxLength - leftNeighbours) ) )
    return (leftNeighbours + rightNeighbours + 1)


def neighbours(items, i, step, end):
    if i == end:
        return 0

    start = i + step
    end = end + step

    for index in xrange(start, end, step):
        if items[index] == None:
            return abs(i-index)-1

    return abs(start - end)


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) == 2 else  'input.txt'

    input = open(filename)

    towers = [ (index, int(line)) for index, line in enumerate(input)]

    print 'Solution ' + str(find_biggest_square(towers))
