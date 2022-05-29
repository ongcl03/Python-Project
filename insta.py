# Program     :  INSTA SCRIPT
# Author      :  ONG CHANG LE
# Email       :  websitecl03@gmail.com
# Start Date  :  25/4/2022
# Update Date :  27/05/2022


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








# login
def login(username="your_username", password="your_password"):
    search = driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[1]/div/label/input")
    search.send_keys(username)

    search = driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[2]/div/label/input")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/div/div/div/button").click()
    time.sleep(2)
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except Exception:
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
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(name)
        time.sleep(5)

    # Click profile
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div").click()
        time.sleep(5)
    except Exception:
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(name)
        time.sleep(10)

        # Click profile
        driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div").click()
        time.sleep(3)



# Print out the follower information
def profile_information(name="cl_ong0504"):
    search_name(name)
    try:
        posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span").text
        followers = driver.find_element(by=By.XPATH,value="/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").text
        following = driver.find_element(by=By.XPATH,value="/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text
    except Exception:
        posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span").text
        followers = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[2]/div/span").text
        following = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[3]/div/span").text


    print(f"Posts number : {posts} \nFollowers number : {followers} \nFollowing number : {following}")
    driver.get("https://www.instagram.com/")


# Next picture
def click_next_picture(name="cl_ong0504"):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
    driver.get("https://www.instagram.com/")



# Follow a user
def follow_one_person(name="cl_ong0504"):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//div[@class='_7UhW9   xLCgt        qyrsm            uL8Hv        T0kll ']").click()
    driver.get("https://www.instagram.com/")


# Loop the list to follow
def follow_many_people(following_list=target_list):
    for i in range(len(following_list)):
        if i != 0 and i % 10 == 0:
            time.sleep(120)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(following_list[i])
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//div[@class='_7UhW9   xLCgt        qyrsm            uL8Hv        T0kll ']").click()
            driver.get("https://www.instagram.com/")
        else:
            driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(following_list[i])
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//div[@class='_7UhW9   xLCgt        qyrsm            uL8Hv        T0kll ']").click()
            driver.get("https://www.instagram.com/")
    driver.get("https://www.instagram.com/")


# Like a post
def like_first_post_in_profile(name="cl_ong0504"):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
    driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/button").click()
    driver.get("https://www.instagram.com/")


# Loop for like all post
def like_all_post_in_profile(name="cl_ong0504"):
    search_name(name)
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span").text
    like_post_num = int(posts)
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()

    for i in range(like_post_num):
        if i < like_post_num-1:
            if i != 0 and i % 50 == 0:

                try:
                    time.sleep(100)
                    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)
                except Exception:
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)

            else:
                try:
                    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)
                except Exception:
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)

        else:
            try:
                driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/button").click()
            except Exception:
                driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/button").click()

    print(driver.find_element(by=By.XPATH, value="//li[@class='Y8-fY ']//*[span[@class='g47SY ']]").text)
    driver.get("https://www.instagram.com/")






# Comment on a post
def comment_first_post_in_profile(name="cl_ong0504", comment="Hello"):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//div[@class='RxpZH']").click()
    driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(comment)
    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
    driver.get("https://www.instagram.com/")



# Loop for comment all post
def comment_all_post(name="cl_ong0504", comment="Hello", random_comment=random_comment):
    search_name(name)
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
        time.sleep(2)

    for i in range(11):
        if i < 10:
            try:
                driver.find_element(by=By.XPATH, value="//div[@class='RxpZH']").click()
                driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(random.choice(random_comment))
                driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                time.sleep(2)
                driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                time.sleep(2)
            except Exception:
                driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div/div/div[2]/button[2]").click()
                time.sleep(120)
                try:
                    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                    time.sleep(2)
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)
                except Exception:
                    driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div/div/div[2]/button[2]").click()
                    time.sleep(160)
                    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                    time.sleep(2)
                    driver.find_element(by=By.XPATH, value="//button[@class='wpO6b  ']//*[@aria-label='Next']").click()
                    time.sleep(2)

        else:
            driver.find_element(by=By.XPATH, value="//div[@class='RxpZH']").click()
            driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(random.choice(random_comment))
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/button").click()
    driver.get("https://www.instagram.com/")


# Comment and spam a post in profile
def comment_spam_a_post_in_profile(name="cl_ong0504", spam_num=50, spam_msg = "You like spam"):
    search_name(name)
    try:
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//div[@class='eLAPa']").click()
        time.sleep(2)

    for i in range(spam_num):
        try:
            driver.find_element(by=By.XPATH, value="//div[@class='RxpZH']").click()
            driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(spam_msg)
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
        except Exception:
            driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div/div/div[2]/button[2]").click()
            time.sleep(180)
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(spam_msg)
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
    driver.get("https://www.instagram.com/")



# Comment and spam a post with link
def comment_spam_a_post(post="https://www.instagram.com/p/Cd7GH2Rr_fd/", spam_num=50, spam_msg="You like spam"):
    driver.get(post)
    for i in range(spam_num):
        try:
            driver.find_element(by=By.XPATH, value="//div[@class='RxpZH']").click()
            driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(spam_msg)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
        except Exception:
            driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]/button[2]").click()
            time.sleep(180)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").send_keys(spam_msg)
            driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
            time.sleep(3)
    driver.get("https://www.instagram.com/")




# Message a person
def message_a_person(msg_person="cl_ong0504", message="Hello!!"):
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[1]/div/div[3]/div/div[2]/a").click()
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input").send_keys(msg_person)
    time.sleep(2)

    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[2]").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[1]/div/div[3]/div/button").click()
    time.sleep(3)

    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()



# Message and spam a person
def message_spam_a_person(msg_person="cl_ong0504", message="You like spam", spam_number=50):
    message_a_person(msg_person, message="Hello!!")
    for i in range(spam_number):
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
    driver.get("https://www.instagram.com/")

# Message to many people
def message_to_many_people(message_list=target_list, message="Hello!!!"):
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[1]/div/div[3]/div/div[2]/a").click()
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
    time.sleep(2)

    for i in message_list:
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input").send_keys(i)
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[2]").click()

    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[1]/div/div[3]/div/button").click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()

    # driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/article/div[2]/div[2]/div/p/a/span").click()




    # input_mail = driver.find_element(by=By.XPATH, value="//input[@aria-label='Mobile Number or Email']")
    # input_mail.click()
    # input_mail.send_keys("p")

    # driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()




# Message and spam many people
def message_spam_many_people(message_list=target_list, message="You Like Spam", spam_number=50):
    message_to_many_people(message_list=message_list, message=message)
    time.sleep(2)

    for i in range(spam_number):
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()

    driver.get("https://www.instagram.com/")




# Get the list of following in specific amount
def get_following_list(name="cl_ong0504", num_of_following=100):
    search_name(name)


    following_list = []

    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/div").click()
    time.sleep(2)

    for i in range(num_of_following):
        try:
            username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]/ul/div/li[" + str(i + 1) + "]/div/div[1]/div[2]/div[1]/span/a").text
            following_list.append(username)
            scroll = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]")
            scroll.click()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(5)
        except Exception:
            username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]/ul/div/li[" + str(i + 1) + "]/div/div[2]/div[1]/div/div/span/a").text
            following_list.append(username)
            scroll = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]")
            scroll.click()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(5)

    driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()

    print(following_list)
    driver.get("https://www.instagram.com/")


# Get the list of following 2
def get_following_list_2(name="cl_ong0504", num_of_following=100):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/div").click()
    time.sleep(2)


    for i in range((num_of_following // 12) + 7):
        scroll = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]")
        scroll.click()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
        time.sleep(3)

    following_list = []

    for i in range(num_of_following):
        try:
            try:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]/ul/div/li[" + str(
                    i + 1) + "]/div/div[1]/div[2]/div[1]/span/a").text
                following_list.append(username)
                if i + 1 == num_of_following:
                    print(following_list)
                    break
            except Exception:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]/ul/div/li[" + str(
                    i + 1) + "]/div/div[2]/div[1]/div/div/span/a").text
                following_list.append(username)
                if i + 1 == num_of_following:
                    print(following_list)
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






def get_follower_list(name="cl_ong0504", num_of_follower=100):
    search_name(name)
    driver.find_element(by=By.XPATH, value="//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()
    time.sleep(2)


    for i in range((num_of_follower // 12) + 7):
        scroll = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")
        scroll.click()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
        time.sleep(3)

    follower_list = []

    for i in range(num_of_follower):
        try:
            try:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]/ul/div/li[" + str(
                    i + 1) + "]/div/div[1]/div[2]/div[1]/span/a").text
                follower_list.append(username)
                if i + 1 == num_of_follower:
                    print(follower_list)
                    break
            except Exception:
                username = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]/ul/div/li[" + str(
                    i + 1) + "]/div/div[2]/div[1]/div/div/span/a").text
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
    try:
        driver.find_element(by=By.XPATH,value="//*[@id='react-root']/section/main/div/div/article/div/div[2]/div/div[2]/section[2]/div/div/div/a[2]/div").click()
        time.sleep(2)
    except Exception:
        driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a[2]/div").click()
        time.sleep(2)

    for i in range(15):
        scroll_down = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div[3]/div")
        scroll_down.click()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
        time.sleep(2)

        elements = driver.find_elements_by_xpath("//*[@id]/div/span/a")

        for element in elements:
            if element.get_attribute('title') not in users:
                likers.append(element.get_attribute('title'))

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

        login(username="your_username", password="your_password")
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
        login(username="your_username", password="your_password")
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




