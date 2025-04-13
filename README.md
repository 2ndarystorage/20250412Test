# OpenAI ことわざジェネレーター

OpenAIのAPIを使用して日本のことわざをランダムに生成するPythonプログラムです。

## 機能

- OpenAI APIを使用して日本のことわざをランダムに生成
- ことわざとその意味を表示
- 環境変数からAPIキーを読み込み

## セットアップ

1. 必要なライブラリをインストール:
   ```
   pip install openai python-dotenv
   ```

2. `.env`ファイルにOpenAI APIキーを設定:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 使用方法

```
python main.py
```

または

```
python test/main.py
```

## 注意事項

- `.env`ファイルはGitで追跡されないため、APIキーが公開されることはありません
- APIキーが設定されていない場合はエラーメッセージが表示されます
