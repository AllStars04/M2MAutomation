import Class.Automation

obj = Class.Automation.Automation()
obj.openURL()
obj.login()
obj.clickOnMenu("Devices")
obj.clickOnSubmeu("All devices")
obj.verifyTextOnScreen("Results")
obj.clickOnButton("Search")
obj.clickOnLink("111110001000002")
obj.verifyTextOnScreen("Overview")
obj.clickOnTab("Operations")
obj.clickOnLink("Configure")
obj.verifyTextOnScreen("Change state")
obj.clickOnButton("Change...")
#obj.clickOnButton("Change...",2)
# obj.verifyTextOnScreen("Basic information")
# obj.enterText("Name","AutoTest1")
# obj.enterText("Description","Autoamtion test")
# obj.clickOnInput("Parent organisation","PPTOMTOM")
# obj.selectRadioButton("Yes")
# obj.selectRadioButton("Yes",2)

