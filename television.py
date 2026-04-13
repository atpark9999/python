class Television:
    """
    Class to hold the actions for the television
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Function to set up and initialize for the television
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        Function to set up and initialize the television
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        Function to mute or unmute the television
        """

        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        Function for pressing the channel up button
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Function for pressing the channel down button
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Function for pressing the volume up button
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self):
        """
        Function for pressing the volume down button
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self):
        """
        Function that returns the television status
        :return: returns the television status
        """
        if self.__muted:
            volume = 0
        else:
            volume = self.__volume

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"