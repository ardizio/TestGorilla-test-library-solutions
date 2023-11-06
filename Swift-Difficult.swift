func aboveAverageSalesCount(_ sales:[Int] ) -> Int {
	var i = 0
	var sum = 0
	for s in sales{
		sum += s
		i += 1
	}
	let mean = sum/i

	if(i>5 && i<50){
	    var streak = 0
        var currentStreak = 0
        for day in sales{
            if day > mean{
                currentStreak += 1
                if(currentStreak>streak){
                    streak = currentStreak
                }
            }
            else{ currentStreak = 0 }
        }
        return streak	
	}
	else{
		return -1
	}
}


// max number of consecutive days of sales above aboveAverageSalesCount
func aboveAverageSalesCount(_ sales: [Int]) -> Int {
    let n = sales.count

    // Check if the number of days is within the desired range
    if n >= 5 && n <= 50 {
        let mean = sales.reduce(0, +) / n

        var streak = 0
        var currentStreak = 0

        for day in sales {
            if day > mean {
                currentStreak += 1
                streak = max(streak, currentStreak)
            } else {
                currentStreak = 0
            }
        }

        return streak
    } else {
        return -1
    }
}
