import os

def on_new_email(email_file_path):
    recipiend_email = get_recipiend_email()
    # TODO protect from code injections.
    os.popen(f'gpg -r {recipiend_email} {email_file_path}')
    os.popen(f'ipfs add {email_file_path}.gpg')
