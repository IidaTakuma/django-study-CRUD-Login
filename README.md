### todoアプリ

#### CRUD

- 投稿機能

- 閲覧機能

- 編集機能

- 削除機能

#### ログイン機能

- サインアップ
- ログイン
- ログアウト





### 仕様

Todoリスト(メインページ)

- 投稿者の、タイトル、投稿日、投稿者を表示
- ログイン中のユーザを表示
- ログイン、ログアウトのボタンを表示
- 新規投稿ボタン
- ログインしていないユーザがアクセスするとログインページへ行く

詳細ページ

- 投稿者の、タイトル、詳細、投稿日、投稿者を表示
- 編集ボタンを表示
- 削除ボタンを表示
- 完了ボタンを表示

編集ページ

- フォーム(タイトル、詳細)
- フォームには編集前の文章が表示
- 完了ボタン

新規作成ページ

- フォーム(タイトル、詳細)
- 完了ボタン

サインアップページ

- フォーム(ユーザ名、パスワード)
- 完了ボタン

ログイン画面

- フォーム(ユーザ名、パスワード)

- 完了ボタン



#### モデル

User

Memo

- タイトル(文字列)
- 詳細(文字列)
- 完了の是非(真偽値)
- 投稿日
- 紐づけられているユーザ
- 