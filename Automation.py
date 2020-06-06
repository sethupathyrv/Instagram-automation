from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Username=input("Enter your username:")
Password=input("Enter your password:")
FrndUsername=input("Enter the username of the person you have to message to:")

def ReadOldMessage():
    try:
        uueGX = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "uueGX"))
                )
        n=1
        lastText=[]
        print(uueGX.text)
        while(uueGX.text[-n]!='\n'):
            lastText.insert(0,uueGX.text[-n])
            n+=1        
    
    finally:
        print("\n")

    LatestMessage=""
    LatestMessage=LatestMessage.join(lastText)
    print("From my new joining string,the latest Message is -",LatestMessage,"\n")
    return LatestMessage


def SendToBot_DmBotReply():
    clickthere.send_keys(LatestMessage)
    botbut=bot.find_element_by_xpath('//*[@id="btnSay"]').click()
    sleep(5)
    try:
        reply = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.ID, "answer_0"))
                )
        print(reply.text)
    
    finally:
        print('\n')


    test_str = reply.text
    BotReplied = "" 
  
    for i in range(len(test_str)): 
        if i >= 6: 
            BotReplied = BotReplied + test_str[i] 
    print("Bot replied",BotReplied)


    sleep(2)
    typehere=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    typehere.send_keys(BotReplied)
    send=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    return BotReplied

def ForBotMem():
    try:
        reply = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.ID, "answer_0"))
                )
        print(reply.text)
    
    finally:
        print('\n')


    test_str = reply.text
    BotReplied = "" 
  
    for i in range(len(test_str)): 
        if i >= 6: 
            BotReplied = BotReplied + test_str[i] 
            
    print("\nIn bot memory",BotReplied)


    sleep(2)

    return BotReplied
    

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
sleep(2)
username=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
username.send_keys(Username)
password=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys(Password)
loginbutton=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
sleep(3)
notnowbutton=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
sleep(2)
nonotif=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
sleep(2)

dmbutton=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div').click()
sleep(3)
clkmsg=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
sleep(2)
sermsg=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input').send_keys('FrndUsername')
sleep(2)
tick=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/div/div[3]/button/span').click()
sleep(2)
copy=driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button').click()
sleep(2)

bot=webdriver.Chrome()
bot.get('http://p-bot.ru/en/index.html')
sleep(2)
clickthere=bot.find_element_by_xpath('//*[@id="user_request"]')
clickthere.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
#clickthere.send_keys(ReturnLatestReply())
#botbut=bot.find_element_by_xpath('//*[@id="btnSay"]').click()
#sleep(5)



for i in range(0,30):
    LatestMessage=ReadOldMessage()
    if i==0:
        BotMemory='jj'
    else:
        BotMemory=ForBotMem()
    if LatestMessage =='Seen':
        print("Sleeping for next 20 seconds-They seenzoned us so")
        sleep(20)
        pass
    else:
        if LatestMessage==BotMemory :
            print("\nWill sleep for next 20 sec cuz They didn't reply")
            sleep(20)
            pass

        else:
            SendToBot_DmBotReply()
            print("Message sent and waiting for reply - sleeping for 20 seconds")
            sleep(20)
            pass
    
    


