import os

def on_new_email(email_file_path):
    get_recipiend_email_address = get_recipiend_email_address()
    # TODO protect from code injections.
    os.popen(f'gpg -r {get_recipiend_email_address} {email_file_path}')
    os.popen(f'ipfs add {email_file_path}.gpg')
