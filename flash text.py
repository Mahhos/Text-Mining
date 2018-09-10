from flashtext.keyword import KeywordProcessor


keyword_processor = KeywordProcessor()
# keyword_processor.add_keyword('SQL injection')
keyword_processor.add_keyword('SQL injection', ('vulnerability type', 'SQL injection'))
keyword_processor.add_keyword('cross-site scripting', ('vulnerability type', 'cross-site scripting'))
keyword_processor.add_keyword('cross-site scripting', 'XSS')
# keyword_processor.add_keyword('parameter')
# keyword_processor.add_keyword('function')
# keyword_processor.add_keyword('variable')

keyword_dict = {
      "cross-site scripting": ["XSS"],
      "parametert": ["variabler"]
}
# {'clean_name': ['list of unclean names']}
keyword_processor.add_keywords_from_dict(keyword_dict)
# Or add keywords from a list:
keyword_processor.add_keywords_from_list(["parameter", "function", "variable"])

####keyword replacement
# keyword_processor.add_keyword('cross-site scripting', 'XSS')
# keyword_processor.replace_keywords('vulnerability is cross-site scripting')

keyword_processor.extract_keywords('SQL injection vulnerability in the update_zone function in catalog/admin/geo_zones.php in osCommerce Online Merchant 2.3.3.4 and earlier allows remote administrators to execute arbitrary SQL commands via the zID parameter in a list action. ')