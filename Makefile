BUILD_PATH = docs/build
SOURCE_PATH = docs/source
HTML_PATH = $(BUILD_PATH)/html
API_PATH = $(SOURCE_PATH)/api
TEST_PATH = tests
DATA_PATH = $(TEST_PATH)/data
BIDS_PATH = $(DATA_PATH)/bids
DERIVATIVES_PATH = $(DATA_PATH)/derivatives
COV_PATH = htmlcov

doc:
	sphinx-apidoc -fMET -o $(API_PATH) bidso
	sphinx-build -T -b html -d $(BUILD_PATH)/doctrees $(SOURCE_PATH) $(HTML_PATH)

test:
	rm $(BIDS_PATH) -fr
	py.test -x --cov=bidso --cov-report=html --cov-report=term tests

clean:
	rm $(BUILD_PATH) -fr
	rm $(API_PATH) -fr
	rm $(BIDS_PATH) -fr 
	rm $(COV_PATH) -fr 
