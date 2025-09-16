def myfun():
    print("Hello World!!!")

def yourfun():
    print("Hey there")    

yourfun()    # in main.py only hey there is print because __name=__module__ when we run on another file using import
if __name__== "__main__":

    print("We are diectly running this code ")
    myfun()
    print(__name__)

