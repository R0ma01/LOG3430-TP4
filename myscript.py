# import os
# import sys
# import subprocess
#
# def get_last_good_commit():
#     try:
#         result = subprocess.run(
#             ["git", "rev-list", "-n", "1", "--skip=10", "HEAD"],
#             capture_output=True,
#             text=True,
#             check=True
#         )
#         return result.stdout.strip()
#     except subprocess.CalledProcessError:
#         print("Erreur: Impossible de trouver un commit stable.")
#         sys.exit(1)
#
# def run_git_bisect():
#     try:
#         bad_commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
#         good_commit = get_last_good_commit()
#
#         print(f"Bad commit: {bad_commit}")
#         print(f"Good commit: {good_commit}")
#
#
#         os.system(f"git bisect start {bad_commit} {good_commit}")
#
#
#         os.system("git bisect run pytest")
#
#
#         os.system("git bisect reset")
#     except Exception as e:
#         print(f"Erreur lors de l'exécution de git bisect: {e}")
#         sys.exit(1)
#

import os
if __name__ == "__main__":

    os.system("git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
    os.system("git bisect run pytest")
