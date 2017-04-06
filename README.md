# the-biggest-square


Short description of the algorithm:

Sort towers based on height<br/>
loop through sorted towers and add tower original index to list<br/>
check from that list how many neighbours are already list<br/>
min (amount of neighbours, tower height) is the size of the square that fits behind this tower and it's neighborous<br/>
repeat until tower height <= found biggest square 
		   
		   
		   
Algorithm:<br/>
towers = input
<br/>
towers.sort  # tallest first
<br/>
<br/>
indexList = [None] * towers.size 
<br/>
biggestSquare = 0
<br/>
<br/>
for tower in towers
<br/>
&nbsp;&nbsp;if tower.height <= biggestSquare
<br/>
&nbsp;&nbsp;&nbsp;return biggestSquare
<br/>
<br/>
&nbsp;&nbsp;indexList[tower.index] = tower.index
<br/>
&nbsp;&nbsp;left = indexList.findLastNoneBefore(index)
<br/>
&nbsp;&nbsp;right = indexList.findNextNoneAfter(index)
<br/>
<br/>
&nbsp;&nbsp;squareSize = min( ( right-left ) - 1, tower.height )
<br/>
&nbsp;&nbsp;if squareSize > biggestSquare
<br/>
&nbsp;&nbsp;&nbsp;biggestSquare = square
       
       
