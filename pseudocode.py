import os

def on_new_email(email_file_path):
    get_recipiend_email_address = get_recipiend_email_address()
    # TODO protect from code injections.
    # TODO make sure that the file name is not public, or make it random.
    # TODO maybe it's possible to retrieve the recipient's public key from the email itself? Or at least
    # its fingerprint or something so we can download the key from key databases to verify it?
    os.popen(f'gpg -r {get_recipiend_email_address} {email_file_path}')
    cid = os.popen(f'ipfs add -Q {email_file_path}.gpg')
    # TODO somehow make the user able to receive CID do download the email.
    # Also other peers should be able co-host the emails.
