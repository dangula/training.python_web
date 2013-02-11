import os
import bottler
import unittest
import tempfile


class BottlerTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, bottler.app.config['DATABASE'] = tempfile.mkstemp()
        bottler.app.config['TESTING'] = True
        self.app = bottler.app
        bottler.init_db()
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bottler.app.config['DATABASE'])
    
    def test_database_setup(self):
        con = bottler.connect_db()
        cur = con.execute('PRAGMA table_info(entries);')
        rows = cur.fetchall()
        print rows
        self.assertTrue(len(rows) == 3)


if __name__ == '__main__':
    unittest.main()