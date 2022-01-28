Single-database configuration for Flask.

このフォルダはデータベースをmigrationによって管理すためのものです．
ファイルの追加や記述をする必要はありません．

## Migrateの手順

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