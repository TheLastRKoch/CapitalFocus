from datetime import datetime


class TimeService:

    @classmethod
    def get_timestamp(self):
        return datetime.utcnow().strftime("%d%b%y%H%M%S")

    @classmethod
    def get_time_standard(self):
        return datetime.utcnow().strftime("%d/%b/%Y %H:%M:%S")
