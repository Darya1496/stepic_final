from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")

    SUCSESS_ADD_BOOK = (By.XPATH, "//*[@id='messages']/div[2]/div") #Уведомление об успешном добавлении книги в корзину
    NAME_BOOK_ON_PAGE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1") #Название книги на странице
    NAME_ADD_BOOK = (By.XPATH,"//*[@id='messages']/div[1]/div/strong") #Название добавленной в корзину книги из уведомления

    PRICE_PRODUCT = (By.XPATH, "//p[@class='price_color']") #Цена книги на странице добавления
    PRICE_ALLERT = (By.XPATH, "//div[@class='alertinner ']/p/strong") #Сумма в уведомлении


