class TestData:
    query: str
    query_params: list[str]
    expected_results: list[list]

    def __init__(self, query: str, query_params: list[str], expected_results: list[list]):
        self.query = query
        self.query_params = query_params
        self.expected_results = expected_results
