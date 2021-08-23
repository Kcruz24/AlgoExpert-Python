# O(N) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	totalSpeed = 0
	
	while len(redShirtSpeeds) > 0:
		fastestRedShirt = max(redShirtSpeeds)
		blueShirtRider = min(blueShirtSpeeds) if fastest else max(blueShirtSpeeds)
	
		tandemSpeed = max(fastestRedShirt, blueShirtRider)
	
		totalSpeed += tandemSpeed
	
		redShirtSpeeds.pop(redShirtSpeeds.index(fastestRedShirt))
		blueShirtSpeeds.pop(blueShirtSpeeds.index(blueShirtRider))
			
	return totalSpeed