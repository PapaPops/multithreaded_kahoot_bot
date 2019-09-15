import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys as system
from random import randint as rand



class kahootBotInstance:
    """
        threaded bot class for interacting with live kahoot quizzes working with selenium
    """

    def __init__(self):
        options = Options()
        options.headless = True

        self.driver = webdriver.Chrome(options= options, executable_path="./driver-container/chromedriver")
        self.driver.implicitly_wait(10)


    @staticmethod
    def make_name() -> str:
        name = ""

        alphabet = "abcdefghijklmnopqrstvuwxyz0123456789"
        
        length = rand(4,10)

        for _ in range(length):
            name += alphabet[rand(0,len(alphabet)-1)]

        return name
    

    
    @staticmethod
    def make_specialized_name(name : str) -> str:

        name = list(name)
        new_name = ""
        
        for i in range(len(name)):
            if rand(1,3) == 2:
                name[i] = name[i].upper()
        
        for i in range(len(name)):
            new_name += name[i]
            if rand(1,4) == 4:
                new_name += " "

        return new_name

        


    def __login(self, code : int, name : str = None):

        if name is None:
            self.name = kahootBotInstance.make_name()
        else:
            self.name = name

        try:
            self.driver.get("https://kahoot.it/")
            code_input = self.driver.find_element_by_css_selector("#game-input")
            code_input.send_keys(str(code))
            code_input.send_keys(Keys.ENTER)

            print(f"entered code for {self.name}")

            name_input = self.driver.find_element_by_css_selector("#nickname")
            name_input.send_keys(self.name)
            name_input.send_keys(Keys.ENTER)

            print(f"entered nickname for {self.name}")

        except:

            print(f"something went wrong while trying to login with bot : {self.name}")
        
        finally:

            if self.get_website() == "https://kahoot.it/v2":

                print(f"something went wrong while trying to log {self.name} on /(wrong pin)/")

                return

        

    def __aq(self,answer : int = 0):
        
        buttons = self.driver.find_elements_by_tag_name("button")
        buttons[answer].click()
        


    def login(self,code : int, name : str = None):
        """
            code : login code for the bot to join a game
            name (optional else randomized) : optional name for the bot to take as nickname in game
        """
        thread = threading.Thread(target=self.__login, args =(code,name))
        thread.start()

    def answer_question(self,answer : int = 0):
        """
        answer : 0 - red , 1 - blue , 2 - yellow , 3 - green
        """
        if answer < 0 or answer > 3:
            return

        if self.get_website() != "https://kahoot.it/v2/gameblock":
            #print(f"{self.name} couldn't answer the current question since the answer page hasn't loaded")
            return


        thread = threading.Thread(target = self.__aq, args = (answer,))
        thread.start()


    def get_website(self):
        return self.driver.current_url



    def close(self):
        """
        closes the current instance of the driver belonging to the bot
        """
        print(f"deleted {self.name}")

        self.driver.close()
    
if __name__ == "__main__":
    print("cannot run file as main")