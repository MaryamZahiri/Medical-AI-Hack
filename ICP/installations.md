[Image Classification](https://internetcomputer.org/docs/current/developer-docs/ai/ai-on-chain)
[wasi](https://github.com/WebAssembly/wasi-sdk/tree/wasi-sdk-21)
[wasi2ic](https://github.com/wasm-forge/wasi2ic/tree/main)
```
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```
```
sh -ci "$(curl -fsSL https://internetcomputer.org/install.sh)"
```
```
apt-get install wget
```
For wasi:
```
# Install necessary packages
apt-get update && \
apt-get install -y --no-install-recommends \
cmake \
clang \
ninja-build \
wget \
curl
```
```
# Clean up APT when done
apt-get clean && rm -rf /var/lib/apt/lists/*
```
Install wasi
```
export WASI_VERSION=21
export WASI_VERSION_FULL=${WASI_VERSION}.0
wget https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-${WASI_VERSION}/wasi-sdk-${WASI_VERSION_FULL}-linux.tar.gz
tar xvf wasi-sdk-${WASI_VERSION_FULL}-linux.tar.gz
```
```
export WASI_SDK_PATH=`pwd`/wasi-sdk-${WASI_VERSION_FULL}
CC_wasm32_wasi="${WASI_SDK_PATH}/bin/clang --sysroot=${WASI_SDK_PATH}/share/wasi-sysroot"
```
wasi2ic
```
  git clone https://github.com/wasm-forge/wasi2ic
  cargo update
  rustup update
  <!-- Based on new version -->
  rustup install 1.76.0
  cd wasi2ic
  git pull
  cargo build
  cargo install --path .
  <!-- Check wasi2ic binary in output -->
  ls target/release
  cp target/release/wasi2ic /usr/local/bin/
```
After deploy:
```
dfx canister id frontend
```
https://internetcomputer.org/docs/current/developer-docs/ai/ai-on-chain
https://github.com/WebAssembly/wasi-sdk/tree/wasi-sdk-21