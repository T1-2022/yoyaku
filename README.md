# t1-2022

## ディレクトリ説明

### app
アプリケーション全体のフォルダ

### static
cssやjavascriptを入れるためのディレクトリ

### templates
htmlを入れるためのディレクトリ

### .gitignore
開発に関係なくリポジトリに上げる必要のないものを
除くためのファイル

### requirements.txt
開発に必要なライブラリを書いておけば、以下のコマンドで一括インストール可能

```
pip install -r requirements.txt
```

## 開発について

* ベースとなるブランチは「develop」

```
git checkout develop
```

* developを最新状態にする

```
git pull origin develop
```

* branchを分ける

```
git branch 作業ブランチ名
```

* 作業ブランチに移動する

```
git checkout 作業ブランチ名
```

* 作業を行う

* 変更を追加

```
git add -A
```

* 変更をコミット（issue番号つけると分かりやすい，つけなくても可）

```
git commit -m "コメント #issue番号"
```

* 変更をリモートに送る

```
git push origin 作業ブランチ名
```

* 作業が完了したらプルリクエストをdevelopに送る

コメントに「close #issue番号」と記述すれば
自動的にissueが閉じられるはず

## 実行方法

app.pyがメインファイルとなる．

ルーティングファイルをBlue printを用いてapp.pyから参照する形で記述すると結合がスムーズだと思われる．

```
python app.py
```

ローカル環境はこのコマンドで実行できる.
本番環境用に後々書き換える必要性があるため要検討．
