from pathlib import Path

import cv2

if __name__ == "__main__":
    """
    Convert jpg files in image_dir to mp4 file.
    """
    import argparse
    parser = argparse.ArgumentParser(description="jpg2mp4 converter")
    parser.add_argument("dir", help="image_dir ")
    args = parser.parse_args()

    img_dir = Path(args.dir)
    img_list = sorted(img_dir.glob("*.jpg"))
    writer = None
    for i, p in enumerate(img_list):
        print(p)
        cvimg = cv2.imread(str(p))
        if cvimg is None:
            continue

        if writer is None:
            out_movei_name = Path.home() / f"{img_dir.stem}.mp4"
            apiPreference = 0
            codec = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 15
            size = (cvimg.shape[1], cvimg.shape[0])
            print(f"{size=}")
            writer = cv2.VideoWriter(str(out_movei_name), apiPreference, fourcc=codec, fps=fps, frameSize=size)


        print("write", i, p)
        writer.write(cvimg)

    writer.release()
    print(f"saved as {out_movei_name}")
