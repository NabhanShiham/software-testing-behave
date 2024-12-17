from selenium.webdriver.common.by import By


class Homepage:
    PAGE_URL = "https://www.saucedemo.com/"

    text_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password"),
        "First Name": (By.ID, "first-name"),
        "Last Name": (By.ID, "last-name"),
        "Zip Code": (By.ID, "postal-code")
    }

    navigation_buttons = {
        "Login": (By.ID, "login-button"),
        "Checkout": (By.ID, "checkout"),
        "Continue": (By.ID, "continue"),
        "Cart": (By.CLASS_NAME, "shopping_cart_link"),
        "Options": (By.ID, "react-burger-menu-btn"),
        "About": (By.ID, "about_sidebar_link"),
        "Logout": (By.ID, "logout_sidebar_link"),
        "Reset": (By.ID, "reset_sidebar_link"),
        "Close": (By.ID, "react-burger-cross-btn"),
        "Continue Shopping": (By.ID, "continue-shopping"),
        "Finish": (By.ID, "finish"),
        "Back Home": (By.ID, "back-to-products"),
        "Filter": (By.CLASS_NAME, "product_sort_container"),
        "Cancel": (By.ID, "cancel")
    }

    messages = {
        "login error": (
            By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3"),
        "price label": (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > "
                                         "div.summary_total_label"),
        "checkout error": (By.CSS_SELECTOR, "#checkout_info_container > div > form > div > "
                                            "div.error-message-container.error > h3")
    }

    item_buttons = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    }

    remove = {
        "Sauce Labs Backpack": (By.ID, "remove-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "remove-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "remove-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "remove-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "remove-sauce-labs-onesie"),
        "Test.allTheThings() T-Shirt (Red)": (By.ID, "remove-test.allthethings()-t-shirt-(red)")
    }

    socials = {
        "Facebook": (By.CSS_SELECTOR, "ul.social li.social_facebook"),
        "Twitter": (By.CSS_SELECTOR, "ul.social li.social_twitter"),
        "LinkedIn": (By.CSS_SELECTOR, "ul.social li.social_linkedin")
    }

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def close_page(self):
        self.driver.quit()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def click_button(self, button):
        self.driver.find_element(*self.navigation_buttons[button]).click()

    def get_error_message(self):
        return self.driver.find_element(*self.messages["login error"]).text

    def get_checkout_error(self):
        return self.driver.find_element(*self.messages["checkout error"]).text

    def add_to_cart(self, item):
        self.driver.find_element(*self.item_buttons[item]).click()

    def get_total(self):
        return self.driver.priceLabel.text

    def cart_is_empty(self):
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
        return len(cart_items) == 0

    def remove_from_cart(self, product):
        self.driver.find_element(*self.remove[product]).click()

    def total(self):
        return self.driver.find_element(*self.messages["price label"]).text

    def get_products_page(self):
        return self.driver.get(self.PAGE_URL + "inventory.html")

    def cart_contains(self):
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
        return len(cart_items)

    def select_filter(self, filter_by):
        self.driver.find_element(*self.navigation_buttons["Filter"]).click()
        self.driver.find_element(By.XPATH, f'//option[@value="{filter_by}"]').click()

    def get_first_product(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".inventory_list:first-child").text.split("\n")[0]

    def click_social_network_button(self, sns):
        self.driver.find_element(*self.socials[sns]).click()

    def get_current_url(self):
        return self.driver.current_url
