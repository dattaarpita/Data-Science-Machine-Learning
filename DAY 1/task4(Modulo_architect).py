x=int(input("Enter raw number of seconds:"))
hours=x//3600
remaining_second=x%3600
mins=remaining_second//60
seconds=remaining_second%60
print(f"{hours} Hours, and {seconds} seconds")
