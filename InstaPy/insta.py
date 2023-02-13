# Program            :  INSTA SCRIPT
# Author             :  ONG CHANG LE
# Email              :  websitecl03@gmail.com
# Start Date         :  25/4/2022
# Finish Date        :  27/05/2022
# Latest Update Date :  13/2/2023



# Disclaimer :
# 1. Don't use main account, use your second account or test account for safety
# 2. Don't spam others without permission, this script is just for fun and Instagram management
# 3. Manage your account easily with the feature you like
# 4. If you want to involve in this project or any feedback, kindly hit the mail box mention above
# 4. Developer/Author will not take any responsibility on your account banning and troubles you cause
# 5. Play safe, have fun


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


# requirements :
# 1. selenium module (pip install selenium)
# 2. chrome driver (https://chromedriver.chromium.org/downloads) --> Setup tutorial :https://www.youtube.com/watch?v=Xjv1sY630Uc



PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

time.sleep(3)


disclaimer_note = "\nDisclaimer :\n1. Don't use main account, use your second account or test account for safety\n2. Don't spam others without permission, this script is just for fun and Instagram management\n3. Manage your account easily with the feature you like\n4. If you want to involve in this project or any feedback, kindly hit the mail box mention above \n4. Developer/Author will not take any responsibility on your account banning and troubles you cause\n5. Play safe, have fun\n\n"
print(disclaimer_note)

target_list = ['nike', 'adidas', 'kfc', 'mcdonalds', 'marvel', 'disney']
random_comment=["nice post", "have a great day", "inspirational", "well deserved", "see your effort so good", "keep it up", "absolute great", "fantastic", "awesome", "brilliant", "wonderful", "effortless"]
option = "1.  Search A Person\n2.  Get Profile Information\n3.  Click Next Picture\n4.  Follow A Person\n5.  Follow Many Person\n6.  Like First Post In Profile\n7.  Like All Post In Profile\n8.  Comment First Post In Profile\n9.  Comment All Post In Profile\n10. Comment and Spam A Post In Profile\n11. Comment and Spam A Post With Link\n12. Message A Person\n13. Message and Spam A Person\n14. Message Many People\n15. Message and Spam Many People\n16. Get Following List\n17. Get Following List 2\n18. Get Follower List\n19. Get Post Like Number\n20. Exit The Program\n"





#################################################################    ALL THE FUNCTIN AT HERE    ###########################################################################################################


# Press follow button
def press_follow_button():
    driver.find_element(by=By.XPATH, value="//*[@class='_aacl _aaco _aacw _aad6 _aade']").click()


# Press unfollow button
def press_unfollow_button():
    driver.find_element(by=By.XPATH, value="//div[contains(text(),'Unfollow')]").click()


 # Open first post in profile
def open_first_post_in_profile():
    driver.find_element(by=By.XPATH, value="//div[@class='_aagw']").click()


## LIKE ##

# Press like button
def like_post():
    driver.find_element(by=By.XPATH, value="//span[contains(@class,'_aamw')]//button[contains(@type,'button')]").click()


# Press next button
def press_next_button():
    driver.find_element(by=By.XPATH, value="//div[contains(@class,'_aaqg _aaqh')]//button[contains(@type,'button')]").click()


## COMMENT ##

# Click comment section
def click_comment_section():
    driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").click()



# Type comment in comment section
def type_text_in_comment_section(comment):
    driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(comment)



# Post comment
def post_comment():
    driver.find_element(by=By.XPATH, value="//div[contains(text(),'Post')]").click()



# Press Ok button when in ban (comment)
def press_ok_in_ban():
    driver.find_element(by=By.XPATH, value="//button[normalize-space()='OK']").click()



## MESSAGE ##

# Click message button in home page
def click_send_message_button_in_home_page():
    driver.find_element(by=By.XPATH, value="//*[@aria-label='Messenger']").click()


# Click send message button
def click_send_message_button():
    driver.find_element(by=By.XPATH, value="//button[text()='Send Message']").click()


# Search the person to message
def search_person_to_message(msg_person):
    driver.find_element(by=By.XPATH,  value="//input[@placeholder='Search...']").send_keys(msg_person)


# Select the person to message
def select_the_person_to_message():
   driver.find_element(by=By.XPATH, value="//*[@aria-label='Toggle selection']").click()


# Click next button to process to message 
def click_next_button_to_message():
    driver.find_element(by=By.XPATH, value="//button[@class='_acan _acao _acas _acav _aj1-']/div[text()='Next']").click()


# Type the message to send
def type_message_to_send(message):
    driver.find_element(by=By.XPATH, value="//*[@placeholder='Message...']").send_keys(message)


# Send message
def send_the_message():
    driver.find_element(by=By.XPATH, value="//button[text()='Send']").click()


# Click the following button to open the following list
def click_following_list():
    driver.find_element(by=By.XPATH, value="(//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade'])[3]").click()


# Scroll the following list
def scroll_following_list():
    scroll = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
    scroll.click()
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)


# Click the followers list
def click_followers_list():
    driver.find_element(by=By.XPATH, value="(//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade'])[2]").click()


# Scroll the followers list
def scroll_followers_list():
    scroll = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
    scroll.click()
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)

#################################################################    ALL THE FUNCTIN AT HERE    ###########################################################################################################




# login
def login(username="heyboy123.321", password="good123456#"):
    search = driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[1]/div/label/input")
    search.send_keys(username)

    search = driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[2]/div/label/input")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)

    time.sleep(5)
    try:
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/div/div/div/button").click()
    except:
        pass
    time.sleep(2)
    # try:
    #     driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    # except Exception:
    driver.find_element(by=By.XPATH, value="// button[text() = 'Not Now']").click()


# name_list = ["nike", "adidas"]
#
# for i in name_list:
#     driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(i)
#     time.sleep(3)
#     driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div").click()
#     time.sleep(3)
#     driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
#     driver.get("https://www.instagram.com/")


# Search name
def search_name(name="cl_ong0504"):
    try:
        driver.find_element(by=By.XPATH, value="//*[@aria-label='Search']").click()
        driver.find_element(by=By.XPATH, value="//*[@aria-label='Search input']").send_keys(name)
        time.sleep(3)

        # Click profile
        driver.find_element(by=By.XPATH, value="//*[@class='_abm4']").click()
        time.sleep(3)
    except Exception:
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        driver.find_element(by=By.XPATH, value="//*[@aria-label='Search']").click()
        driver.find_element(by=By.XPATH, value="//*[@aria-label='Search input']").send_keys(name)
        time.sleep(10)

        # Click profile
        driver.find_element(by=By.XPATH, value="//*[@class='_abm4']").click()                               
        time.sleep(10)



# Print out the follower information
def profile_information(name="cl_ong0504"):
    search_name(name)
    try:
        posts = driver.find_element(by=By.XPATH,  value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span").text                # posts
        followers = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span").text           # followers
        following = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span/span").text           # following

    except Exception:
        posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span").text
        followers = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[2]/div/span").text
        following = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[3]/div/span").text


    print(f"Posts number : {posts} \nFollowers number : {followers} \nFollowing number : {following}")
    driver.get("https://www.instagram.com/")


# Next picture
def click_next_picture(name="cl_ong0504"):
    search_name(name)
    open_first_post_in_profile()                                # Open first post in profile                                    
    press_next_button()                                         # Press next button to like post
    time.sleep(2)
    driver.get("https://www.instagram.com/")



# Follow a user
def follow_one_person(name="cl_ong0504"):
    search_name(name)
    press_follow_button()                                       # Press follow button
    time.sleep(1)
    driver.get("https://www.instagram.com/")



# Loop the list to follow
def follow_many_people(following_list=target_list):

    for i in following_list:
        try:
            driver.get("https://www.instagram.com/" + i)
            time.sleep(2)
            press_follow_button()                              # Press follow button
        except:
            time.sleep(5)
            driver.get("https://www.instagram.com/" + i)
            time.sleep(5)
            press_follow_button()                              # Press follow button

    driver.get("https://www.instagram.com/")



# Like a post
def like_first_post_in_profile(name="cl_ong0504"):
    search_name(name)
    open_first_post_in_profile()                               # Open first post in profile
    like_post()                                                # Press like button
    driver.get("https://www.instagram.com/")





# Loop for like all post
def like_all_post_in_profile(name="cl_ong0504"):
    search_name(name)
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span").text
    like_post_num = int(posts)
    try:
        open_first_post_in_profile()                         # Open first post in profile
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        open_first_post_in_profile()                         # Open first post in profile

    for i in range(like_post_num):
        if i < like_post_num-1:
            if i != 0 and i % 50 == 0:
                
                # If get ban or too many posts
                try:
                    time.sleep(100)     
                    like_post()                             # Press like button
                    press_next_button()                     # Press next button to like next post
                    time.sleep(2)
                except Exception:
                    press_next_button()                     # Press next button to like next post
                    time.sleep(2)


            # It will firstly execute this until the second last post
            else:
                try:
                    like_post()                             # Press like button
                    press_next_button()                     # Press next button to like next post
                    time.sleep(2)
                except Exception:
                    press_next_button()                     # Press next button to like next post
                    time.sleep(2)


        # Last post use this
        else:
            try:
                like_post()
            except Exception:
                pass

    driver.get("https://www.instagram.com/")






# Comment on a post
def comment_first_post_in_profile(name="cl_ong0504", comment="Hello"):
    search_name(name)
    open_first_post_in_profile()                                             # Open first post
    time.sleep(2)   
    click_comment_section()                                                  # Click comment section
    type_text_in_comment_section(comment)                                    # Type text
    post_comment()
    driver.get("https://www.instagram.com/")




# Loop for comment all post
def comment_all_post(name="cl_ong0504", comment="Hello", random_comment=random_comment):
    search_name(name)
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span").text
    like_post_num = int(posts)
    try:
        open_first_post_in_profile()                                     # Open first post
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        open_first_post_in_profile()                                     # Open first post
        time.sleep(2)

    for i in range(like_post_num):
        # To get the whole process on the try (not in else, because in else block, we just need the last post)
        if i < like_post_num - 1:

            # It will execute this first (if no ban until the second last post)
            try:
                click_comment_section()                                                     # Click comment section
                type_text_in_comment_section(random.choice(random_comment))                 # Type random comment
                post_comment()                                                              # Post comment
                time.sleep(2)
                press_next_button()                                                         # Press next button to comment next post
                time.sleep(2)

            # When we get a ban, we need to wait
            except Exception:
                press_ok_in_ban()                                                           # Press ok             
                time.sleep(120)

                # Now wait is over, try to comment (test will get ban or not)
                try:
                    post_comment()                                                          # Post comment
                    time.sleep(2)
                    press_next_button()                                                     # Press next button to comment next post
                    time.sleep(2)

                # Get ban again, need to wait more time and finally comment
                except Exception:
                    post_comment()                                                          # Post comment
                    time.sleep(160)
                    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                    time.sleep(2)
                    press_next_button()                                                     # Press next button to comment next post
                    time.sleep(2)

        # The post to comment
        else:
            click_comment_section()                                                         # Click comment section
            type_text_in_comment_section(random.choice(random_comment))                     # Type random comment
            post_comment()                                                                  # Post comment
    driver.get("https://www.instagram.com/")






# Comment and spam a post in profile
def comment_spam_a_post_in_profile(name="cl_ong0504", spam_num=50, spam_msg = "You like spam"):
    search_name(name)
    try:
        open_first_post_in_profile()                                     # Open first post
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        open_first_post_in_profile()                                     # Open first post
        time.sleep(2)

    for i in range(spam_num):
        try:
            click_comment_section()                                      # Click comment section
            type_text_in_comment_section(spam_msg)                       # Spam comment
            post_comment()                                               # Post comment
            time.sleep(3)
        except Exception:
            press_ok_in_ban()                                            # Press ok            
            time.sleep(180)
            post_comment()                                               # Post comment
            time.sleep(3)
            click_comment_section()                                      # Click comment section  
            type_text_in_comment_section(spam_msg)                       # Spam comment
            post_comment()                                               # Post comment
            time.sleep(3)
    driver.get("https://www.instagram.com/")



# Comment and spam a post with link
def comment_spam_a_post(post="https://www.instagram.com/p/Cd7GH2Rr_fd/", spam_num=50, spam_msg="You like spam"):
    driver.get(post)
    time.sleep(3)
    for i in range(spam_num):
        try:
            click_comment_section()                                      # Click comment section
            type_text_in_comment_section(spam_msg)                       # Spam comment
            post_comment()                                               # Post comment
            time.sleep(3)
        except Exception:
            press_ok_in_ban()                                            # Press ok            
            time.sleep(180)
            post_comment()                                               # Post comment
            time.sleep(3)
            click_comment_section()                                      # Click comment section  
            type_text_in_comment_section(spam_msg)                       # Spam comment
            post_comment()                                               # Post comment
            time.sleep(3)

    driver.get("https://www.instagram.com/")




# Message a person
def message_a_person(msg_person="cl_ong0504", message="Hello!!"):
    click_send_message_button_in_home_page()                                      # Click message button in home page
    time.sleep(1)
    click_send_message_button()                                                   # Click send message button
    time.sleep(2)
    search_person_to_message(msg_person)                                          # Search the person
    time.sleep(2)

    select_the_person_to_message()                                                # Select the person
    click_next_button_to_message()                                                # Click next button
    time.sleep(3)

    type_message_to_send(message)                                                 # Type the message
    send_the_message()                                                            # Send the message
    driver.get("https://www.instagram.com/")




# Message and spam a person
def message_spam_a_person(msg_person="cl_ong0504", message="You like spam", spam_number=50):
    click_send_message_button_in_home_page()                                        # Click message button in home page
    time.sleep(1)
    click_send_message_button()                                                     # Click send message button
    time.sleep(2)
    search_person_to_message(msg_person)                                        # Search the person
    time.sleep(2)

    select_the_person_to_message()                                                  # Select the person
    click_next_button_to_message()                                                  # Click next button
    time.sleep(5)

    type_message_to_send(message)                                                   # Type the message
    send_the_message()                                                              # Send the message
    
    for i in range(spam_number):    
        type_message_to_send(message)                                               # Type the message
        send_the_message()                                                          # Send the message
    driver.get("https://www.instagram.com/")


# Message to many people
def message_to_many_people(message_list=target_list, message="Hello!!!"):
    click_send_message_button_in_home_page()                                      # Click message button in home page
    time.sleep(1)
    click_send_message_button()                                                   # Click send message button
    time.sleep(2)

    for i in message_list:
        search_person_to_message(i)                                               # Search the person
        time.sleep(3)
        select_the_person_to_message()                                            # Select the person
        
    click_next_button_to_message()                                                # Click next button
    time.sleep(5)

    type_message_to_send(message)                                                 # Type the message
    send_the_message()                                                            # Send the message

    driver.get("https://www.instagram.com/")



# Message and spam many people
def message_spam_many_people(message_list=target_list, message="Hello!!!", spam_number=50):
    click_send_message_button_in_home_page()                                        # Click message button in home page
    time.sleep(1)
    click_send_message_button()                                                     # Click send message button
    time.sleep(2)

    for i in message_list:
        search_person_to_message(i)                                                 # Search the person
        time.sleep(3)
        select_the_person_to_message()                                              # Select the person
        
    click_next_button_to_message()                                                  # Click next button
    time.sleep(5)

    type_message_to_send(message)                                                   # Type the message
    send_the_message()                                                              # Send the message

    # Spam message
    for i in range(spam_number):
        driver.find_element(by=By.XPATH, value="//*[@placeholder='Message...']").send_keys("hi")                            # Type the message
        send_the_message()                                                          # Send the message

    driver.get("https://www.instagram.com/")




# Get the list of following in specific amount
def get_following_list(name="cl_ong0504", num_of_following=100):
    search_name(name)


    following_list = []

    click_following_list()                  # click the following button to open the following list
    time.sleep(2)

    for i in range(num_of_following):
        try:
            username_tag = driver.find_element(by=By.XPATH, value="(//span[contains(@class,'_aap6 _aap7 _aap8')])["+str(i+1)+"]//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']/*")
            username = username_tag.get_attribute("innerHTML")

            if "<" in username:
                username = username.split("<")[0]

            following_list.append(username)
            scroll_following_list()
            time.sleep(5)
        except Exception:
            driver.refresh()

            username_tag = driver.find_element(by=By.XPATH, value="(//span[contains(@class,'_aap6 _aap7 _aap8')])["+str(i+1)+"]//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']/*")
            username = username_tag.get_attribute("innerHTML")

            if "<" in username:
                username = username.split("<")[0]

            following_list.append(username)

            scroll_following_list()
            time.sleep(5)

    print(following_list)
    driver.get("https://www.instagram.com/")







# Get the list of following 2
def get_following_list_2(name="cl_ong0504", num_of_following=100):
    search_name(name)
    time.sleep(1)
    click_following_list()
    time.sleep(2)


    for i in range((num_of_following // 12) + 7):
        scroll_following_list()
        time.sleep(3)

    following_list = []

    for i in range(num_of_following):
        try:
            try:
                username_tag = driver.find_element(by=By.XPATH, value="(//span[contains(@class,'_aap6 _aap7 _aap8')])["+str(i+1)+"]//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']/*")
                username = username_tag.get_attribute("innerHTML")

                if "<" in username:
                    username = username.split("<")[0]

                following_list.append(username)
                if i + 1 == num_of_following:
                    print(following_list)
                    print(len(following_list))
                    break
            except Exception:
                username_tag = driver.find_element(by=By.XPATH, value="(//span[contains(@class,'_aap6 _aap7 _aap8')])["+str(i+1)+"]//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']/*")
                username = username_tag.get_attribute("innerHTML")

                if "<" in username:
                    username = username.split("<")[0]

                following_list.append(username)
                if i + 1 == num_of_following:
                    print(following_list)
                    print(len(following_list))
                    break

        except Exception:
            value_followers = len(following_list)
            print(value_followers)
            print(following_list)
            break
    driver.get("https://www.instagram.com/")


# Get the list of following 3
# def get_following_list_3(name="cl_ong0504",num_of_following=100):
#     search_name(name)
#     driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/div").click()
#     time.sleep(2)
#
#
#     for i in range((num_of_following // 12) + 7):
#         scroll = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]")
#         scroll.click()
#         driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
#         time.sleep(3)
#
#     users = []
#
#     elements = driver.find_element(by=By.XPATH, value="//a[@class='notranslate _0imsa ']")
#
#     for element in elements:
#         if element.get_attribute('title') not in users:
#             users.append(element.get_attribute('title'))
#
#     for i in users:
#         if users.count(i) > 1:
#             users.remove(i)
#
#     print(users)
#     print(len(users))



# # Get the list of following in specific amount
# def get_following_list(name="cl_ong0504", num_of_following=100):
#     search_name(name)


#     following_list = []

#     driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div").click()
#     time.sleep(2)

#     for i in range(num_of_following):
#         try:
#             username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li["+str(i+1)+"]/div/div[1]/div[2]/div[1]/span/a/span").text
#             following_list.append(username)
#             scroll = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
#             scroll.click()
#             driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
#             time.sleep(5)
#         except Exception:
#             driver.refresh()
#             username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[" + str(i + 1) + "]/div/div[1]/div[2]/div[1]/span/a/span").text
#             following_list.append(username)
#             scroll = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]")
#             scroll.click()
#             driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
#             time.sleep(5)

#     driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()

#     print(following_list)
#     driver.get("https://www.instagram.com/")




def get_follower_list(name="cl_ong0504", num_of_follower=100):
    search_name(name)
    time.sleep(1)
    click_followers_list()
    time.sleep(2)


    for i in range((num_of_follower // 12) + 7):
        scroll_followers_list()
        time.sleep(3)

    follower_list = []

    for i in range(num_of_follower):
        try:
            try:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div["+str(i+1)+"]/div[2]/div[1]/div/div/div/span/a/span/div").text
                follower_list.append(username)
                if i + 1 == num_of_follower:
                    print(follower_list)
                    break
            except Exception:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div["+str(i+1)+"]/div[2]/div[1]/div/div/div/span/a/span/div").text
                follower_list.append(username)
                if i + 1 == num_of_follower:
                    print(follower_list)
                    break

        except Exception:
            value_followers = len(follower_list)
            print(value_followers)
            print(follower_list)
            break
    driver.get("https://www.instagram.com/")







# Get the like number of the post
def get_like_post_number(url="https://www.instagram.com/p/CdwNdmOs19F/"):
    driver.get(url)
    likers = []
    users = []
    time.sleep(2)
    try:
        driver.find_element(by=By.XPATH,value="//div[@class='_aacl _aaco _aacw _aacx _aada _aade']").click()
        time.sleep(2)
    except Exception:
        driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a[2]/div").click()
        time.sleep(2)

    for i in range(15):
        try:
            scroll_down = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div")
            scroll_down.click()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
        except:
            scroll_down = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div")
            scroll_down.click()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
        time.sleep(2)

        elements = driver.find_elements(by=By.XPATH, value="//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o _ab9s _abcm']/div/div/div")
        print(len(elements))
        
        for element in elements:
            if element.get_attribute('title') not in users:
                likers.append(element.get_attribute('title'))

        for element in elements:
            print(element.get_attribute('innerHTML'))

        time.sleep(1)


    for i in likers:
        if likers.count(i) > 1:
            likers.remove(i)

    print(len(likers))


    for i in likers:
        if likers.count(i) > 1:
            likers.remove(i)


    print(likers)
    print(len(likers))


    driver.get("https://www.instagram.com/")



# Get profile picture of a person
def get_profile_picture(name = "cl_ong0504"):
    search_name(name)
    time.sleep(1)
    try:
        image_element = driver.find_element(by=By.XPATH, value = "//*[contains(@alt,'Profile photo')]")
        image_link = image_element.get_attribute("src")
    except:
        image_element = driver.find_element(by=By.XPATH, value = '''//img[@alt="'''+ name +''''s profile picture"]''')
        image_link = image_element.get_attribute("src")
    print(image_link)
    driver.get("https://www.instagram.com/")



# Unfollow a person
def unfollow_a_person(name = "cl_ong0504"):
    search_name(name)
    press_follow_button()
    time.sleep(1)
    press_unfollow_button()

    driver.get("https://www.instagram.com/")



# Unfollow a list of person
def unfollow_many_people(target_list):
    for name in target_list:
        try:
            unfollow_a_person(name)
            time.sleep(2)
        except:
            time.sleep(300)
            unfollow_a_person(name)
            time.sleep(2)



mylist = driver.find_elements(by=By.XPATH, value='//img[contains(@alt,"Photo by")]')
print(len(mylist))


# def get_like_post_number_2(url="https://www.instagram.com/p/CdwNdmOs19F/"):
#     driver.get(url)
#     likers = []
#     users = []
#     try:
#         driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div[2]/div/a[2]/div").click()
#         time.sleep(2)
#     except Exception:
#         driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a[2]/div").click()
#         time.sleep(2)
#
#     for i in range(15):
#         scroll_down = driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div/div[3]/div")
#         scroll_down.click()
#         driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
#         time.sleep(2)
#
#         elements = driver.find_elements_by_xpath("//*[@id]/div/span/a")
#
#         for element in elements:
#             if element.get_attribute('title') not in users:
#                 likers.append(element.get_attribute('title'))
#         time.sleep(1)
#
#     for i in likers:
#         if likers.count(i) > 1:
#             likers.remove(i)
#
#     print(likers)
#     print(len(likers))
#     driver.get("https://www.instagram.com/")


# Run the function
# if __name__ == "__main__":
#     search_name()
#     profile_information()
#     click_next_picture()
#     follow_one_person()
#     follow_many_people()
#     like_first_post_in_profile()
#     like_all_post_in_profile()
#     comment_first_post_in_profile()
#     comment_all_post()
#     comment_spam_a_post_in_profile()
#     comment_spam_a_post()
#     message_a_person()
#     message_spam_a_person()
#     message_to_many_people()
#     message_spam_many_people()
#     get_following_list()
#     get_following_list_2()
#     get_follower_list()
#     get_like_post_number()



if __name__ == "__main__":
    print("All list should input as format : hello,hi,halo,ok\n")
    print("Please choose your mode : ")
    print("1. Default Mode \n2. Input Target Mode\n")
    choice_mode = int(input("Please enter (number 1 or 2) you want the mode you want to use: "))


    if choice_mode == 1:
        print("Welcome to Insta Script\n")

        login(username="jjdjdnfjwj", password="good123456#")
        driver.get("https://www.instagram.com/")
        try:
            while True:
                print(option)
                number = int(input("Please Enter Your Option: "))

                if number == 1:
                    # name = input("Enter username to search: ")
                    search_name()
                    print("\n")
                elif number == 2:
                    # name = input("Enter username to get information: ")
                    profile_information()
                    print("\n")
                elif number == 3:
                    click_next_picture()
                    print("\n")
                elif number == 4:
                    follow_one_person()
                    print("\n")
                elif number == 5:
                    follow_many_people()
                    print("\n")
                elif number == 6:
                    like_first_post_in_profile()
                    print("\n")
                elif number == 7:
                    like_all_post_in_profile()
                    print("\n")
                elif number == 8:
                    comment_first_post_in_profile()
                    print("\n")
                elif number == 9:
                    comment_all_post()
                    print("\n")
                elif number == 10:
                    comment_spam_a_post_in_profile()
                    print("\n")
                elif number == 11:
                    comment_spam_a_post()
                    print("\n")
                elif number == 12:
                    message_a_person()
                    print("\n")
                elif number == 13:
                    message_spam_a_person()
                    print("\n")
                elif number == 14:
                    message_to_many_people()
                    print("\n")
                elif number == 15:
                    message_spam_many_people()
                    print("\n")
                elif number == 16:
                    get_following_list()
                    print("\n")
                elif number == 17:
                    get_following_list_2()
                    print("\n")
                elif number == 18:
                    get_follower_list()
                    print("\n")
                elif number == 19:
                    get_like_post_number()
                    print("\n")
                elif number == 20:
                    print("\nThank You For Using This Script\nHave A Nice Day")
                    driver.close()
                    break

        except Exception:
            driver.get("https://www.instagram.com/")
            while True:
                print(option)
                number = int(input("Please Enter Your Option: "))

                if number == 1:
                    # name = input("Enter username to search: ")
                    search_name()
                    print("\n")
                elif number == 2:
                    # name = input("Enter username to get information: ")
                    profile_information()
                    print("\n")
                elif number == 3:
                    click_next_picture()
                    print("\n")
                elif number == 4:
                    follow_one_person()
                    print("\n")
                elif number == 5:
                    follow_many_people()
                    print("\n")
                elif number == 6:
                    like_first_post_in_profile()
                    print("\n")
                elif number == 7:
                    like_all_post_in_profile()
                    print("\n")
                elif number == 8:
                    comment_first_post_in_profile()
                    print("\n")
                elif number == 9:
                    comment_all_post()
                    print("\n")
                elif number == 10:
                    comment_spam_a_post_in_profile()
                    print("\n")
                elif number == 11:
                    comment_spam_a_post()
                    print("\n")
                elif number == 12:
                    message_a_person()
                    print("\n")
                elif number == 13:
                    message_spam_a_person()
                    print("\n")
                elif number == 14:
                    message_to_many_people()
                    print("\n")
                elif number == 15:
                    message_spam_many_people()
                    print("\n")
                elif number == 16:
                    get_following_list()
                    print("\n")
                elif number == 17:
                    get_following_list_2()
                    print("\n")
                elif number == 18:
                    get_follower_list()
                    print("\n")
                elif number == 19:
                    get_like_post_number()
                    print("\n")
                elif number == 20:
                    print("\nThank You For Using This Script\nHave A Nice Day")
                    driver.close()
                    break


    elif choice_mode == 2:
        print("Welcome to Insta Script\n")
        # username = input("Enter username: ")
        # password = input("Enter password: ")
        # login(username= username, password=password)
        login(username="jjdjdnfjwj", password="good123456#")
        driver.get("https://www.instagram.com/")
        try:
            while True:
                print(option)
                number = int(input("Please Enter Your Option: "))

                if number == 1:
                    name = input("Enter username to search: ")
                    search_name(name)
                    print("\n")
                elif number == 2:
                    name = input("Enter a username to get information: ")
                    profile_information(name)
                    print("\n")
                elif number == 3:
                    name = input("Enter a username to get picture and next: ")
                    click_next_picture(name)
                    print("\n")
                elif number == 4:
                    name = input("Enter a username to follow: ")
                    follow_one_person(name)
                    print("\n")
                elif number == 5:
                    name_list = input("Enter a list of username to follow: ").strip().split(",")
                    follow_many_people(name_list)
                    print("\n")
                elif number == 6:
                    name = input("Enter a username to like first post: ")
                    like_first_post_in_profile(name)
                    print("\n")
                elif number == 7:
                    name = input("Enter a username to like all post: ")
                    like_all_post_in_profile(name)
                    print("\n")
                elif number == 8:
                    name = input("Enter a username to comment first post: ")
                    comment = input("Enter your comment message: ")
                    comment_first_post_in_profile(name, comment)
                    print("\n")
                elif number == 9:
                    name = input("Enter a username to comment first post: ")
                    comment = input("Enter your comment message: ")
                    comment_list = input("Enter a list of random spam message: ")
                    comment_all_post(name, comment, comment_list)
                    print("\n")
                elif number == 10:
                    name = input("Enter username to comment and spam a post: ")
                    spam_num = int(input("Enter spam comment number: "))
                    comment = input("Enter your comment spam message: ")
                    comment_spam_a_post_in_profile(name, spam_num, comment)
                    print("\n")
                elif number == 11:
                    link = input("Enter a link post to comment and spam: ")
                    spam_num = int(input("Enter spam comment number: "))
                    comment = input("Enter your comment spam message: ")
                    comment_spam_a_post(link, spam_num, comment)
                    print("\n")
                elif number == 12:
                    name = input("Enter a username to message: ")
                    message = input("Enter a message: ")
                    message_a_person(name, message)
                    driver.get("https://www.instagram.com/")
                    print("\n")
                elif number == 13:
                    name = input("Enter a username to message and spam: ")
                    message = input("Enter a spam message: ")
                    spam_num = int(input("Enter spam message number: "))
                    message_spam_a_person(name, message, spam_num)
                    print("\n")
                elif number == 14:
                    name_list = input("Enter a list of username to message: ").strip().split(",")
                    message = input("Enter a message: ")
                    message_to_many_people(name_list, message)
                    driver.get("https://www.instagram.com/")
                    print("\n")
                elif number == 15:
                    name_list = input("Enter a list of username to message and spam: ").strip().split(",")
                    message = input("Enter a spam message: ")
                    spam_num = int(input("Enter spam message number: "))
                    message_spam_many_people(name_list, message, spam_num)
                    print("\n")
                elif number == 16:
                    name = input("Enter a username to get following list: ")
                    num_of_following = int(input("Enter number of following list you want: "))
                    get_following_list(name, num_of_following)
                    print("\n")
                elif number == 17:
                    name = input("Enter a username to get following list: ")
                    num_of_following = int(input("Enter number of following list you want: "))
                    get_following_list_2(name, num_of_following)
                    print("\n")
                elif number == 18:
                    name = input("Enter a username to get followers list: ")
                    num_of_followers = int(input("Enter number of followers list you want: "))
                    get_follower_list(name, num_of_followers)
                    print("\n")
                elif number == 19:
                    link = input("Enter a post link to get like number: ")
                    get_like_post_number(link)
                    print("\n")
                elif number == 20:
                    print("\nThank You For Using This Script\nHave A Nice Day")
                    driver.close()
                    break
        except Exception:
            driver.get("https://www.instagram.com/")
            while True:
                print(option)
                number = int(input("Please Enter Your Option: "))

                if number == 1:
                    name = input("Enter username to search: ")
                    search_name(name)
                    print("\n")
                elif number == 2:
                    name = input("Enter a username to get information: ")
                    profile_information(name)
                    print("\n")
                elif number == 3:
                    name = input("Enter a username to get picture and next: ")
                    click_next_picture(name)
                    print("\n")
                elif number == 4:
                    name = input("Enter a username to follow: ")
                    follow_one_person(name)
                    print("\n")
                elif number == 5:
                    name_list = input("Enter a list of username to get information: ")
                    follow_many_people(name_list)
                    print("\n")
                elif number == 6:
                    name = input("Enter a username to like first post: ")
                    like_first_post_in_profile(name)
                    print("\n")
                elif number == 7:
                    name = input("Enter a username to like all post: ")
                    like_all_post_in_profile(name)
                    print("\n")
                elif number == 8:
                    name = input("Enter a username to comment first post: ")
                    comment = input("Enter your comment message: ")
                    comment_first_post_in_profile(name, comment)
                    print("\n")
                elif number == 9:
                    name = input("Enter a username to comment first post: ")
                    comment = input("Enter your comment message: ")
                    comment_list = input("Enter a list of random spam message: ")
                    comment_all_post(name, comment, comment_list)
                    print("\n")
                elif number == 10:
                    name = input("Enter username to comment and spam a post: ")
                    spam_num = int(input("Enter spam comment number: "))
                    comment = input("Enter your comment spam message: ")
                    comment_spam_a_post_in_profile(name, spam_num, comment)
                    print("\n")
                elif number == 11:
                    link = input("Enter a link post to comment and spam: ")
                    spam_num = int(input("Enter spam comment number: "))
                    comment = input("Enter your comment spam message: ")
                    comment_spam_a_post(link, spam_num, comment)
                    print("\n")
                elif number == 12:
                    name = input("Enter a username to message: ")
                    message = input("Enter a message: ")
                    message_a_person(name, message)
                    driver.get("https://www.instagram.com/")
                    print("\n")
                elif number == 13:
                    name = input("Enter a username to message and spam: ")
                    message = input("Enter a spam message: ")
                    spam_num = int(input("Enter spam message number: "))
                    message_spam_a_person(name, message, spam_num)
                    print("\n")
                elif number == 14:
                    name_list = input("Enter a list of username to message: ")
                    message = input("Enter a message: ")
                    message_to_many_people(name_list, message)
                    driver.get("https://www.instagram.com/")
                    print("\n")
                elif number == 15:
                    name_list = input("Enter a list of username to message and spam: ")
                    message = input("Enter a spam message: ")
                    spam_num = int(input("Enter spam message number: "))
                    message_spam_many_people(name_list, message, spam_num)
                    print("\n")
                elif number == 16:
                    name = input("Enter a username to get following list: ")
                    num_of_following = int(input("Enter number of following list you want: "))
                    get_following_list(name, num_of_following)
                    print("\n")
                elif number == 17:
                    name = input("Enter a username to get following list: ")
                    num_of_following = int(input("Enter number of following list you want: "))
                    get_following_list_2(name, num_of_following)
                    print("\n")
                elif number == 18:
                    name = input("Enter a username to get followers list: ")
                    num_of_followers = int(input("Enter number of followers list you want: "))
                    get_follower_list(name, num_of_followers)
                    print("\n")
                elif number == 19:
                    link = input("Enter a post link to get like number: ")
                    get_like_post_number(link)
                    print("\n")
                elif number == 20:
                    print("\nThank You For Using This Script\nHave A Nice Day")
                    driver.close()
                    break




