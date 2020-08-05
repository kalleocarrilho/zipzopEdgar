from selenium import webdriver
from datetime import datetime   
import time

class WhatsappBot:
    def __init__(self):
        self.message = " (FIGURINHA DO EDGAR) "
        self.grupo = ["Time Monditech"]
        #self.grupos = ["teste"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessage(self):
        #<span dir="auto" title="teste" class="_3ko75 _5h6Y_ _3Whw5">teste</span>
        #<div tabindex="-1" class="_3uMse">
        #<div class="_1JNuk">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            time.sleep(1)
            teste = 0
            while(teste == 0):
                time.sleep(5)
                nome = self.driver.find_elements_by_xpath(f"//span[contains(@class, 'FMlAw') and contains(@class, ' ') and contains(@class, '_3Whw5')]")[-1].text
                attr = self.driver.find_elements_by_xpath(f"//div[contains(@class, '_11PeL') and contains(@class, 'copyable-text')]")[-1].get_attribute('data-pre-plain-text')
                print(attr)
                attr = attr.replace('[','')
                attr = attr.replace(']','')
                print(attr.split(',')[0])
                now = datetime.now()

                current_time = now.strftime("%H:%M")
                print("Current Time =", current_time)

                teste = 1
                
                if(nome == 'Edgar Meante' and currrent_time != attr):
                    chat_box = self.driver.find_element_by_class_name('_3uMse')
                    print('AAA---111')
                    time.sleep(1)
                    print('AAA---222')
                    
                    print('AAA---222---111')
                    chat_box.click()
                    print('AAA---333')
                    chat_box.send_keys(self.message)
                    sendButton = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(1)
                    #sendButton.click()
                    time.sleep(1)
                    teste = 1

            
bot = WhatsappBot()
bot.SendMessage()
        

        