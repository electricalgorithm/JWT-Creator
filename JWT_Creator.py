"""This script creates you a JWT for using IoT Projects of your Google Cloud."""
import argparse
import datetime
import jwt

def create_jwt(project_id: str, private_key_file: str, algorithm: str, minutes: int = 20) -> str:
    # The time that the token was issued at
    iat = datetime.datetime.now(tz=datetime.timezone.utc)
    # The time the token expires.
    exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=minutes)
    
    token = {
        "iat": iat,
        "exp": exp,
        # The audience field should always be set to the GCP project id.
        "aud": project_id,
    }
    # Read the private key file.
    with open(private_key_file, "r") as f:
        private_key = f.read()

    return [jwt.encode(token, private_key, algorithm=algorithm), iat, exp]


def init_argument_parser() -> dict:
    parser = argparse.ArgumentParser(description="This application gives you the JWT token you need.")
    parser.add_argument("-i", "--project_id", nargs="+", required=True, help="Provide your project id as a string.")
    parser.add_argument("-p", "--private_key", nargs="+", required=True, help="Provide the private key file.")
    parser.add_argument("-a", "--algorithm", nargs="+", required=True, help="Provide the algorithm name as a string.")
    parser.add_argument("-t", "--minutes", nargs="+", required=False, help="Provide duration in terms of minutes.")
    parser.add_argument("-s", "--save", nargs="+", required=False, help="Save the token into a TXT file.")

    return parser.parse_args()


if __name__ == "__main__":
    args = init_argument_parser()
    jwt_token, start_time, end_time = create_jwt(args.project_id[0], args.private_key[0], args.algorithm[0], minutes=(int(args.minutes[0]) or 20))
    print(f'\n\tJWT_Creator.py\n\
            Starting Time: {start_time}\n\
            Ending Time: {end_time}')
    print("\n========= JSON WEB TOKEN IS BELOW =========")
    print(jwt_token)
    print("========= JSON WEB TOKEN IS ABOVE =========\n")

    # Save the token into a file if wanted.
    if args.save is not None:
        save_file = open(args.save[0], "w")
        save_file.write(jwt_token)
        save_file.close
