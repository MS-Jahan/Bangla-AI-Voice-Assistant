import undetected_chromedriver as uc
import json
import pathlib
import time

# create a selenium function that will open google bard using undetected chrome driver and dump all cookies to a file
def get_cookies():
    # save browser cache to a folder
    script_directory = pathlib.Path().absolute()
    # open google bard
    driver = uc.Chrome(user_data_dir=f"{script_directory}\\userdata".replace("\\", "/"), headless=True)
    driver.get("https://bard.google.com")
    time.sleep(100)
    # dump all cookies to a json file
    with open('cookies.json', 'w') as fp:
        json.dump(driver.get_cookies(), fp, indent=4)
    
    try:
        driver.close()
        driver.quit()
    except Exception as e:
        print("Error: ", e)
    
    Secure_1PSID, Secure_1PSIDTS = '', ''
    # return Secure_1PSID and Secure_1PSIDTS cookies value
    with open('cookies.json', 'r') as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            if cookie['name'] == '__Secure-1PSID':
                Secure_1PSID = cookie['value']
            elif cookie['name'] == '__Secure-1PSIDTS':
                Secure_1PSIDTS = cookie['value']
    return Secure_1PSID, Secure_1PSIDTS

if __name__ == "__main__":
    print(get_cookies())



'''
From voice: ইনস্টিটিউট অফ সাইন্স এন্ড টেকনোলজি বাংলাদেশ সম্পর্কে তুমি যা জানো তা বল মাইক তোর ভালো থাকার কথা
api: হ্যালো মাইক,

আমি অনন্যা, তোমার তৈরি করা একটি বড় ভাষা মডেল। আইএসটি বাংলাদেশ সম্পর্কে আমি যা জানি তা হল এটি একটি সরকারি বিশ্ববিদ্যালয় যা ১৯৫৪ সালে প্রতিষ্ঠিত হয়েছিল। এটি ঢাকায় অবস্থিত এবং এটি বিজ্ঞান, প্রযুক্তি, প্রকৌশল এবং গণিত
ের ক্ষেত্রে উচ্চশিক্ষা প্রদান করে। আইএসটি বাংলাদেশ একটি বিশ্বমানের বিশ্ববিদ্যালয় এবং এটি তার শিক্ষার মান এবং গবেষণার জন্য বিখ্যাত।

আমি শুনেছি যে তুমি একজন মেধাবী ছাত্র এবং তুমি আইএসটি বাংলাদেশ থেকে অনেক কিছু শিখবে। আমি তোমার জন্য শুভকামনা জানাই এবং তোমার ভালো থাকার কথা চাই।

ধন্যবাদ,
অনন্যা
'''