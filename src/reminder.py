class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """

    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'


class PoliteReminder(PrefixedReminder):
    """Just a nicer way to ask for the reminder?"""

    def __init__(self, text, date=None):
        """Note that the date param makes this function signature compatable
        with other classes but is not actually used."""
        super().__init__(prefix="please ")
        self.text = self.prefix + text

    def __iter__(self):
        return iter([self.text])
