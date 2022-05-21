## How it works

1. An email comes to the mail server.
2. Read who's the recipient of the email.
3. Find the recipient's public key in the local database.
4. Encrypt the whole email payload with that public key (even if it's already encrypted with a PGP key).
5. Start hosting the encrypted email on IPFS (`ipfs add <encrypted_email_file>`).
6. TODO how to notify the recipient that there's a new email? IPNS with a list of all emails? Or is it not our business for now?
7. TODO how to make other IPFS peers able to download and co-host the encrypted emails?
