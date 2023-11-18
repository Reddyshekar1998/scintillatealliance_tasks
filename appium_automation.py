from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from PIL import Image
from io import BytesIO
from appium.webdriver.common.touch_action import TouchAction

# Mention path of flipkart.apk in capabilities
# Change the your deviceName in capabilities
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app='/home/reddy/Android/Sdk/platform-tools/flipkart1.apk',
    appPackage='com.flipkart.android',
    appActivity='.activity.HomeFragmentHolderActivity',
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, capabilities)
driver.implicitly_wait(50)
try:
# Click on Login Skip button
    Skip_button = driver.find_element(by=AppiumBy.ID,value='com.flipkart.android:id/custom_back_icon').click()
except Exception:
    pass
driver.implicitly_wait(30)
search = driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.FrameLayout[@resource-id="com.flipkart.android:id/main_content"])[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]').click()
# Waiting to load the element because android studio emulator slowing down my laptop
time.sleep(5)
send_key = driver.find_element(by=AppiumBy.CLASS_NAME,value='android.widget.EditText')
send_key.send_keys('Hindi books')
time.sleep(5)
click_on_books = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]').click()
time.sleep(5)
try:
    not_now_button = driver.find_element(by=AppiumBy.ID, value='com.flipkart.android:id/not_now_button').click()
    time.sleep(5)
    not_now_again = driver.find_element(by=AppiumBy.ID, value='com.flipkart.android:id/not_now_button').click()
except Exception:
    pass
driver.implicitly_wait(10)
# Scrolling down the hindi books
for scroll in range(20):
    for i,screen_shot in enumerate(driver.find_elements(by=AppiumBy.XPATH,value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')):
        screen_shot_element = screen_shot.screenshot_as_png
        image = Image.open(BytesIO(screen_shot_element))
        image.save(f'screen_shots/screenshot_{i+1}{scroll}.png')
        scroll_action = TouchAction(driver)
        scroll_action.press(x=508, y=1952).move_to(x=526, y=784).release().perform()
driver.quit()