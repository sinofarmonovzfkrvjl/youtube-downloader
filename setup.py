from setuptools import setup, find_packages

setup(
    name="youtube_downloader",
    version="0.0.1",
    description="A package to download youtube videos and audio from youtube",
    author="Sino Farmonov",
    url="https://github.com/sinofarmonovzfkrvjl/youtube-downloader",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=["requests"]
)
