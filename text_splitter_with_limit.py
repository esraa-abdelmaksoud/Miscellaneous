

txt_str_len = 32000
txt = "*x "*(txt_str_len//2)
char_limit = 32700
if txt_str_len > char_limit:
    sets_num = (txt_str_len // char_limit) + 1
    loop  = 1
    prev_sep = 0
    while loop <= sets_num:
        sep = txt[prev_sep:(char_limit*loop)].rfind(" ")
        if (char_limit+prev_sep) > txt_str_len:
            left_text = txt[prev_sep:]
            print(f"{prev_sep}: end")
        else:
            left_text = txt[prev_sep:(sep+prev_sep)]
            print(f"{prev_sep}:{sep+prev_sep}")
        prev_sep += sep
        loop += 1
else:
    print(txt_str_len)