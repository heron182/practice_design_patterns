import logging

logging.basicConfig(level=logging.INFO)


class Database(object):
    def __init__(self):
        self.observers = []
        self._shards = 1

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def shards(self):
        return self._shards

    @shards.setter
    def shards(self, value):
        self._shards = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class BackupObserver(object):
    def __init__(self, observable):
        self.observable = observable

    def __call__(self):
        logging.info(f'Backing up data for {self.observable.shards} shards')


class ScaleResources(object):
    def __init__(self, observable):
        self.observable = observable

    def __call__(self):
        if self.observable.shards > 50:
            logging.info(
                f'Scaling resources due to Observable having more than 50 active shards'
            )


def main():
    db = Database()
    bp = BackupObserver(db)
    sc = ScaleResources(db)
    db.attach(bp)
    db.attach(sc)
    db.shards = 80


if __name__ == '__main__':
    main()
