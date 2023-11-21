def is_spam_words(text, spam_words, space_around=False):
    textl = text.lower()
    words1 = [w.lower() for w in spam_words]

    if any(w in textl for w in words1):
        if space_around==False:
            return True
        else:
            # check left and right
            for w in words1:
                if (f' {w}' in textl or textl.startswith(w)) and (textl.endswith(w) or textl.endswith(f'{w}.') or f'{w} ' in textl):
                    return True
    return False

print(is_spam_words('The atmosphere at the match was terrifying.', ['match'], True))