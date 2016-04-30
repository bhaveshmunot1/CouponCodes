class FileOperations:
    def ReadFile(self, path):
        with open(path, 'r') as content_file:
            content = content_file.read()
        return content
        
    def WriteToFile(self, path, content):
        with open(path, "w") as text_file:
            text_file.write(str(content))
            
    def AppendToFile(self, path, content):
        with open(path, "a") as myfile:
            try:
                myfile.write(str(content)+"\n\n")
            except:
                pass