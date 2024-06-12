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
Install wasi2ic
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
Before deploy on mainnet:
```
<!-- Error: No wallet configured for combination of identity 'default' and network 'ic' by -->
dfx identity get-wallet --network ic

<!-- Worked -->
dfx identity get-wallet 

<!-- Worked -->
dfx identity get-principal

<!-- Error -->
dfx ledger create-canister $(dfx identity get-principal) --network ic
<!-- Error: Failed to transfer funds. Caused by: the debit account doesn't have enough funds to complete the transaction, current balance: 0.00000000 ICP -->

dfx wallet balance --network ic
<!-- Error: Failed to setup wallet caller.
Caused by: No wallet configured for combination of identity 'default' and network 'ic' -->

dfx cycles --network ic redeem-faucet-coupon <enter cycle>
<!-- Error: Failed 'redeem_to_cycles_ledger' call.
Caused by: The replica returned a rejection error: reject code CanisterReject, reject message Code is expired, used or not redeemable, error code None -->

<!-- Worked -->
dfx wallet --network ic redeem-faucet-coupon <enter cycle>

dfx deploy --network ic 
```
After deploy:
```
dfx canister id frontend
dfx identity list
dfx identity new MedAI --network ic
<!-- passphrase: -->
```
```
55A7B-5A44C-5E45B
Worked: A9A75-A9DFA-C54FD
Failed: FBAFE-7F598-5D476
```
https://internetcomputer.org/docs/current/developer-docs/ai/ai-on-chain
https://github.com/WebAssembly/wasi-sdk/tree/wasi-sdk-21