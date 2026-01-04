-- Supabase SQL Editor에서 실행할 contacts 테이블 생성 SQL

CREATE TABLE contacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Row Level Security 활성화 (선택사항)
ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;

-- 모든 사용자가 읽기/쓰기 가능하도록 정책 추가 (개발용)
CREATE POLICY "Allow all operations" ON contacts
    FOR ALL
    USING (true)
    WITH CHECK (true);
