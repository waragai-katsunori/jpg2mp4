from pathlib import Path

import cv2

if __name__ == "__main__":
    """
    Convert movie file in jpeg files.
    """
    import argparse
    parser = argparse.ArgumentParser(description="jpg2mp4 converter")
    parser.add_argument("movie_file", help="movie file(.mp4, .avi, .webm) to jpgs ")
    args = parser.parse_args()

    movie_file = Path(args.movie_file)
    assert movie_file.suffix in (".mp4", ".avi", ".webm")
    cap = cv2.VideoCapture(str(movie_file))

    outdir = Path.home() / f"{movie_file.stem}"
    outdir.mkdir(exist_ok=True)
    counter = -1
    while True:
        ret, cvimg = cap.read()
        if cvimg is None:
            break
        counter += 1
        oname = outdir / f"{movie_file.stem}_{counter:04d}.jpg"
        cv2.imwrite(str(oname), cvimg)
    print(f"saved to {outdir}")
