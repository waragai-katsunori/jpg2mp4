from pathlib import Path

import cv2
import numpy as np

if __name__ == "__main__":
    """
    Concatenate images and save as a mp4 file.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Concatenate images and save as a mp4 file")
    parser.add_argument("dir", help="image_dir ")
    parser.add_argument("dir2", help="image_dir2 ")
    args = parser.parse_args()

    img_dir1 = Path(args.dir)
    img_list1 = sorted(img_dir1.glob("*.jpg"))
    img_dir2 = Path(args.dir2)
    img_list2 = sorted(img_dir2.glob("*.jpg"))

    assert img_dir1.is_dir()
    assert img_dir2.is_dir()

    writer = None
    for i, (p1, p2) in enumerate(zip(img_list1, img_list2)):
        print(p1, p2)
        cvimg1 = cv2.imread(str(p1))
        cvimg2 = cv2.imread(str(p2))
        if cvimg1 is None:
            continue

        concat = np.hstack([cvimg1, cvimg2])
        if writer is None:
            out_movei_name = Path.home() / f"{img_dir1.stem}_cat.mp4"
            apiPreference = 0
            codec = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 15
            size = (concat.shape[1], concat.shape[0])
            print(f"{size=}")
            writer = cv2.VideoWriter(str(out_movei_name), apiPreference, fourcc=codec, fps=fps, frameSize=size)


        print("write", i, p1)
        writer.write(concat)

    writer.release()
    print(f"saved as {out_movei_name}")
