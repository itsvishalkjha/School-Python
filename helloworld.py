#what is a comment 

#to give a comment use a hastag , comment hota kya hai ? comment is a piece of code which the computer does not act upon

#problem 1 -
#  and friends planned a picnic
#   gave 5000 rupees ,  and  have 3000 rupees what percent of money  
# contributed  in the total amount

#here v is amount by  , a is amount by others t is the sum of total amount x and y are used to find 
# the percentage and also we have used f to find the remaining percentage so that the code looks pretty

# v = 5000
# a =  3000
# t = v+a

# x = v/t 
# y= x*100
# f = 100-y
# print("The percentage of money  contributed is :", y)
# print("The percentage of money others contributed is :", f)


#problem 2 finding the winner of class votin assembly

abhigyan = input("Enter the number of votes for Abhigyan: ")
swapnil = input("Enter the number of votes for Swapnanil: ")
dhritiraj = input("Enter the number of votes for Dhritiraj: ")

abhigyan = int(abhigyan)
swapnil = int(swapnil)
dhritiraj = int(dhritiraj)

total_votes =  abhigyan + swapnil + dhritiraj


abhigyan_percent = (abhigyan / total_votes) * 100
swapnil_percent = (swapnil / total_votes) * 100
dhritiraj_percent = (dhritiraj / total_votes) * 100


#Printing the results
print("Results:")

print("Abhigyan: ", abhigyan_percent, "%")
print("Swapnil: ", swapnil_percent, "%")
print("Dhritiraj: ", dhritiraj_percent, "%")


#bringing in the condition

if abhigyan > swapnil and abhigyan > dhritiraj:
    print("Abhigyan party dena hoga ")
elif swapnil> abhigyan and swapnil >dhritiraj:
    print("Swapnil party kab derha ")
elif dhritiraj>abhigyan and dhritiraj>swapnil:
    print("Dhriti faad dia elections , netaji slayy ")

    
