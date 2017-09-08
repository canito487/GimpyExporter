README - GIMPY EXPORTER V1.2
1| Install python 2.7
2| pip install xlrd shutil OrderedDict requests simplejson openpyxl os ConfigParser platform
3| Move TestCaseTracker.xlsx and add_a_json.json files to a directory path you want.
	Ex: /Users/alex.hernandez/gimpyexporter/TestCaseTracker.xlsx
	Ex: /Users/alex.hernandez/gimpyexporter/add_a_test_case.json * Save these paths because you will be prompted for these paths at beginning of script

4| Create a TestCaseSets Folder where your test cases will be stored.
	Ex: /Users/alex.hernandez/gimpyexporter/TestCaseSets    *Save this path because you will be prompted for this path at beginning of script




5| Execute gimpyexporter.py with this command:   python gimpyexporter.py


**Important** - 
1) Make sure you test your first round of test cases in the TEST GIMPY DB. I have a feature suite already set up: its feature suite 3136, or you can create one if you want.
2) Use the excel sheet provided – TestCaseTracker.xlsx
3) Use the add a test case template – add-a-test-case.json
4) Start writing test cases on row 3
4) The URLs are already in the script but here it is just in case:
