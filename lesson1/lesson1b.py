goal = 100
current_volunteers = 101
needed = (goal - current_volunteers)
extra = (current_volunteers - goal)

if current_volunteers < goal:
	print "Keep recruiting! You need",needed, "additional volunteers."
elif current_volunteers >= goal:
	print "You're ready to go!"
	if current_volunteers > 100:
		print "You have",extra, "extra volunteer(s)!"
else:
	print "#"