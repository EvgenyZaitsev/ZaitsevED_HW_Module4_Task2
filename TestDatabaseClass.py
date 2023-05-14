from pyodbc import Connection, Cursor
import pytest

import EmployeesTestData
import JobsTestData
import LocationsTestData
import Variables
from DbHelper import *


class TestDatabaseClass:
    _connection: Connection
    _cursor: Cursor

    def setup_class(self):
        connection_string = DbHelper.format_connection_string(Variables.DriverName, Variables.DbServer,
                                                              Variables.DbName,
                                                              Variables.DbUser, Variables.DbPassword, False)
        self._connection, self._cursor = DbHelper.connect_to_database(connection_string)

    def teardown_class(self):
        DbHelper.close_connection(self._connection, self._cursor)

    @pytest.mark.parametrize("test_data",
                             [EmployeesTestData.EmployeesCount, EmployeesTestData.EmployeesOldestOne],
                             ids=['test_employees_count', 'test_employees_oldest'])
    def test_employees(self, test_data):
        query = test_data.query
        params = test_data.query_params
        expected_results = test_data.expected_results

        column_names, actual_results = DbHelper.execute_query(self._cursor, query, params)
        print(column_names)
        for actual_result in actual_results:
            print(actual_result)

        for result_number, expected_result in enumerate(expected_results):
            for index, value in enumerate(expected_results[result_number]):
                assert expected_results[result_number][index] == actual_results[result_number][index]

    @pytest.mark.parametrize("test_data",
                             [LocationsTestData.LocationMostPopular, LocationsTestData.LocationWithNulls,
                              LocationsTestData.LocationTopCountry],
                             ids=['test_location_most_popular', 'test_location_with_null', 'test_location_top_country'])
    def test_locations(self, test_data):
        query = test_data.query
        params = test_data.query_params
        expected_results = test_data.expected_results

        column_names, actual_results = DbHelper.execute_query(self._cursor, query, params)
        print(column_names)
        for actual_result in actual_results:
            print(actual_result)

        for result_number, expected_result in enumerate(expected_results):
            for index, value in enumerate(expected_results[result_number]):
                assert expected_results[result_number][index] == actual_results[result_number][index]

    @pytest.mark.parametrize("test_data",
                             [JobsTestData.JobsMaxAverageMin, JobsTestData.JobsEmployeesCount],
                             ids=['test_jobs_max_average_min_salary', 'test_jobs_employees_count_per_position'])
    def test_jobs(self, test_data):
        query = test_data.query
        params = test_data.query_params
        expected_results = test_data.expected_results

        column_names, actual_results = DbHelper.execute_query(self._cursor, query, params)
        print(column_names)
        for actual_result in actual_results:
            print(actual_result)

        for result_number, expected_result in enumerate(expected_results):
            for index, value in enumerate(expected_results[result_number]):
                assert expected_results[result_number][index] == actual_results[result_number][index]
