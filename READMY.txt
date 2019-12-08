#run tests in parallel
pytest -n <number of CPUs>

#generate allure report
py.test --alluredir=./reports ./tests
allure serve ./reports

