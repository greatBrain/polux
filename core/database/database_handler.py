import sqlite3 as lite

class Connection:
      def __init__(self):
          pass
      
      def connect(self):
          self.conn = lite.connect('database/polux.db')
          return self.conn    

      def cursor(self):
          self.cursor = self.conn.cursor()
          return self.cursor

          


      