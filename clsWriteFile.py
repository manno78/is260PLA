class clsWriteFile:
    """Writes text to specified file

    :param FileName: string, the file being written to.
    :param Overwrite: boolean, if the file exits should it be overwritten
    """
    def __init__(self, initFileName, initOverwrite=True):
        self.FileName = initFileName
        self.Overwrite = initOverwrite
        if self.Overwrite == True:
            file = open(self.FileName, "w")
            file.close()

    def setWriteFile(self, LogText):
        """writes the supplied string to the file"""
        file = open(self.FileName, "a+")
        file.write(LogText + "\r\n")
        file.close()
