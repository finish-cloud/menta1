# 検索ツールサンプル
# これをベースに課題の内容を追記してください
import pandas as pd
# 検索ソース

# 検索ツール


def search():

    df = pd.read_csv("./Book1.csv")
    source = list(df["name"])

    while True:

        word = input("鬼滅の登場人物の名前を入力してください >>> ")

        # ここに検索ロジックを書く

        if word in source:
            print("{}が見つかりました".format(word))
        else:
            print("{}は見つかりませんでした".format(word))
            # 追加
            add_chara = input("追加登録しますか？(0:しない 1:する)　＞＞　")
            if add_chara == "1":
                source.append(word)

        df = pd.DataFrame(source, columns=["name"])
        df.to_csv("./Book1.csv", encoding="utf_8-sig",
                  index=False,  header=False)
        print(source)


# CSV ファイル (employee.csv) として出力
# df.to_csv("employee.csv", index=False, encoding="utf-8", mode='a')

if __name__ == "__main__":
    search()
