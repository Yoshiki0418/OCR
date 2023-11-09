from PIL import Image
import pyocr


# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
txt = engine.image_to_string(Image.open('1-1.png'), lang="jpn")
# 「Test Message」が出力される

with open("Test.text", mode = "w" , encoding = "utf-8" ) as f:
    for i in txt:
        f.write(i)

with open("Test.text", mode = "r" , encoding = "utf-8" ) as f:
    a = []
    data = f.read()
    lines = data.split('\n')
    for ans in lines:
        ans = ans.replace("合      計", "合計") 
        ans = ans.replace("合    計","合計")
        ans = ans.replace(' ', '')
        ans = ans.replace("@",'')
        ans = ans.replace("画","")
        ans = ans.replace("園","")
        a.append(ans)

with open("Test2.text", mode = "w" , encoding = "utf-8" ) as f:
    for i in a:
        if "年" in i or "茶碗" in i:
            data1 = str(i) + "\n"
            f.write(data1)
        if "円" in i:
            data1 = str(i) + "\n"
            f.write(data1)
        if "\\" in i:
            if "消費税" not in i or "お預り" not in i or "お釣" not in i:
                data1 = str(i) + "\n"
                f.write(data1)