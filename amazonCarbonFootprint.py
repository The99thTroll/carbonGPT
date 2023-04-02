from flask import Flask, request, jsonify
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

  

  
app = Flask(__name__)

app.config["DEBUG"] = True
objectDetected = "none"
lastPost = ""

def get_result(image_path):
    #use selenium to open the website
    webdriver_path = r"./chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    driver.get("https://microsoft.github.io/onnxjs-demo/#/squeezenet")
    time.sleep(5)

    #click the button to upload the image
    #the style is "display: none;" and it is the second in the array. It is in the form of an input tag
    file_upload = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/main/div/div/div/div/div[1]/div/div[3]/div[1]/div[1]/label/input"))
    )
    file_upload.send_keys(image_path)

    time.sleep(3)

    xpath = "/html/body/div/div/div[3]/main/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]"
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    print(result.text)
    return (result.text)
    


@app.route("/image", methods=["POST"])
def image():
        try:
            global objectDetected
            image = request.files["image"]
            image.save("images/" + image.filename)
            
            print("calling function")
            objectDetected =  image.filename + "-" + get_result("/Users/albrino/Downloads/Old-Items/ChromeExtensionScrapingHelloWorld/images/" + image.filename)
            print(objectDetected)
            print("returned")
        except Exception as e:
            print(e)
            return "error"
        
@app.route("/imageCheck", methods=["GET"])
def imageCheck():
        filename = request.args.get("filename")
        #check if the filename is in the first part of the objectDetected
        print(objectDetected.split)
        print(objectDetected.split("-")[0])
        print(objectDetected.split("-")[1])
        if objectDetected.split("-")[0] == filename:
            #return the second part of the objectDetected in the
            return jsonify(objectDetected.split("-")[1])
        return "not found"


#start app at port
if __name__ == "__main__":
    app.run(port=5000)