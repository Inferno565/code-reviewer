import argparse
import subprocess

from commiter import commit_msg

def git_commit(file_name):
    try:
        message = commit_msg(file_name)

        if file_name == ".":
            subprocess.run(["git", "add", "."], check=True)
        else:
            subprocess.run(["git", "add", file_name], check=True)

        subprocess.run(["git", "commit", "-m", message], check=True)
        print("Git commit successful.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Git commit failed.")


def main():
    parser = argparse.ArgumentParser(description="Automate Git commits")
    parser.add_argument(
        "filename", metavar="filename", type=str, nargs="+", help="Commit message"
    )

    args = parser.parse_args()
    filename = " ".join(args.filename)

    git_commit(filename)


if __name__ == "__main__":
    main()
