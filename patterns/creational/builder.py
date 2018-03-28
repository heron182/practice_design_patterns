'''
    Separate the construction of a complex object from its representation so that 
    the same construction process can create different representations.
    Parse a complex representation, create one of several targets.

https://gist.github.com/pazdera/1121157
'''


class Database(object):

  def __init__(self):
    self._connection = None
    self._dyalects = None
    self._orm = None

  def setConnection(self, connection):
    self._connection = connection

  def setDyalects(self, dyalects):
    self._dyalects = dyalects

  def setOrm(self, orm):
    self._orm = orm

  def getSpecification(self):
    return (self._connection.for_database, self._dyalects.for_database,
            self._orm.for_database)


class Connection(object):
  for_database = None


class Dyalects(object):
  for_database = None


class Orm(object):
  for_database = None


class DatabaseBuilder(object):

  def __init__(self):
    self.database = None

  def getConnection(self):
    pass

  def getDyalects(self):
    pass

  def getOrm(self):
    pass


class PostgresBuilder(DatabaseBuilder):

  def getConnection(self):
    conn = Connection()
    conn.for_database = 'Connection for Postgres database'
    return conn

  def getDyalects(self):
    dyalects = Dyalects()
    dyalects.for_database = 'Dyalects for Postgres database'
    return dyalects

  def getOrm(self):
    orm = Orm()
    orm.for_database = 'Orm for Postgres database'
    return orm


class Director(object):

  _builder = None

  def setBuilder(self, builder):
    self._builder = builder

  def buildDatabase(self):
    database = Database()

    connection = self._builder.getConnection()
    database.setConnection(connection)

    dyalects = self._builder.getDyalects()
    database.setDyalects(dyalects)

    orm = self._builder.getOrm()
    database.setOrm(orm)

    self._builder.database = database

  def getDatabase(self):
    return self._builder.database


def main():
  director = Director()
  postgresBuilder = PostgresBuilder()
  director.setBuilder(postgresBuilder)
  director.buildDatabase()
  postgresInterface = director.getDatabase()
  print(postgresInterface.getSpecification())


if __name__ == '__main__':
  main()
