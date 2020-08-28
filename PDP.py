from appium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.remote.command import Command

driver = webdriver.Remote(
   command_executor="http://localhost:4723/wd/hub",

desired_capabilities = {
    "deviceName": "iPhone 11 Pro",
    "platformName": "IOS",
    "platformVersion": "13.3",
    #"automationName": "XCUITest",
    "browserName": "Safari",

})


driver.get("https://dev-www.zoro.com/louisville-extension-ladder-fiberglass-24-ft-ia-fe3224/i/G3499955/")
driver.implicitly_wait(10)

     #Tap on the image on PDP   DONE
#
# driver.execute_script("window.scrollTo(0,400)")
# image = driver.find_element_by_css_selector("[data-za='product-images_hover-zoom']")
# action = TouchActions(driver)
# action.tap(image).perform()
# driver.find_element_by_css_selector("[data-za='product-images-modal-close']").is_displayed()
# driver.quit()




      #Zoom In and Zoom out on PDP  DONE
# driver.execute_script('document.body.style.zoom = "1.5"')



     #Tap on the dots under the image  DONE
# driver.execute_script("window.scrollTo(0,600)")
# action = TouchActions(driver)
# second_circle = driver.find_element_by_id("slick-slide11")
# action.tap(second_circle).perform()
# third_circle = driver.find_element_by_id("slick-slide12")
# action.tap(third_circle).perform()



    #Jump Links ( click and scroll down, scroll up and click again)  (visual bugs, misaligned)
# driver.execute_script("window.scrollTo(0,1600)")



    #Tap on quantity box (adjust the amount, click on -/+ and add to cart)    DONE
# driver.execute_script("window.scrollTo(0,900)")
# quantity_input = driver.find_element_by_css_selector("[data-za='quantity-input']")
# action = TouchActions(driver)
# action.tap(quantity_input).perform()
# quantity_input.clear().send_keys(10)
# increment_button = driver.find_element_by_css_selector("[data-za='incrementer-plus-btn']")
# action.tap(increment_button).perform()
# increment_minus_button = driver.find_element_by_css_selector("[data-za='incrementer-minus-btn']")
# action.tap(increment_minus_button).perform()
# add_to_cart = driver.find_element_by_css_selector("[data-za='add-to-cart']")
# action.tap(add_to_cart).perform()
# driver.implicitly_wait(5)
# driver.find_element_by_css_selector("[data-za='flyout-cart-body']").is_displayed()




    #Tap on dots under the recommendation carousel


# driver.execute_script("window.scrollTo(0,1600)")
# action = TouchActions(driver)
# second_circle = driver.find_element_by_id("slick-slide25")
# action.tap(second_circle).perform()
# third_circle = driver.find_element_by_id("slick-slide28")
# action.tap(third_circle).perform()


                                      #
