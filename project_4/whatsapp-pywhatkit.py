import pywhatkit

# phone_number = input("Enter the phone number: ")

# CONTACT
# scheduling of a message
# pywhatkit.sendwhatmsg(phone_no=phone_number,
#                       message="Testing pywhatkit",
#                       time_hour=11,
#                       time_min=10, 
#                       wait_time=15, 
#                       tab_close=True)

# Send message instantly
# pywhatkit.sendwhatmsg_instantly(phone_no=phone_number,
#                       message="Testing pywhatkit",
#                       wait_time=15, 
#                       tab_close=True)

# GROUP
group_id = input("Enter group id:")
# scheduling of a message in a group
# pywhatkit.sendwhatmsg_to_group(group_id=group_id,
#                       message="Testing pywhatkit group message",
#                       time_hour=11,
#                       time_min=10, 
#                       wait_time=15, 
#                       tab_close=True)
# Send message instantly in a group
pywhatkit.sendwhatmsg_to_group_instantly(group_id=group_id,
                      message="Testing pywhatkit group message",
                      wait_time=15, 
                      tab_close=True)