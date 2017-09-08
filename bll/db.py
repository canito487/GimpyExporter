import platform
import dal


def login_gimpy(username):

    """Login to gimpy"""

    # Type in your rest api url       *****IMPORTANT*****
    gimpyUrl = ""         # <---- Use this Testing Env URL 
                                                    

    # Method body:
    loginPayload = {
        "UserName": username,
        "Password": ""
    }

    # Method Headers:
    loginHeaders = {'content-type': 'application/json'}

    # Send the request with parameters and store it in login_response
    login_response = dal.tcdb.login_gimpy_call(gimpyUrl, loginPayload, loginHeaders)

    # Use the .json function() to get the data in json format and then we store it in login_response_json variable
    login_response_json = login_response.json()

    # Store the token
    token = login_response_json["Token"]
    return token

def add_a_test_case(body, token):

    """Create the Test Case"""

    # This is the gimpy URL used to add a test case to the DB                       *****IMPORTANT*****
    addTestCaseURL = "" # <--- Use this test env url first
                                                           

    # Method body
    addTestCase_PayLoad = body

    # Method Headers
    addTestCase_headers = {'content-type': 'application/json',
                               'Token': '%s' % token}

    # Specify request body json data and headers
    addTestCase_response = dal.tcdb.add_a_test_case_call(addTestCaseURL, addTestCase_PayLoad, addTestCase_headers)


    """Store the addTestCase response"""

    # Use the .json function() to get the data in json format and then we store it in addTestCase_response variable
    addTestCase_response = addTestCase_response.json()
    return addTestCase_response

def update_feature_suite(fsid, testcaseid, token):

    """Update Feature Suite"""

    # This is the gimpy URL used to add a test case to the DB
    updateFsURL = ""

    # Method body
    updateFsPayload = [
    {
        "Id": testcaseid
    }
    ]

    # Method Headers
    updateFsHeaders = {'content-type': 'application/json',
                               'Token': '%s' % token}

    # Specify request body json data and headers
    updateFsResponse = dal.tcdb.update_feature_suite_call(updateFsURL, updateFsPayload, updateFsHeaders)
    return updateFsResponse

def checkPathConfig ():
    # Get os type
    os_type = platform.system()
    if os_type == "Windows":
        dal.config.checkWindowsConfig()
    else:
        dal.config.checkMacConfig()

def setDirPath():
    dirPath = dal.config.getDirPath()
    return dirPath


def setTemplatePath():
    templatePath = dal.config.getTemplatePath()
    return templatePath


def setExcelPath():
    excelPath = dal.config.getExcelPath()
    return excelPath

def setTSname(name):
    dal.config.createTCSet(name)


def openWB(path):
    wb = dal.excel.openExcileFile(path)
    return wb

def openWS(path):
    ws = dal.excel.getSheet(path)
    return ws
