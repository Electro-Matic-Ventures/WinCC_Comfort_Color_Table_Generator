from ApplicationData import ApplicationData


class Generate:
    
    data: ApplicationData
    
    def __init__(self, data:ApplicationData=ApplicationData()):
        self.data = data
        return    