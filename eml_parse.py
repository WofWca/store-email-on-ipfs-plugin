import json, datetime
import eml_parser

def get_recipiend_email_address(email_file_path: str = "./tests/sample.eml") -> list:

    ep = eml_parser.EmlParser()
    parsed_eml = ep.decode_email(email_file_path)
    print(parsed_eml)

    recipiend_email_addresses = parsed_eml['header']['to']
    return recipiend_email_addresses

def get_contents(email_file_path: str = "./tests/sample.eml") -> dict:

    ep = eml_parser.EmlParser(include_raw_body=True)
    parsed_eml = ep.decode_email(email_file_path)
    print(parsed_eml)

    contents = parsed_eml['body']
    return contents

if __name__ == '__main__':
    print(get_recipiend_email_address())
    print(get_contents())