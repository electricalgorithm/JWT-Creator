import argparse
import datetime
import logging
import os
import random
import ssl
import time
import jwt

def create_jwt(project_id, private_key_file, algorithm):
    token = {
        # The time that the token was issued at
        "iat": datetime.datetime.now(tz=datetime.timezone.utc),
        # The time the token expires.
        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=60*23),
        # The audience field should always be set to the GCP project id.
        "aud": project_id,
    }
    # Read the private key file.
    with open(private_key_file, "r") as f:
        private_key = f.read()

    return jwt.encode(token, private_key, algorithm=algorithm)




def init_argument_parser():
    parser = argparse.ArgumentParser(description="This application gives you the JWT token you need.")
    parser.add_argument("-i", "--project_id", nargs="+", required=True, help="Provide your project id as a string.")
    parser.add_argument("-p", "--private_key", nargs="+", required=True, help="Provide the private key file.")
    parser.add_argument("-a", "--algorithm", nargs="+", required=True, help="Provide the algorithm name as a string.")

    return parser.parse_args()


if __name__ == "__main__":
    args = init_argument_parser()
    jwt_token = create_jwt(args.project_id[0], args.private_key[0], args.algorithm[0])
    print(jwt_token)
