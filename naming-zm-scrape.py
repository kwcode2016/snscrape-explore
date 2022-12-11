import os

from_date = '2019-04-01'
to_date = '2022-12-11'
file_name_message = "all zm tweets"
file_name_message = file_name_message.replace(' ', '-')

print (file_name_message)

filename_template = f'snscrape --jsonl --progress --max-results 100000 --since {from_date} twitter-search "\$ZM until:{to_date}" > zm-4-{from_date}-{to_date}-{file_name_message}.jsonl'

print(filename_template)