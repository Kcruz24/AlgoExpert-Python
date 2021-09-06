# O(Nlog(N)) time | O(1) space - SOLUTION (Mine)
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    if max(redShirtHeights) > max(blueShirtHeights):
        for idx, redShirt in enumerate(redShirtHeights):
            if blueShirtHeights[idx] >= redShirt:
                return False
    else:
        for idx, blueShirt in enumerate(blueShirtHeights):
            if redShirtHeights[idx] >= blueShirt:
                return False

    return True
	
# O(Nlog(N)) time | O(1) space - SOLUTION (Algo Expert)
def class_photos4(redShirtHeights, blueShirtHeights):

	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	first_row = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
	
	for idx in range(len(blueShirtHeights)):
		blueShirtHeight = blueShirtHeights[idx]
		redShirtHeight = redShirtHeights[idx]
		
		if first_row == 'RED':
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
			
	return True