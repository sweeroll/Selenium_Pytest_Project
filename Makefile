pytest:
	@pytest -s -v --headless=True --alluredir=allure_reports;
	@allure serve allure_reports
