from stat_parser import Parser, display_tree


parser = Parser()

# http://www.thrivenotes.com/the-last-question/
tree = parser.parse("Multiple SQL injection vulnerabilities in myBloggie 2.1.6 and earlier allow remote attackers to execute arbitrary SQL commands via the (1) cat_id or (2) year parameter to index.php in a viewuser action, different vectors than CVE-2005-1500 and CVE-2005-4225. ")

display_tree(tree)
