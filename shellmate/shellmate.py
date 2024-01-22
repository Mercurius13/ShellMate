import os
import sys
import openai
import argparse
from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])


def explain_command(command, os):
    """
    Explain a given command using GPT, for the specified OS.
    """
    prompt = f"Explain the {os} command '{command}' in 2 lines. Make sure you don't use markdown or give code in ``` format, I want plain text"
    return query_openai(prompt)


def find_command(description, os):
    """
    Find a command based on the given description for the specified OS.
    """
    prompt = f"Find a {os} command that matches the following description: '{description}'"
    return query_openai(prompt)


def query_openai(prompt):
    """
    Send a query to OpenAI's GPT model and return the response.
    """
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=75,
    )

    response = completion.choices[0].message.content
    return response


def shellmate():
    parser = argparse.ArgumentParser(
        description="ShellMate: Your GPT-Powered Shell Assistant",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'command',
        choices=['explain', 'find'],
        help="Command to execute:\n  explain - Explain a command.\n  find - Find a command based on a description."
    )
    parser.add_argument(
        'input',
        help="Input to the command:\n  For 'explain' - The command to explain.\n  For 'find' - The description to find the command for."
    )
    parser.add_argument(
        '-os',
        default='linux',
        choices=['linux', 'windows', 'mac'],  # Updated to lowercase
        help="Specify the operating system. Options: linux, windows, mac (default: linux).\n"
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='Show this help message and exit.'
    )

    # Custom usage message
    parser.usage = parser.format_usage().replace("usage: ", "Usage:\n  ")

    # Custom examples section
    parser.epilog = 'Examples:\n' \
                    '  shellmate explain "ls -l" -os linux\n' \
                    '  shellmate find "how to see disk usage" -os windows\n'

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command == 'explain':
        result = explain_command(args.input, args.os)
    elif args.command == 'find':
        result = find_command(args.input, args.os)
    print(result)


if __name__ == "__shellmate__":
    shellmate()
