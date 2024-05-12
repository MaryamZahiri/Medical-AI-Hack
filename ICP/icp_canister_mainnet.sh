#!/bin/bash

dfx --version

dfx upgrade

dfx identity new MedAI

dfx identity use MedAI

DFX_CYCLES_LEDGER_SUPPORT_ENABLE=1

dfx cycles --network ic redeem-faucet-coupon FBAFE-7F598-5D476

dfx identity whoami

dfx ledger --network ic balance

dfx wallet --network ic redeem-faucet-coupon FBAFE-7F598-5D476

dfx ledger --network ic create-canister 2rhaq-2tmze-htcwu-dm6zo-tw4yx-ptcw7-dqwgo-yefxr-z3rtt-ndoka-4ae --amount .25