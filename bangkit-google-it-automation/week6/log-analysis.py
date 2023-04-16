import re

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"

re.search(r"ticky: ERROR: ([\w ]*) ", line)

# ./csv_to_html.py error_message.csv /var/www/html/error_message.html
# ./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
