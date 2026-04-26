import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Seed Timeseries Generator Wrapper")
    parser.add_argument(
        "--ecosystem",
        type=str,
        default="all",
        choices=["all", "scoop_shovel", "chocolatey", "winget"],
        help="Which ecosystem to seed",
    )
    args = parser.parse_args()

    rust_dir = os.path.join(os.path.dirname(__file__), "seed_generator")

    print("[*] Building Rust seed generator (this takes a moment on first run)...")
    try:
        subprocess.run(["cargo", "build", "--release"], cwd=rust_dir, check=True)
    except Exception as e:
        print(f"[!] Failed to compile Rust seed generator: {e}")
        print("[!] Ensure you have the Rust toolchain installed (https://rustup.rs/)")
        sys.exit(1)

    print("[*] Executing blazing-fast Rust generator...")
    try:
        subprocess.run(
            ["cargo", "run", "--release", "--", "--ecosystem", args.ecosystem],
            cwd=rust_dir,
            check=True,
        )
    except Exception as e:
        print(f"[!] Rust generator failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
