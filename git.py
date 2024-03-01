import argparse
import subprocess


def git_commit(message):
    try:
        # Run 'git add .' to stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Run 'git commit -m "<message>"' to commit changes with the specified message
        subprocess.run(["git", "commit", "-m", message], check=True)

        print("Git commit successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Git commit failed.")


def main():
    parser = argparse.ArgumentParser(description="Automate Git commits")
    parser.add_argument(
        "message", metavar="message", type=str, nargs="+", help="Commit message"
    )

    args = parser.parse_args()
    message = " ".join(args.message)

    git_commit(message)


if __name__ == "__main__":
    main()
