# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:24:56 2022

@author: alber
"""

import streamlit as st
import pandas as pd

# ページのタイトル設定
st.set_page_config(
    page_title="あなたの未来のキャリア",
)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = "main"
    st.session_state.answers = []

# 各種メニューの非表示設定
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 最初のページ
def main():
    st.markdown(
        "<h1 style='text-align: center;'>あなたの未来のキャリア</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer0)
        st.session_state.page_id = "page1"

    with st.form("f0"):
        st.radio("就活についての今の気持ちは？", ["就活したくない", "就活しないといけない", "就活ってどういうことをするんだろう", "就活頑張りたい", "就活についていろいろ知りたい"], key="answer0")
        st.form_submit_button("スタート！", on_click=change_page)


# 問題１
def page1():
    st.markdown(
        "<h1 style='text-align: center;'>第１問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer1)
        st.session_state.page_id = "page2"

    with st.form("f1"):
        st.radio("あなたが重視するのは？", ["仕事のやりがい", "ワークライフバランス"], key="answer1")
        st.form_submit_button("回答", on_click=change_page)


# 問題２
def page2():
    st.markdown(
        "<h1 style='text-align: center;'>第２問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer2)
        st.session_state.page_id = "page3"

    with st.form("f2"):
        st.radio("長野県内で就職したい？", ["長野県内", "県外に行きたい", "海外に行きたい"], key="answer2")
        st.form_submit_button("回答", on_click=change_page)


# 問題３
def page3():
    st.markdown(
        "<h1 style='text-align: center;'>第３問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer3)
        st.session_state.page_id = "page4"

    with st.form("f3"):
        st.radio("あなたの学部は？", ["まだ高校生", "人文学部", "教育学部", "経法学部", "理学部", "医学部", "工学部", "農学部", "繊維学部", "大学院"], key="answer3")
        st.form_submit_button("回答", on_click=change_page)


# 問題４
def page4():
    st.markdown(
        "<h1 style='text-align: center;'>第４問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer4)
        st.session_state.page_id = "page5"

    with st.form("f4"):
        st.multiselect("どんな業種に興味がある？", ["メーカー", "商社", "IT・情報処理", "専門・技術サービス業", "官公庁・団体", "教育機関", "運輸・倉庫", "流通","サービス", "金融", "エネルギー", "医療・福祉施設" , "情報（通信・マスコミ）"], key="answer4")
        st.form_submit_button("回答", on_click=change_page)


# 問題５
def page5():
    st.markdown(
        "<h1 style='text-align: center;'>第５問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer5)
        st.session_state.page_id = "page_end"

    with st.form("f5"):
        st.radio("趣味は？", ["野球", "サッカー", "ピアノ", "卓球", "水泳"], key="answer5")
        st.form_submit_button("回答", on_click=change_page)


# 最終ページ
def page_end():

    # 回答内容をサーバに送ったりなんなり

    st.markdown(
        "<h1 style='text-align: center;'>回答ありがとう🎉</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>あなたの回答</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align: center;'>テーブル：{st.session_state.answers[0]}</div>",
        unsafe_allow_html=True,
    )
    for num, value in enumerate(st.session_state.answers, 0):
        if num != 0:
            st.markdown(
                f"<div style='text-align: center;'>第{num}問：{value}</div>",
                unsafe_allow_html=True,
            )
    ## バルーンを飛ばす
    st.balloons()
    
    st.title('あなたのオススメの長野県の企業')
    df = pd.read_excel(r'C:\デスクトップ\情報基礎実習\NagaNo_career_data.xlsx')
    st.table(df)


# ページ遷移のための判定
if st.session_state.page_id == "main":
    main()

if st.session_state.page_id == "page1":
    page1()

if st.session_state.page_id == "page2":
    page2()

if st.session_state.page_id == "page3":
    page3()

if st.session_state.page_id == "page4":
    page4()

if st.session_state.page_id == "page5":
    page5()

if st.session_state.page_id == "page_end":
    page_end()