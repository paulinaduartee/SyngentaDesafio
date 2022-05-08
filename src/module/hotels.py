class Hotels():
    def __init__(self,name,classification, regular_weekday, regular_weekend, rewards_weekday, rewards_weekend):
        self.name = name
        self.classification = classification
        self.__regular_weekday = regular_weekday
        self.__regular_weekend = regular_weekend
        self.__rewards_weekday = rewards_weekday
        self.__rewards_weekend = rewards_weekend
        return
    def get_weekday(self, client):
        if client == 'Regular':
            return self.__regular_weekday
        elif client == 'Rewards':
            return self.__rewards_weekday
    def get_weekend(self, client):
        if client == 'Regular':
            return self.__regular_weekend
        elif client == 'Rewards':
            return self.__rewards_weekend