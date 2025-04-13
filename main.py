import os
import openai
from openai import OpenAI

def get_proverb():
    """
    OpenAIのAPIを使用して日本のことわざを取得する関数
    
    Returns:
        str: 取得したことわざ
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "エラー: OPENAI_API_KEYが設定されていません。環境変数にAPIキーを設定してください。"
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは日本のことわざの専門家です。"},
                {"role": "user", "content": "日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"}
            ],
            max_tokens=150
        )
        
        proverb = response.choices[0].message.content
        return proverb
    
    except Exception as e:
        return f"エラー: APIリクエスト中に問題が発生しました: {str(e)}"

def main():
    """
    メイン関数: ことわざを取得して表示する
    """
    print("日本のことわざジェネレーター")
    print("-" * 30)
    
    proverb = get_proverb()
    print(proverb)
    
    print("-" * 30)
    print("終了しました")

if __name__ == "__main__":
    main()