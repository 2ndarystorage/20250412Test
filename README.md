# ことわざジェネレーター

OpenAIまたはGoogle GeminiのAPIを使用して日本のことわざをランダムに生成するPythonプログラムです。

## 機能

- OpenAIまたはGoogle Gemini APIを使用して日本のことわざをランダムに生成
- 使用するAPIをユーザーが選択可能
- ことわざとその意味を表示
- 環境変数からAPIキーを読み込み

## セットアップ

1. 必要なライブラリをインストール:
   ```
   pip install openai google-generativeai python-dotenv
   ```

2. `.env`ファイルにAPIキーを設定:
   ```
   # OpenAI API Key
   OPENAI_API_KEY=your_openai_api_key_here
   # Google Gemini API Key
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 使用方法

```
python main.py
```

プログラム実行後、使用するAPIを選択します:
1. OpenAI
2. Google Gemini
q. 終了

## 注意事項

- `.env`ファイルはGitで追跡されないため、APIキーが公開されることはありません
- APIキーが設定されていない場合はエラーメッセージが表示されます
- 各APIの利用には、それぞれのサービスでのアカウント登録とAPIキーの取得が必要です
