#!/home/nate/python/python_env/bin/python3
# Purpose : Say Hello
import argparse

# The get_args() function is dedicated to getting the arguments. All the argparse code now lives here.
def get_args():
    parser = argparse.ArgumentParser(description="Say Hello")
    # The only change to this program is adding -n and --name for the “short” and “long” option names. We also indicate a default value. “metavar” will show up in the usage to describe the argument.
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to Greet"
    )
    # We need to call return to send the results of parsing the arguments back to the main() function.
    return parser.parse_args()


def main():
    # Call the get_args() function to get parsed arguments. If there is a problem with the arguments or if the user asks for --help, the program never gets to this point because argparse will cause it to exit.
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
