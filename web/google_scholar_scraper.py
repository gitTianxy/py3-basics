# encoding=utf-8
"""
TODO: analyze results from google scholar
----------------------------------------
"""
import gsscraper

if __name__ == '__main__':
    query = "neeman grothendieck duality"
    # return a Python dict with keys “title”, “author”, etc.
    gsscraper.get_result(query)
    # return a list of such Python dicts
    gsscraper.get_results(query, 5)
    # return a list of strings in XML format.
    gsscraper.get_result_as_xml(query)
