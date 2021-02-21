import abc


class MusicAbstract(metaclass=abc.ABCMeta):
    music_default_ganre = ['electronic']

    @classmethod
    @abc.abstractmethod
    def get_music_playlist(cls):
        return cls.music_default_ganre


class MyPlaylist(MusicAbstract):
    def __init__(self):
        self.ganre = ['dnb']

    def get_music_playlist(self):
        return self.ganre + super().get_music_playlist()


if __name__ == '__main__':
    m = MyPlaylist()
    print(m.get_music_playlist())
