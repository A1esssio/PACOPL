import unittest
from RK2 import Database, DataTable, TableDatabaseLink, \
    get_dbs_starting_with_a, get_dbs_sorted_by_max_rows, get_many_to_many_links_sorted

class TestDatabaseQueries(unittest.TestCase):
    def setUp(self):
        self.databases = [
            Database(1, "Аналитика"),
            Database(2, "Архив"),
            Database(3, "Продажи"),
        ]
        self.tables = [
            DataTable(1, "Users", 100, 1),
            DataTable(2, "Logs", 2000, 2),
            DataTable(3, "AnalyticsData", 500, 1),
            DataTable(4, "OldRecords", 50, 2)
        ]
        self.links = [
            TableDatabaseLink(1, 1),
            TableDatabaseLink(2, 2),
            TableDatabaseLink(1, 2)
        ]

    def test_get_dbs_starting_with_a(self):
        result = get_dbs_starting_with_a(self.databases, self.tables)

        self.assertEqual(len(result), 2)

        self.assertEqual(result[0][0], "Аналитика")
        self.assertIn(("Users", 100), result[0][1])
        self.assertIn(("AnalyticsData", 500), result[0][1])

    def test_get_dbs_sorted_by_max_rows(self):
        result = get_dbs_sorted_by_max_rows(self.databases, self.tables)

        expected = [
            ("Архив", 2000),
            ("Аналитика", 500),
        ]
        self.assertEqual(result, expected)

    def test_get_many_to_many_links(self):
        result = get_many_to_many_links_sorted(self.databases, self.tables, self.links)

        expected = [
            ('Аналитика', [('Users', 100)]),
            ('Архив', [('Logs', 2000), ('Users', 100)]),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
