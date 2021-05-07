#Declaring a dictonary to hold the people and their data

people = { }
add = True
#Creating variables to store values

mHeight=0
mWeight=0
mTotal=0
fHeight=0
fWeight=0
fTotal=0
#Creating a while loop to contain the adding of people
while  add == True:
	#Collect information about the individual
	name = str(input("What is the name of the individual"))
	gender = str(input("What is the gender. Enter either m or f"))
	if gender == 'm':
		mTotal=mTotal + 1
		height = int(input("What is their height in inches"))
		mHeight = mHeight + height
		weight = int(input("What is their weight in pounds"))
		mWeight = mWeight + weight
		

		#Add that information to a new key value pair inside dictonary
		people[name]= height,weight,gender
		#Shows the current dictonary
		print(people)
		#asks if they would like to continue filling out the dictonary
		tf=str(input("Would you like to add another person? Enter y or n for yes or no"))
		if tf == 'n':
			add=False
	else :
		fTotal + 1
		height = int(input("What is their height in inches"))
		fHeight= fHeight+ height
		weight = int(input("What is their weight in pounds"))
		fWeight = fWeight + weight
		
		#Add that information to a new key value pair inside dictonary
		people[name]= height,weight,gender
		#Shows the current dictonary
		print(people)
		#asks if they would like to continue filling out the dictonary
		tf=str(input("Would you like to add another person? Enter y or n for yes or no"))
		if tf == 'n':
			add=False
#Asking wether or not they think males or females will have a higher bmi
quieston = str(input("Do you think that the males had a higher average bmi or the females. \n To guess enter either m or f"))
#BMI Calculations
mBMI = (mWeight*703)/mHeight*mHeight
fBMI = (fWeight*703)/fHeight*fHeight

if quieston == 'm':
	if mBMI > fBMI :
		print("Congrats! You were right, us guys do be chunky sometimes")
	else :
		print("Oooohhh you had to much faith in the girls to be skinny queens, sorry bud")
else :
	if mBMI > fBMI :
		print("Ahhh see, you should have known those girls were gonna be skinnier")
	else :
		print("Congrats you called it, looks like wine actually does have calories in it!")