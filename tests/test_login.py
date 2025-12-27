import allure


@allure.feature("User login")
@allure.story("Success login")
@allure.title("Успешный логин (standard_user / secret_sauce)")
def test_successful_login(login_page):
    with allure.step("Login to website"):
        login_page.open_page()
    with allure.step("Check link login page"):
        login_page.check_current_url_is("https://www.saucedemo.com/")
    with allure.step("Check page elements"):
        login_page.check_page_elements_are_visible()
    with allure.step("Filling out the login form"):
        login_page.fill_login_form("standard_user", "secret_sauce")
    with allure.step("Check link user home page"):
     login_page.check_current_url_is("https://www.saucedemo.com/inventory.html")
    with allure.step("Check page title text"):
        login_page.check_products_title_text_is("Products")

@allure.feature("User login")
@allure.story("Unsuccess login")
@allure.title("Логин с неверным паролем")
def test_correct_username_with_incorrect_password_login(login_page):
    with allure.step("Login to website"):
        login_page.open_page()
    with allure.step("Check link login page"):
        login_page.check_current_url_is("https://www.saucedemo.com/")
    with allure.step("Check page elements"):
        login_page.check_page_elements_are_visible()
    with allure.step("Filling out the login form"):
        login_page.fill_login_form("standard_user", "secret_sauces")
    with allure.step("Check error alert text"):
        login_page.check_error_alert_text_is(
        "Epic sadface: Username and password do not match any user in this service"
        )

@allure.feature("User login")
@allure.story("Unsuccess login")
@allure.title("Логин заблокированного пользователя (locked_out_user)")
def test_locked_out_user_login(login_page):
    with allure.step("Login to website"):
        login_page.open_page()
    with allure.step("Check link login page"):
        login_page.check_current_url_is("https://www.saucedemo.com/")
    with allure.step("Check page elements"):
        login_page.check_page_elements_are_visible()
    with allure.step("Filling out the login form"):
        login_page.fill_login_form("locked_out_user", "secret_sauce")
    with allure.step("Check error alert text"):
        login_page.check_error_alert_text_is(
        "Epic sadface: Sorry, this user has been locked out."
    )

@allure.feature("User login")
@allure.story("Unsuccess login")
@allure.title("Логин с пустыми полями")
def test_empty_fills_login(login_page):
    with allure.step("Login to website"):
        login_page.open_page()
    with allure.step("Check link login page"):
        login_page.check_current_url_is("https://www.saucedemo.com/")
    with allure.step("Check page elements"):
        login_page.check_page_elements_are_visible()
    with allure.step("Filling out the login form"):
        login_page.fill_login_form("", "")
    with allure.step("Check error alert text"):
        login_page.check_error_alert_text_is(
        "Epic sadface: Username is required"
    )

@allure.feature("User login")
@allure.story("Success login")
@allure.title("Логин пользователем performance_glitch_user)")
def test_performance_glitch_user_login(login_page):
    with allure.step("Login to website"):
        login_page.open_page()
    with allure.step("Check link login page"):
        login_page.check_current_url_is("https://www.saucedemo.com/")
    with allure.step("Check page elements"):
        login_page.check_page_elements_are_visible()
    with allure.step("Filling out the login form"):
        login_page.fill_login_form("performance_glitch_user", "secret_sauce")
    with allure.step("Check link user home page"):
        login_page.check_current_url_is("https://www.saucedemo.com/inventory.html")
    with allure.step("Check page title text"):
        login_page.check_products_title_text_is("Products")

