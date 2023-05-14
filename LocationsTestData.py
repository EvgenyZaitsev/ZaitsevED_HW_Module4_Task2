from TestData import TestData

LocationMostPopular = TestData('SELECT TOP(1) {} FROM {} GROUP BY {} ORDER BY {} DESC',
                               ['country_id as Country, COUNT(*) as TotalCount', 'hr.locations',
                                'country_id', 'TotalCount'], [['US', 3]])


LocationWithNulls = TestData('SELECT {} FROM {} WHERE {} IS NULL ',
                              ['city as City, country_id as Country', 'hr.locations', 'postal_code'],
                              [['London', 'UK']])

LocationTopCountry = TestData('SELECT {} FROM {} WHERE {} = (SELECT MAX({}) FROM {}) ',
                              ['city as City, country_id as Country', 'hr.locations', 'country_id', 'country_id', 'hr.locations'],
                              [['Southlake', 'US'], ['South San Francisco', 'US'], ['Seattle', 'US']])
