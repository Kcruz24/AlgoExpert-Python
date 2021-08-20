# O(N) time | O(1) space - DOES NOT WORK
def class_photos(red_shirt_heights, blue_shirt_heights):
	taller_heights = 0
	
	for i in range(len(blue_shirt_heights)):
		blue_back_row = max(blue_shirt_heights) > max(red_shirt_heights)

		if blue_shirt_heights[i] > red_shirt_heights[i] and blue_back_row:
			taller_heights += 1
		elif red_shirt_heights[i] > blue_shirt_heights[i]:
			taller_heights += 1
	
	return taller_heights == len(blue_shirt_heights)
	
	
# O(N) time | O(1) space - DOES NOT WORK
def class_photos2(red_shirt_heights, blue_shirt_heights):
	
	if max(blue_shirt_heights) == max(red_shirt_heights):
		return False
	
	back_row = max(max(blue_shirt_heights), max(red_shirt_heights))
	
	for i in range(len(blue_shirt_heights)):
		tallest_blue_shirt = max(blue_shirt_heights)
		tallest_red_shirt = max(red_shirt_heights)
		
		if back_row in blue_shirt_heights and tallest_blue_shirt < tallest_red_shirt:
			blue_shirt_heights.pop(tallest_blue_shirt)
			return False
		elif back_row in red_shirt_heights and tallest_red_shirt < tallest_blue_shirt:
			red_shirt_heights.pop(tallest_red_shirt)
			return False
	
	return True
	
# O(Nlog(N)) time | O(1) space - SOLUTION
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