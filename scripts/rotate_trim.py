from pathlib import Path
import cv2
import numpy as np

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="rotate and trim")
    parser.add_argument("dir", help="image_dir ")
    args = parser.parse_args()

    img_dir = Path(args.dir)
    out_dir = Path.home() / "rotate_trim" / img_dir.name
    print(img_dir, out_dir)

    for p in img_dir.glob("**/*.jpg"):
        outname = out_dir / p.relative_to(img_dir)
        img = cv2.imread(str(p))
        if img is None:
            continue
        rotated = np.rot90(img, 3).copy()
        h, w = rotated.shape[:2]
        yu = int(0.25 * h)
        outname.parent.mkdir(exist_ok=True, parents=True)
        cv2.imwrite(str(outname), rotated[yu:, :, :])
        print(outname)
