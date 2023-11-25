from mcolour import custom_style_text

if __name__ == "__main__":
    verse_snippet = """
Згрібайте жар руками голими
хапайте хвилю світову
степами вдаль біжіть розлогими
шукайте казку там нову
пливіть в човнах по морю синьому
знайдіте царство вічних змін
людина жах і біль свій кинь йому
бо все ж ти завжди тлін.
"""

    styled_verse = custom_style_text(
        verse_snippet,
        text_style="1",
        text_color="34m",
        background_color="45m"
    )

    print(styled_verse)