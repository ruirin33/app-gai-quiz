import streamlit as st

def quiz_app():
    st.title('クイズアプリ')

    # クイズデータ（例）
    quiz_data = [
        {
            'question': '次のうち、最も大きな惑星はどれ？',
            'options': ['地球', '木星', '金星', '火星'],
            'correct_answer': '木星',
            'explanation': '木星は太陽系で最も大きな惑星です。'
        },
        {
            'question': '水の化学式は？',
            'options': ['H2O', 'CO2', 'O2', 'N2'],
            'correct_answer': 'H2O',
            'explanation': '水の化学式はH2Oです。'
        },
        # 他の問題も同様に追加
    ]

    # ユーザの回答と正解を保持するリスト
    user_answers = []
    correct_answers = []

    # クイズを表示するループ
    for i, quiz in enumerate(quiz_data, start=1):
        st.subheader(f'Question {i}: {quiz["question"]}')
        selected_option = st.radio(f'選択肢 - Question {i}', quiz['options'])
        user_answers.append(selected_option)
        correct_answers.append(quiz['correct_answer'])
        st.write('')  # スペースを追加して見た目を改善

    # すべての問題に回答した後に回答ボタンを表示する
    if st.button('すべての問題に回答する'):
        st.subheader('解説')
        correct_count = 0  # 正解数をカウントするための変数

        for i, quiz in enumerate(quiz_data):
            st.write(f'Question {i + 1}: {quiz["question"]}')
            st.write(f'あなたの回答: {user_answers[i]}')
            st.write(f'正解: {quiz["correct_answer"]}')

            if user_answers[i] == quiz['correct_answer']:
                st.success('結果: 正解')
                correct_count += 1
            else:
                st.error('結果: 不正解')

            st.info(f'解説: {quiz["explanation"]}')
            st.markdown('---')  # 区切り線を追加して見た目を整える

        # 正答率を計算して表示
        total_questions = len(quiz_data)
        accuracy = correct_count / total_questions * 100
        
        st.markdown('## 最終結果')
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="正解数", value=f"{correct_count}/{total_questions}")
        with col2:
            st.metric(label="正答率", value=f"{accuracy:.1f}%")
        
        # 正答率に応じてメッセージを表示
        if accuracy == 100:
            st.balloons()
            st.success('完璧です！おめでとうございます！')
        elif accuracy >= 80:
            st.success('素晴らしい成績です！')
        elif accuracy >= 60:
            st.info('よく頑張りました！')
        else:
            st.warning('もう少し頑張りましょう！')

if __name__ == '__main__':
    quiz_app()