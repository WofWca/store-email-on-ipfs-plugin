__license__ = """
Copyright 2022 WofWca <wofwca@protonmail.com>
Copyright 2022 Valery Senotov <senotovel@gmail.com>
Copyright 2022 Sergei Filipppov <sphilippov@protonmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

# def on_new_email(original_message: str, recipiend_email_address: str):
def on_new_email(original_message_file_name: str, recipiend_email_addresses: list[str]):
    # Work with just one recipient for now. TODO
    recipiend_email_address = recipiend_email_addresses[0]
    # original_message_file_name = 'original_message.txt'
    # with open(original_message_file_name, 'w') as original_message_file:
    #     original_message_file.write(original_message)
    print(f'New email.\nPath: {original_message_file_name},\nrecipient: {recipiend_email_address}\n')

    original_message_dir = os.path.dirname(original_message_file_name)
    original_message_file_basename = os.path.basename(original_message_file_name)
    # Pretty stupid, but alrighty
    encrypted_email_file_name = f'{original_message_dir}/../encrypted_emails/{original_message_file_basename}.gpg'

    # TODO protect from code injections.
    # TODO make sure that the file name is not public, or make it random.
    # TODO maybe it's possible to retrieve the recipient's public key from the email itself? Or at least
    # its fingerprint or something so we can download the key from key databases to verify it?
    # https://crypto.stackexchange.com/questions/81913/is-it-possible-to-get-the-pgp-public-key-from-pgp-message
    # or the email address itself can contain a public key (I don't think it is in any standards though).
    os.popen(
        f'gpg'
        f' -r {recipiend_email_address}'
        f' --output {encrypted_email_file_name}'
        f' --encrypt {original_message_file_name}'
    )
    fs = os.popen(f'ipfs add -Q {encrypted_email_file_name}')
    cid = fs.read()
    # TODO somehow make the user able to receive CID do download the email.
    # Also other peers should be able co-host the emails.
    print(f'Encryped email stored on IPFS. CID:\n{cid}\n')
