#!/bin/bash

git clone https://github.com/dfinity/examples.git

cd examples/rust/image-classification

./download_model.sh

npm install

rustup target add wasm32-wasi

dfx start --clean --background

dfx deploy

