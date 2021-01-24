# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import sys

from library1.hello import say_hello
from library2.greetings import greetings


if __name__ == '__main__':
    say_hello()
    greetings()
