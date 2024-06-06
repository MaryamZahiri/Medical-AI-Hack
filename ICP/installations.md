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
https://internetcomputer.org/docs/current/developer-docs/ai/ai-on-chain
https://github.com/WebAssembly/wasi-sdk/tree/wasi-sdk-21