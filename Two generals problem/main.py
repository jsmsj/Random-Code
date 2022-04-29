from helpers import *
       
castle = Castle()

general1 = General("general1",1000)
general2 = General("general2",1000)

messengers_list = general1.create_messengers(20,"i will attack at dawn")

passing_through_castle(messengers_list,castle,general1)

confirmation_list = general2.create_messengers(20,"okayy all the best")

passing_through_castle(messengers_list,castle,general2)

print(summary(castle,general1,general2))
