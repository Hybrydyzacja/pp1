# 27.	An influencer is a person who can influence other people's behaviour. An influencer communicates with other people using social networking sites. 
# Write a program that checks whether a given person can be a good influencer, that is, whether the person has at least two of the following accounts: 
# Facebook, Twitter or Instagram. Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. 
# Sample result:
# facebook = True
# twitter = False
# instagram = True
# A person can be a good influencer!

facebook = True
twitter = False
instagram = True
if facebook and twitter or facebook and instagram or twitter and instagram:
    print("A person can be a good influencer!")