import os

# def on_new_email(original_message: str, recipiend_email_address: str):
def on_new_email(original_message_file_name: str, recipiend_email_address: str):
    # original_message_file_name = 'original_message.txt'
    # with open(original_message_file_name, 'w') as original_message_file:
    #     original_message_file.write(original_message)

    # TODO protect from code injections.
    # TODO make sure that the file name is not public, or make it random.
    # TODO maybe it's possible to retrieve the recipient's public key from the email itself? Or at least
    # its fingerprint or something so we can download the key from key databases to verify it?
    # https://crypto.stackexchange.com/questions/81913/is-it-possible-to-get-the-pgp-public-key-from-pgp-message
    # or the email address itself can contain a public key (I don't think it is in any standards though).
    os.popen(f'gpg -r {recipiend_email_address} {original_message_file_name}')
    encrypted_email_file_name = f'{original_message_file_name}.gpg'
    fs = os.popen(f'ipfs add -Q {encrypted_email_file_name}')
    cid = fs.read()
    # TODO somehow make the user able to receive CID do download the email.
    # Also other peers should be able co-host the emails.
    print(f'Encryped email stored on IPFS. CID: {cid}')
