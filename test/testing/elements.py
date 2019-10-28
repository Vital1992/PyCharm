from selenium import webdriver

class users():
    login1 = "QATest1"
    password1 = "Qa123456789!"

    login2 = "QATest2"
    password2 = "Qa123456789!"

class pom():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    loginBtn = "//span[@qid='navbar-login-register-button']"
    registerBtn = "//*[contains(text(), 'Join Now')]"
    usernameFiled = "//input[@type='text'][@class='input'][@required='required']"
    emailField = "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div/div/dl[3]/dd/input"
    passwordFiled = "//input[@class='input js-password input--passwordHideShow']"
    acceptTerms = "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div/div/dl[7]/dd/label/i"
    submitBtn = "//*[@id = 'js-signUpButton']"
    successfulRegistration = "//*[contains(text(),'Thanks for registering')]"
    loginUsernameField = "//input[@name='login']"
    loginPasswordField = "//input[@name='password']"
    loginBtn2 = "//button[@qid='login-button']"
    userIcon = "//*[@id='header']/div/div/div[3]/span/a/span/div/span"
    userProfile = "//span[text()='My Profile']"