# データベースに関して

## データベース定義

### テーブル関係図
[関係図](../../参照/database_ver2.pdf)

### User
* table name    : users
* カラム
  * user_id     : 主キー，オートインクリメント（整数）
  * name        : ユーザーネーム(文字列，20文字上限)
  * email       : メールアドレス(文字列，50文字上限)
* リレーション
  * reserves  : ユーザーと紐づく予約一覧（リスト）
  * registers : ユーザーと紐づく1名の登録者(予約者)

* コンストラクタ：User(name, email)

### Register
* table name    : registers
* カラム
  * register_id   : 主キー，オートインクリメント（整数）
  * user_id       : ユーザーid（整数，外部キー）
  * passwd        : パスワード(文字列，30文字上限)
  * admin         : 管理者フラグ（Boolean）
* リレーション
  * reserves  : 登録者と紐づく予約一覧（リスト）
  * registers : 登録者と紐づく1名のユーザー

* コンストラクタ：User(passwd, admin, user_id=None)

### Conference
* table name    : conferences
* カラム
  * conference_id : 主キー，オートインクリメント（整数）
  * name          : 会議室名（文字列，20文字上限）
  * capacity      : 許容人数（整数）
  * fhoto_id      : 写真番号（整数）
  * remarks       : 備考（文字列，100文字上限）
* リレーション
  * reserves   : 会議室と紐づく予約一覧（リスト）
  * equipments : 会議室と紐づく備品一覧（リスト）

* コンストラクタ：Conference(name, capacity, fhoto_id, remarks)

### Reserve
* table name    : reserves
* カラム
  * reserve_id    : 予約id（整数，主キー，オートインクリメント）
  * regiser_id    : 予約者id（整数，外部キー）
  * conference_id : 会議室id（整数，外部キー）
  * date          : 日付（文字列，30文字上限） 
  * starttime     : 予約開始時間（文字列，30文字上限）
  * starttime     : 予約終了時間（文字列，30文字上限）
  * user_id       : ユーザーid（整数，外部キー）
  * purpose       : 目的（文字列，10文字上限）
  * remarks       : 備考（文字列，100文字上限）

* リレーション
  * registers   : 1名の予約者(Register)と紐づく
  * users       : 1名の利用者(User)と紐づく
  * conferences : 1つの会議室と紐づく

* コンストラクタ：Reserve(register_id, conference_id, date, starttime, endtime, purpose, remarks, user_id=None)

### Equipment
* table name    : equipments
* カラム
  * equipment_id     : 主キー，オートインクリメント（整数）
  * name             : 備品名(文字列，30文字上限)
* リレーション
  * conferences : 複数の会議室と紐づく
* コンストラクタ：Equipment(name)

### ConferenceEquipment
このテーブルは中間テーブルの役割なので、基本的には操作しない．

会議室等から備品数を取得する際にnumを参照する．

* table name    : conference_equipments
* カラム
  * id            : 備品・会議室id（整数，主キー，オートインクリメント）
  * conference_id : 会議室id（整数，外部キー）
  * equipment_id  : 予約者id（整数，外部キー）
  * num           : 備品の数（整数）

## データベース（SQL）の使い方
ここでは、基本的なCRUD操作について記述する．

詳細については、[SQLAlchemy](https://www.sqlalchemy.org/)や[基本的な使い方](https://qiita.com/tomo0/items/a762b1bc0f192a55eae8)を参照していただきたい．

また、例としてユーザーテーブルの操作を挙げているが、他のテーブル名に置き換えれば動作する．

### Create （データの追加）
* テーブル単体での追加
```
# データベースインスタンスを読み込む
from models.database import db

# ユーザーをインスタンス化
user = User(name='tarou', email='tarou@example.com')

# 追加する
db.session.add(user)
# 仮にデータベースに反映させる（エラー処理等に使える）
db.session.flush()
# 実際にデータベースに反映させる
db.session.commit()
```
以下に，リレーションを用いた便利な方法を記述する．
* リレーションと同時にユーザー登録を行う（リレーションが1名の場合）

ユーザーをリレーションに追加すれば自動的にユーザーテーブルにも追加される．
```
# 登録者を作成する
register = Register('passwd', False)
# リレーションにユーザーを追加
register.users = User('豊橋花子', 'hanako@example.com')
db.session.add(register)
db.session.flush()
db.session.commit()
# 自動的にUserテーブルに豊橋花子が追加される
```
* リレーションと同時に備品登録を行う（リレーションが複数の場合）

リレーションが複数の場合（仕様のリスト表記があるもの）はリストとして扱う
```
conference = Conference('会議室A', 60, 1, '特になし')
conference.equipments.append(Equipment('プロジェクター'))
db.session.add(conference)
db.session.flush()
db.session.commit()
```

### Read (データの読み出し)
* リレーションなし
```
# 全てのユーザーの読み込み
users = User.query.all()
# 名前でフィルターを掛ける(1人の)場合
user = db.session.query(User).filter_by(name='tarou').first()
# 変数名．キーで中身の値を取り出せる．（キーは各テーブルの仕様参照）
print(user.name)
```
* リレーションあり
```
# 予約の取得
reserve = db.session.query(Reserve).filter(Reserve.id==1).first()
# リレーションを張ったユーザー（1名）が取得できる
user = reserve.users
# リレーションを張った会議（1部屋）が取得できる
conference = reserve.conferences
```
* 特殊事例：中間テーブルの情報を取り出す方法

[参考](https://qiita.com/shirakiya/items/6faf3ed05e959f135e52)の中間テーブルに
カラムがある場合の方法を参考にしてデータを取得してください．

### Delete（データの削除）
* リレーション無し
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
* リレーションあり

リレーションなしの場合と削除方法は変わらないが、
以下の関係性が成り立っていることに注意してもらいたい．

* UserとRegister
  * Userを削除した場合Registerも削除される
  * Registerを削除した場合Userは削除されない
* ConferenceとEquipment
  * 会議室を削除した際に備品は削除されない
  * 備品を削除した際に会議室は削除されない
* Reserveと(User, Register, Conference)
  * 予約を削除した際に会議室，予約者，利用者を削除しない
  * 会議室を削除した際に予約を削除する(予約者，利用者は削除されない)
  * 予約者を削除した際に予約を削除する(会議室，利用者は削除されない)
  * 利用者を削除した際に予約を削除する(会議室，予約者は削除されない)
  * ただし、利用者と予約者が同一だった場合は、UserとRegisterの関係により処理される

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
* 特定の情報を更新すれば、リレーション先の情報も自動的に書き換わる

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