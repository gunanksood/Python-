import urllib
def convertor(text_to_convert):
    connection=urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
    output=connection.read()
    print "converted pirate speech is "+output


text=raw_input("enter text to translate ")
convertor(text)
    
