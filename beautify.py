def beautify(fn):
    with open(fn,encoding="utf-8") as f:
        text = f.read()
    text = text.replace('（','(').replace('）',')').replace('，',',').replace('”','"')
    with open(fn,'w',encoding="utf-8") as f:
        f.write(text)
beautify('enums.py')