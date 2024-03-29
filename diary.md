# 日誌

## 2022/4/8

- ラズパイのLEDをつけた
- sshしてラズパイを動かした。

### テーマ決め

- 金魚にLINEから餌をやる
    - 水温監視する
- 勉強してた時に昼寝していたら音がなる(警告)
- 雨が降ってきたら洗濯物を入れるように教えてくれる, 
    - 洗濯物退避
- 家電製品のリモコン
- 顔認識を使う?
- 電光掲示板
- twitterのデータを見て感情分析してその色に光らせる。
- モバイルルーター
- ドライブレコーダー
- 音楽プレイヤー
- ボタンを押して音声認識して, slackにその内容を送る。

### これまでのもの

- ドローン
- 囲碁将棋
- 噴水
- ゲームの審判
- アレクサ
- 食堂の混雑状況を通知する
- 控室の鍵を顔認証化
- 講義室の空席数をLEDで表示
- 目覚まし時計(起きないと寝顔アップロード)

### 投票後

下の二つのいずれかにするために, やるべきことを考える。
- 金魚に餌をやる。
    - LINEでメッセージを送ると, 餌をやってその様子をカメラで送ってくれる
    - カメラで金魚の様子を送る。
    - ソフトウェア
        - LINE or Slack API
    - ハードウェア
        - 餌を自動でやる仕組み
        - モーター

- 天気予報を電光掲示板とslack伝言板で表示する。
    - 予算は大丈夫そう
    - 表示するもの
        - 天気, 伝言, 予定(学科の)
    - ソフトウェア
        - Slack API
        - 電光掲示板の制御
        - 伝言を音声認識する?
    - ハードウェア
        - 電光掲示板

### テーマ決定!
電光掲示板を作ることに決定しました。

### 機能
- 電光掲示板に文章, 天気を表示する。
    - 天気を取得する
    - utasの予定を取得する(できるのか?)
- slackにメッセージを打つと, slackから電光掲示板に内容を表示する。
- 控室でボタンを押すと音声認識を開始して, 伝言をslackと電光掲示板に送る。

### 必要なもの
- slack API
- [google cloud platform](https://cloud.google.com/speech-to-text?hl=ja)
- 電光掲示板の制御(ハードウェア&ソフトウェア) 

### 来週までに調べること

- 井上, 犬飼
    - slack APIとutasの情報取得をする。
- 楠井
    - speech to textについて調べる。
- 片山
    - 電光掲示板について(どれを買うか)。
- 杉江
    - 天気予報を取得するAPI。

## 2022/4/15

### やってきたこと

- 井上
    - slackワークスペースを作って実験

- 犬飼
    - utasから直接

- 片山
    - 電光掲示板を買った
    - ACアダプタとかはあるものでなんとかなりそう

- 楠井
    - amazon translate
    - tutorialがあった

- 杉江
    - 気象庁のAPIがある。

- 言語はpython

### 今日の成果

- gitにpushした。
- 天気のAPIを呼ぶのはできた。
- ラズパイと電光掲示板を繋いだ(配線の仕方?)。
- 電光掲示板に表示した。
- 音声の録音ができた。
- 電光掲示板自体の電源が必要?
- 基盤が必要?
- ラズパイの刺すところが足りない

### 買うもの
- ボタン
- 電源

## 2022/4/22

- ボタンを押して押されたら関数を呼ぶことができるようになった。
- voc2txtを呼び出すことができるようになった。
- 画面に映すのはできるようになった
- ワニ口は届くのを待つ。

### 残りやるべきこと

- 電光掲示板
    - 日本語フォント
    - 数秒で終わるようにする

- 日程
    - 日程をメッセージから取得してcsvで永続化して,ある時間になったらタイマーを発火する?
    - データベース使ってもいい

- ワニ口
    - ACアダプタと繋げる。

- 全体的に
    - formatを綺麗にして出力する。

## 2022/5/6

- 電光掲示板日本語フォントに対応した
- slackからメッセージを読んでそれを予定に追加できるようになった

## 2022/5/20

- 電光掲示板の表示の揺れていたのを直した
- 電光掲示板の文字が重ならないようにした
- あとメッセージの種類がみてわかるようにしたい

## 2022/5/27

- タイトル考えた
- メッセージの色を種類ごとに変えた
- 物理的なものを作った

## 2022/5/30

- スライドをつくる
- 担当範囲を決める
- リアルラズベリーパイを作る計画
- 実物のバランス調整

### todo

- ラズパイの設定をしないと発表する場所で動かない?
- 発表練習
- ラズベリーパイを作る
