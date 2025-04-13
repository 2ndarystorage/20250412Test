import os
import openai
from openai import OpenAI

def get_proverb():
    """
    OpenAI��API���g�p���ē��{�̂��Ƃ킴���擾����֐�
    
    Returns:
        str: �擾�������Ƃ킴
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "�G���[: OPENAI_API_KEY���ݒ肳��Ă��܂���B���ϐ���API�L�[��ݒ肵�Ă��������B"
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "���Ȃ��͓��{�̂��Ƃ킴�̐��Ƃł��B"},
                {"role": "user", "content": "���{�̂��Ƃ킴�������_����1�����Ă��������B���Ƃ킴�Ƃ��̈Ӗ����Ȍ��ɐ������Ă��������B"}
            ],
            max_tokens=150
        )
        
        proverb = response.choices[0].message.content
        return proverb
    
    except Exception as e:
        return f"�G���[: API���N�G�X�g���ɖ�肪�������܂���: {str(e)}"

def main():
    """
    ���C���֐�: ���Ƃ킴���擾���ĕ\������
    """
    print("���{�̂��Ƃ킴�W�F�l���[�^�[")
    print("-" * 30)
    
    proverb = get_proverb()
    print(proverb)
    
    print("-" * 30)
    print("�I�����܂���")

if __name__ == "__main__":
    main()