"""
Week 5 Consultation Questions
Practice with reading & writing files
"""


def append_to_file(pth, line):
    """Appends the new line to the file located at pth

    Parameters
    ----------
    pth : str
        Full path of the file to write to.

    line: str
        New line to be appended to the file

    """
    # <COMPLETE THIS PART>
    with open(pth,mode ='at') as fobj:
        fonj.write(line)
    fobj = open(pth,'at')




def replace_line_words(line, new_words):
    """
    Replace the words of `line` that are among the keys
    of the `new_words` dictionary with their corresponding values
    将`line`中属于`new_words`字典键的单词替换成相应的值。

    Parameters
    ----------
    line : str
        String to be modified

    new_words: dict
        Dictionary of the format {<old_word> : <new_word>} where
            - <old_word> is a word within `line` that should be replaced
            - <new_word> is the word that <old_word> should be replaced with within `line`

    Notes
    -----
    For example, given:
    new_words = {'hello' : 'bye}
    line = 'Hello there hello'

    This function should return
    'Bye there bye'

    Returns
    -------
    str
        A copy of `line` but with its words replaced based on `new_words`

    """
    # <COMPLETE THIS PART>
    new_line = []
    for word in line.split():
        if word in new_words.keys():
            new_line.append(new_words[word])
        elif word.lower() in new_words.keys():
            new_line.append(new_words[word.lower()]).title()
        else:
            new_line.append(word)

    return " ".join(new_line)









def create_modified_file(old_file_pth, new_file_pth, new_words):
    """
    Create a new file called `new_file_pth` that is the exact same as
    `old_file_pth`, but with its words replaced according to the `new_words` dictionary.
    Words not found in the `new_words` dictionary should be left unchanged.

    Parameters
    ----------
        old_file_pth: str
            Path of the original file

        new_file_pth: str
            Path of new file created containing replaced words

        new_words: dict
            Dictionary of the form {<old_word> : <new_word>}

    Notes
    -----
    The text in `old_file_pth` should be left unmodified.

    """
    # <COMPLETE THIS PART>


if __name__ == "__main__":
    # ori_file = 'lyrics.txt'
    # new_file = 'modified_lyrics.txt'
    # words_replacement = {
    #     'life': 'new_life',
    #     'no': 'new_no',
    #     'open': 'new_open',
    #     'me': 'new_me',
    # }
    #
    # create_modified_file(ori_file, new_file, words_replacement)

    pass