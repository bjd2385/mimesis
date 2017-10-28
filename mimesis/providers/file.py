from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.providers.base import BaseProvider


class File(BaseProvider):
    """Class for generate fake data for files."""

    def extension(self, file_type: str = 'text') -> str:
        """Get a random file extension from list.

        :param file_type:
            File type (source, text, data, audio, video, image,
            executable, compressed).
        :return: Extension of a file.
        :rtype: str

        :Example:
            .py (file_type='source').
        """
        key = file_type.lower()
        return self.random.choice(EXTENSIONS[key])

    def mime_type(self, type_t: str = 'application') -> str:
        """Get a random mime type from list.

        :param type_t:
            Type of media: (application, image, video, audio, text, message).
        :return: Mime type.
        :rtype: str
        """
        supported = ' '.join(MIME_TYPES.keys())

        if type_t not in list(MIME_TYPES.keys()):
            raise ValueError(
                'Unsupported mime type! Use: {}'.format(supported))

        mime_type = self.random.choice(MIME_TYPES[type_t])
        return mime_type
