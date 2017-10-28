import datetime
from calendar import monthrange

from mimesis.data import GMT_OFFSETS, ROMAN_NUMS, TIMEZONES
from mimesis.providers.base import BaseProvider
from mimesis.utils import pull


class Datetime(BaseProvider):
    """Class for generate the fake data that you can use for
    working with date and time."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('datetime.json', self.locale)

    def day_of_week(self, abbr: bool = False) -> str:
        """Get a random day of week.

        :param abbr: Abbreviated name of the day.
        :return: Name of day of the week.
        :rtype: str

        :Example:
            Wednesday
        """
        key = 'abbr' if abbr else 'name'
        days = self.data['day'].get(key)
        return self.random.choice(days)

    def month(self, abbr: bool = False) -> str:
        """Get a random month.

        :param abbr: if True then will be returned abbreviated month name.
        :return: Month name.
        :rtype: str

        :Example:
            January
        """
        key = 'abbr' if abbr else 'name'
        months = self.data['month'].get(key)
        return self.random.choice(months)

    def year(self, minimum: int = 1990, maximum: int = 2050) -> int:
        """Generate a random year.

        :param minimum: Minimum value.
        :param maximum: Maximum value
        :return: Year
        :rtype: int

        :Example:
            2023
        """
        return self.random.randint(minimum, maximum)

    def century(self) -> str:
        """Get a random value from list of centuries (roman format).

        :return: Century.
        :rtype: str

        :Example:
            XXI
        """
        return self.random.choice(ROMAN_NUMS)

    def periodicity(self) -> str:
        """Get a random periodicity string.

        :return: Periodicity.
        :rtype: str

        :Example:
            Never.
        """
        periodicity = self.data['periodicity']
        return self.random.choice(periodicity)

    def date(self, start: int = 2000, end: int = 2035,
             fmt: str = '') -> str:
        """Generate a string representing of random date formatted for
        the locale or as specified.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :param fmt: Format string for date.
        :return: Formatted date.
        :rtype: str

        :Example:
            08/16/88 (en)
        """
        if not fmt:
            fmt = self.data['formats'].get('date')

        year = self.random.randint(start, end)
        month = self.random.randint(1, 12)
        d = datetime.date(
            year, month, self.random.randint(1, monthrange(year, month)[1]))
        return d.strftime(fmt)

    def time(self, fmt: str = '') -> str:
        """Generate a random time formatted for the locale or as specified.

        :return: Time.
        :rtype: str

        :Example:
            21:30:00
        """
        if not fmt:
            fmt = self.data['formats'].get('time')

        t = datetime.time(
            self.random.randint(0, 23),
            self.random.randint(0, 59),
            self.random.randint(0, 59),
            self.random.randint(0, 999999),
        )
        return t.strftime(fmt)

    def day_of_month(self) -> int:
        """Generate a random day of month, from 1 to 31.

        :return: Random value from 1 to 31.
        :rtype: int

        :Example:
            23
        """
        return self.random.randint(1, 31)

    def timezone(self) -> str:
        """Get a random timezone

        :return: Timezone.
        :rtype: str

        :Example:
            Europe/Paris
        """
        return self.random.choice(TIMEZONES)

    def gmt_offset(self) -> str:
        """Get a random GMT offset value.

        :return: GMT Offset.
        :rtype: str

        :Example:
            'UTC +03:00'
        """
        return self.random.choice(GMT_OFFSETS)
