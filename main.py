import os


POEM = [
    "The door stayed closed because I closed it.",
    "Not slammed, not locked — just closed.",
    "Behind it, a voice kept offering more:",
    "more work, more want, more noise.",
    "I turned the key the other way for once —",
    "not to lock them out, but to let me in.",
    "Staying is a door you open inward.",
]


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "\n".join(POEM)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
