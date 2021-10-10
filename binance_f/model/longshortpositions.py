

class LongShortPositions:

    def __init__(self):
        self.pair = ""
        self.longShortRatio = 0.0  #  long/short account num ratio of top traders
        self.longPosition = 0.0  # long account num ratio of top traders
        self.shortPosition = 0.0  # short account num ratio of top traders 
        self.timestamp = 0
    
    @staticmethod
    def json_parse(json_data):
        result = LongShortPositions()
        result.symbol = json_data.get_string("symbol")
        result.longShortRatio = json_data.get_float("longShortRatio")
        result.longPosition = json_data.get_float("longAccount")
        result.shortPosition = json_data.get_float("shortAccount")
        result.timestamp = json_data.get_int("timestamp")

        return result