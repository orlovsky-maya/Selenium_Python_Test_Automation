def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


# # example_1
# full_string = 'fulltext'
# substring = 'some_value'
# print(test_substring(full_string, substring))

# # example_2
# full_string = 'some_text'
# substring = 'some'
# print(test_substring(full_string, substring))
