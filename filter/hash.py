import check50

FILES = [
    "black_white_correct.png",
    "crop_correct.png",
    "reflect_correct.png",
    "blur_correct.png",
]

for file in FILES:
    print(check50.hash(file))
