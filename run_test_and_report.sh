BROWSER=chromium behave Features/ -f allure_behave.formatter:AllureFormatter -o allure-results/chromium
BROWSER=firefox behave Features/ -f allure_behave.formatter:AllureFormatter -o allure-results/firefox
allure generate allure-results/chromium allure-results/firefox -o allure-report --clean
allure open allure-report
