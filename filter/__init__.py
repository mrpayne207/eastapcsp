import check50

HASHES = {
    "MEHS.jpg" : '963f6887460addafb99d302578f3c10ef688e924b6c8e9abebdda9a9c0df45fe',
    "black_white.png" : '56751daacaa452a8f11a35f5238aa6d896d9c37e993a32e10294add9b2a95abf',
    "crop.png" : '74061251f0ca818c9aa7f8b86e7bbb1efaa4031eb6422b4f755fc67285f6f1fd',
    "reflect.png" : 'ff0a8cb53a28ac9eab1ad02e92530af1999d8a14da62ad12770522b64962bbd1',
    "blur.png" : '7831d7d8a3730adb34222c65d9379db362729e5868d703fc2fd61e41f6a806bc',
}


@check50.check()
def exists():
    """filter.py exists"""
    check50.exists("filter.py")
    check50.include("MEHS.jpg")


@check50.check(exists)
def test_fewer_arguments():
    """filter.py exits given zero command-line arguments"""
    exit = check50.run("python3 filter.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")

@check50.check(exists)
def test_non_existent_file():
    """filter.py exits given a non-existent file"""
    exit = check50.run("python3 filter.py non_existent_file.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")

@check50.check(exists)
def test_more_arguments():
    """filter.py exits given more than two command-line arguments"""
    for file in ["MEHS.jpg", "MEHS1.jpg", "MEHS2.jpg"]:
        check50.include(file)
    exit = check50.run("python3 filter.py MEHS.jpg MEHS1.jpg MEHS2.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_black_white():
    """filter.py correctly filters black and white on MEHS.jpg"""
    test_shirt("black_white")


@check50.check(exists)
def test_crop():
    """filter.py correctly filters crop on MEHS.jpg"""
    test_shirt("crop")


@check50.check(exists)
def test_reflect():
    """filter.py correctly filters reflect on MEHS.jpg"""
    test_shirt("reflect")


@check50.check(exists)
def test_blur():
    """filter.py correctly filters blur on MEHS.jpg"""
    test_shirt("blur")


def test_shirt(photo):
    check50.include(photo)
    check50.run(f"python3 filter.py MEHS.jpg {photo[:-4]}").exit(0)
    hash = check50.hash(f"{photo[:-4]}_correct.png")
    if hash != HASHES[photo]:
        raise check50.Failure("Image does not match")
