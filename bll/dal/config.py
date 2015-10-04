import ConfigParser
import os

def checkMacConfig():
    # create config file and check if it is null
    config = ConfigParser.ConfigParser()

    config.read("config.ini")
    macPath = config.get("Paths", "directoryPath")

    if macPath == "":
        askDirPath = raw_input("Set a path to store your test cases. (Ex: /Users/alex.hernandez/TestCases/): ")
        print "\n"
        askTemplatePath = raw_input("Set a path to your template file. (Ex: /Users/alex.hernandez/add_a_json.json) ")
        print "\n"
        askExcelPath = raw_input("Set a path to your excel file. (Ex:/Users/alex.hernandez/hi.xlsx) ")
        print "\n"
        file1 = open("config.ini", "w")
        config.set("Paths", "directorypath", askDirPath)
        config.set("Paths", "templatepath", askTemplatePath)
        config.set("Paths", "excelpath", askExcelPath)
        config.write(file1)
        file1.close()

    config.read("config.ini")

    dirPath = config.get("Paths", "directorypath")
    templatePath = config.get("Paths", "templatepath")
    excelPath = config.get("Paths", "excelpath")

    print "Your test cases will be stored in this path: \n" + dirPath
    print "\n"
    print "Your template file location is: \n" + templatePath
    print "\n"
    print "Your Excel file location is: \n" + excelPath
    print "\n"

    pathQuestion = raw_input("Is this correct: (Y/N) ").lower()
    while pathQuestion == "n":
        askDirPath = raw_input("Set a path to store your test cases. (Ex: /Users/alex.hernandez/TestCases/): ")
        print "\n"
        askTemplatePath = raw_input("Set a path to your template file. (Ex: /Users/alex.hernandez/add_a_json.json) ")
        print "\n"
        askExcelPath = raw_input("Set a path to your excel file. (Ex:/Users/alex.hernandez/hi.xlsx) ")
        print "\n"
        file1 = open("config.ini", "w")
        config.set("Paths", "directorypath", askDirPath)
        config.set("Paths", "templatepath", askTemplatePath)
        config.set("Paths", "excelpath", askExcelPath)
        config.write(file1)
        file1.close()

        dirPath = config.get("Paths", "directorypath")
        templatePath = config.get("Paths", "templatepath")
        excelPath = config.get("Paths", "excelpath")

        print "Your test cases will be stored in this path: \n" + dirPath
        print "\n"
        print "Your template file location is: \n" + templatePath
        print "\n"
        print "Your Excel file location is: \n" + excelPath
        print "\n"

        pathQuestion = raw_input("Is this correct?: (Y/N) ")
        if not pathQuestion == "n":
            break
        return

def checkWindowsConfig():
    # create config file and check if it is null
    config = ConfigParser.ConfigParser()

    config.read("config.ini")
    windowsPath = config.get("Paths", "directoryPath")

    if windowsPath == "":
        askDirPath = raw_input("Set a path to store your test cases. (Ex: C:\GIMPY_EXPORTER\): ")
        print "\n"
        askTemplatePath = raw_input("Set a path to your template file. (C:\GIMPY_EXPORTER\dadd_a_test_case.json) ")
        print "\n"
        askExcelPath = raw_input("Set a path to your excel file. (C:\GIMPY_EXPORTER\excelfile.xlsx) ")
        print "\n"
        file1 = open("config.ini", "w")
        config.set("Paths", "directorypath", askDirPath)
        config.set("Paths", "templatepath", askTemplatePath)
        config.set("Paths", "excelpath", askExcelPath)
        config.write(file1)
        file1.close()

    config.read("config.ini")

    dirPath = config.get("Paths", "directorypath")
    templatePath = config.get("Paths", "templatepath")
    excelPath = config.get("Paths", "excelpath")

    print "Your test cases will be stored in this path: \n\n" + dirPath
    print "Your template file location is: \n\n" + templatePath
    print "Your Excel file location is: \n\n" + excelPath



    pathQuestion = raw_input("Is this correct: (Y/N) \n").lower()
    while pathQuestion == "n":
        askDirPath = raw_input("Set a path to store your test cases. (Ex: C:\GIMPY_EXPORTER\): ")
        print "\n"
        askTemplatePath = raw_input("Set a path to your template file. (C:\GIMPY_EXPORTER\dadd_a_test_case.json) ")
        print "\n"
        askExcelPath = raw_input("Set a path to your excel file. (C:\GIMPY_EXPORTER\excelfile.xlsx) ")
        print "\n"
        file1 = open("config.ini", "w")
        config.set("Paths", "directorypath", askDirPath)
        config.set("Paths", "templatepath", askTemplatePath)
        config.set("Paths", "excelpath", askExcelPath)
        config.write(file1)
        file1.close()

        dirPath = config.get("Paths", "directorypath")
        templatePath = config.get("Paths", "templatepath")
        excelPath = config.get("Paths", "excelpath")

        print "Your test cases will be stored in this path: \n\n" + dirPath
        print "Your template file location is: \n\n" + templatePath
        print "Your Excel file location is: \n\n" + excelPath

        pathQuestion = raw_input("Is this correct?: (Y/N) ")
        if not pathQuestion == "n":
            break
    return

def getDirPath():
    # create config file and check if it is null
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    path = config.get("Paths", "directoryPath")
    return path

def getTemplatePath():
    # create config file and check if it is null
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    path = config.get("Paths", "templatepath")
    return path

def getExcelPath():
    # create config file and check if it is null
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    path = config.get("Paths", "excelpath")
    return path

def createTCSet(name):
    os.makedirs(name)
