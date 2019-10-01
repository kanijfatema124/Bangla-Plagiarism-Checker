
import Window as window #for importing function and classes from Windows file
import WebSystem
import sys

#                                  Running Main traversing and searching data
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#                                            Showing windows
#-------------------------------------------------------------------------------------------------------------------

app = window.QApplication(window.sys.argv)
desktop_window = window.ApplicationWindow()
desktop_window.show()

def check_clicked():

    input_data_from_desktop_window  = desktop_window.getInputValue() #getting input value from window
    input_with_space = input_data_from_desktop_window.split('।')
    inputs =[]
    for new in input_with_space:
        if new!='':
            inputs.append(new)

    print(inputs)
    url = "https://anytechtune.com/" # this is base url and it can be anything

    links =WebSystem.link_Finder(url)
    links.append(url)
    counter =0
    desktop_window.listWidget.clear()
    desktop_window.progressBar.setProperty('value', 0)
    input_length = len(inputs)

    for link in links:
        contents =WebSystem.content_finder(link)
        for content in contents:
            for input in inputs:
                if len(inputs) == 0:
                    break
                if input in content or content in input:
                    counter = counter+1
                    x =str(counter)+'. '+input+'--'+link
                    inputs.remove(input)
                    desktop_window.listWidget.addItem(x)
                    if len(inputs)==0:
                        break
                if len(inputs) == 0:
                    break
        if len(inputs) == 0:
            break
    result =int(((input_length - len(inputs))/input_length)*100)
    print(result)
    desktop_window.progressBar.setProperty('value',result)


desktop_window.check.clicked.connect(check_clicked)
sys.exit(app.exec())
