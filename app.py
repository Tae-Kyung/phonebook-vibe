import os
from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Supabase 클라이언트 초기화
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)


def get_contacts():
    """모든 연락처 조회 (Select)"""
    response = supabase.table('contacts').select('*').order('created_at', desc=True).execute()
    return response.data


def add_contact(name: str, phone: str):
    """연락처 추가 (Insert)"""
    response = supabase.table('contacts').insert({
        'name': name,
        'phone': phone
    }).execute()
    return response.data


@app.route('/')
def index():
    """메인 페이지 - 연락처 목록"""
    contacts = get_contacts()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add():
    """연락처 추가"""
    name = request.form.get('name')
    phone = request.form.get('phone')

    if name and phone:
        add_contact(name, phone)
        flash('연락처가 추가되었습니다.', 'success')
    else:
        flash('이름과 전화번호를 모두 입력해주세요.', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
