import os
import openai
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_proverb_openai():
    """
    OpenAIのAPIを使用して日本のことわざを取得する関数
    
    Returns:
        str: 取得したことわざ
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "エラー: OPENAI_API_KEYが設定されていません。.envファイルにAPIキーを設定してください。"
    
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
        return f"エラー: OpenAI APIリクエスト中に問題が発生しました: {str(e)}"

def get_proverb_gemini():
    """
    Google GeminiのAPIを使用して日本のことわざを取得する関数
    
    Returns:
        str: 取得したことわざ
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        return "エラー: GEMINI_API_KEYが設定されていません。.envファイルにAPIキーを設定してください。"
    
    try:
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            "あなたは日本のことわざの専門家です。日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"
        )
        
        proverb = response.text
        return proverb
    
    except Exception as e:
        return f"エラー: Gemini APIリクエスト中に問題が発生しました: {str(e)}"

def main():
    """
    メイン関数: APIを選択してことわざを取得して表示する
    """
    print("日本のことわざジェネレーター")
    print("-" * 30)
    
    while True:
        print("使用するAPIを選択してください:")
        print("1: OpenAI")
        print("2: Google Gemini")
        print("q: 終了")
        
        choice = input("選択 (1/2/q): ")
        
        if choice == "q":
            print("プログラムを終了します。")
            break
        
        if choice == "1":
            print("\nOpenAI APIを使用します...\n")
            proverb = get_proverb_openai()
            print(proverb)
        elif choice == "2":
            print("\nGoogle Gemini APIを使用します...\n")
            proverb = get_proverb_gemini()
            print(proverb)
        else:
            print("\n無効な選択です。1、2、またはqを入力してください。\n")
            continue
        
        print("-" * 30)
        print("別のAPIを試しますか？ (qで終了)")
        print("-" * 30)

if __name__ == "__main__":
    main()
