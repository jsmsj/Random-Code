from helpers import *
       
castle = Castle()

general1 = General("general1",1000) # General(name,army_count)
general2 = General("general2",1000)

general1.army_check() # check if army_count <= 0
general2.army_check()

messengers_list = general1.create_messengers(20,"i will attack at dawn") #create messengers
general1.army_check()

passing_through_castle(messengers_list,castle,general1) #messengers passing through the castle

confirmation_list = general2.create_messengers(20,"okayy all the best")
general2.army_check()


passing_through_castle(messengers_list,castle,general2)

print(summary(castle,general1,general2)) # print summary of the above
