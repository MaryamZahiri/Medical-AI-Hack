#!/bin/bash

sh -ci “$(curl -fsSL https://internetcomputer.org/install.sh)”
sh -ci “$(curl -fsSL https://raw.githubusercontent.com/dfinity/sdk/dfxvm-install-script/install.sh)”
DFX_VERSION=0.15.1 sh -ci “$(curl -fsSL https://raw.githubusercontent.com/dfinity/sdk/dfxvm-install-script/install.sh)”

# https://internetcomputer.org/docs/current/developer-docs/getting-started/install/#python
