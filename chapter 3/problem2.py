letter = ''' Dear <|name|>,
            You are selected!!!
            <|Date|>'''
print(letter.replace("<|name|>", "Prince").replace("<|Date|>","sep 10"))