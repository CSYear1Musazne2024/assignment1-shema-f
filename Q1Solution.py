def findRent(start,end):
 f start < 0 or end < 0 or start >= 24 or end > 24 or start >= end:
        return "Invalid input"
    
    total_cost = 0
    current_time = start
    
    # Loop through the times from start to end
    while current_time < end:
        if (0 <= current_time < 7) or (21 <= current_time < 24):
            # From 0-7 and 21-24, the rate is RWF 500 per hour
            next_time = min(end, 7) if current_time < 7 else min(end, 24)
           total_cost += (next_time - current_time) * 500
            current_time = next_time
        elif 7 <= current_time < 10 or 19 <= current_time < 21:
            # From 7-10 and 19-21, the rate is RWF 1000 per hour
            next_time = min(end, 10) if current_time < 10 else min(end, 21)
            total_cost += (next_time - current_time) * 1000
            current_time = next_time
        elif 10 <= current_time < 19:
            # From 10-19, the rate is RWF 1500 per hour
            next_time = min(end, 19)
            total_cost += (next_time - current_time) * 1500
            curent_time=next_time
            
      return total_cost

start=int(input("Enter start time"))
end=int(input("Enter end time"))
print(findRent(start,end))
