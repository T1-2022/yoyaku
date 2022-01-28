# データベースに関して

## データベース定義

### User
* table name    : users
* id     : 主キー，オートインクリメント（整数）
* name   : ユーザーネーム(文字列，20文字上限)
* email  : メールアドレス(文字列，50文字上限)
* passwd : パスワード(文字列，30文字上限)
* admin  : 管理者フラグ（Boolean）

* reserve : ユーザーと紐づく予約一覧

* コンストラクタ：User(name, email, passwd, admin)

### Conference
* table name    : conferences
* id            : 主キー，オートインクリメント（整数）
* name          : 会議室名（文字列，20文字上限）
* capacity      : 許容人数（整数）
* equipment     : 備品（文字列，30文字上限）
* fhoto_id      : 写真番号（整数）
* remakes       : 備考（文字列，100文字上限）

* reserve : 会議室と紐づく予約一覧

* コンストラクタ：Conference(name, capacity, equipment, fhoto_id, remarks)

### Reserve
* table name    : reserves
* id            : 予約id（整数，主キー，オートインクリメント）
* user_id       : ユーザーid（整数，外部キー）
* conference_id : 会議室id（整数，外部キー）
* date          : 日付（文字列，30文字上限） 
* time          : 時間（文字列，30文字上限）
* user_name     : 利用者名（文字列，20文字上限）
* user_email    : 利用者メールアドレス（文字列，50文字上限）
* purpose       : 目的（文字列，100文字上限）
* remakes       : 備考（文字列，100文字上限）

* user : 1名のユーザと紐づく
* conference : 1つの会議室と紐づく

* コンストラクタ：Reserve(user_id, conference_id, date, time, user_name, user_email, purpose, remarks)

## データベース（SQL）の使い方
ここでは、基本的なCRUD操作について記述する．

詳細については、SQLAlchemyを参照していただきたい．

また、例としてユーザーテーブルの操作を挙げているが、他のテーブル名に置き換えていただければ動作する．

### Create （データの追加）
```
# データベースインスタンスを読み込む
from models.database import db

# ユーザーをインスタンス化
user = User(name='tarou', email='tarou@example.com', passwd='passwd', admin=False)

# 追加する
db.session.add(user)
# 仮にデータベースに反映させる（エラー処理等に使える）
db.session.flush()
# 実際にデータベースに反映させる
db.session.commit()
```
### Read (データの読み出し)
リレーションなし
```
# 全てのユーザーの読み込み
users = User.query.all()
# 名前でフィルターを掛ける(1人の)場合
user = db.session.query(User).filter_by(name='tarou').first()
```
リレーションあり
```
# 予約の取得
reserve = db.session.query(Reserve).filter(Reserve.id==1).first()
# リレーションを張ったユーザーが取得できる
user = reserve.user
# リレーションを張ったユーザーが取得できる
conference = reserve.conference
```

### Delete（データの削除）
```
# ユーザーの読み出し(read)
user = db.session.query(User).filter_by(name='tarou').first()

# 削除する
db.session.delete(user)
# 仮にデータベースに反映させる（エラー処理等に使える）
db.session.flush()
# 実際にデータベースに反映させる
db.session.commit()
```

### Update（データの更新）
```
# ユーザーの読み出し(read)
user = db.session.query(User).filter_by(name='tarou').first()
# メールアドレスの変更
user.email = 'tarou@example.com'

# 更新する
db.session.add(user)
# 仮にデータベースに反映させる（エラー処理等に使える）
db.session.flush()
# 実際にデータベースに反映させる
db.session.commit()
```

## データベースの確認方法

### 起動
sqliteコマンドでデータベースを開く．
```
sqlite3 test.db
```

### 終了
```
sqlite > .quit
```

### テーブル一覧
テーブル一覧を表示
```
sqlite > .table
```

### テーブルの中身取得
テーブルからデータを取得して表示するSQL文．

usersを任意のテーブル名にすることで表示可能．
```
sqlite > select * from users;
```

### テーブルの要素一覧
テーブル要素についての情報が見られる．
```
sqlite > .schema
```

## メンテナンス用

1. migrateを行ってデータベース更新

2. flask shellを使ったテスト

### Migrateの手順

1. migration設定の初期化 （初回のみ）

```
flask db init
```

2. migrationファイルの作成

前回との差分をmigrationファイルとして生成．

```
flask db migrate
```

3. migrationの実行

migrationファイルを実行する．（実際の書き換え）

```
flask db upgrade
```

※バージョンを戻す（rollback）

```
flask db downgrade
```

※要注意：データベースを最初に戻す

```
flask db upgrade head
```