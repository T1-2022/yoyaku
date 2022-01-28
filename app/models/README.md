# データベースに関して

## データベース定義
ここにデータベースの定義を書く．

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
```
# 全てのユーザーの読み込み
users = User.query.all()
# 名前でフィルターを掛ける(1人の)場合
user = db.session.query(User).filter_by(name='tarou').first()
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
