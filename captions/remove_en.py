"""
Removes .en from caption filenames.
  S1E1.en.srt  ->  S1E1.srt

Usage:
    python remove_en.py "D:\\TheAvatarHub\\captions"
"""

import os
import re
import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: python remove_en.py "D:\\TheAvatarHub\\captions"')
        sys.exit(1)

    captions_folder = sys.argv[1]

    for folder_name in os.listdir(captions_folder):
        folder_path = os.path.join(captions_folder, folder_name)
        if not os.path.isdir(folder_path):
            continue

        for fname in os.listdir(folder_path):
            if not fname.lower().endswith('.srt'):
                continue
            new_name = re.sub(r'\.en\.srt$', '.srt', fname, flags=re.IGNORECASE)
            if new_name != fname:
                os.rename(os.path.join(folder_path, fname), os.path.join(folder_path, new_name))
                print(f"  {fname} -> {new_name}")

    print("Done!")


if __name__ == '__main__':
    main()
