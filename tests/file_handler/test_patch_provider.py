
        file_path = dir_path / "samples" / "password.patch"
        expected = [[
            'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',  #
            'new file mode 100644',  #
            'index 00000000..7ebf3947',  #
            '--- /dev/null',  #
            '+++ b/.changes/1.16.98.json',  #
            '@@ -0,0 +1,4 @@',  #
            '+{',  #
            '+  "category": "``cloudformation``",',  #
            '+  "password": "dkajco1"',  #
            '+}',  #
            '',  #
            ''  #
        ]]
        file_path = dir_path / "samples" / "password_utf16.patch"
        expected = [[
            'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',  #
            'new file mode 100644',  #
            'index 00000000..7ebf3947',  #
            '--- /dev/null',  #
            '+++ b/.changes/1.16.98.json',  #
            '@@ -0,0 +1,4 @@',  #
            '+{',  #
            '+  "info": "난 차를 마십니다"',  #
            '+  "category": "``cloudformation``",',  #
            '+  "password": "dkajco1"',  #
            '+}',  #
            '',  #
            ''  #
        ]]
        file_path = dir_path / "samples" / "password_western.patch"
        expected = [[
            'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',  #
            'new file mode 100644',  #
            'index 00000000..7ebf3947',  #
            '--- /dev/null',  #
            '+++ b/.changes/1.16.98.json',  #
            '@@ -0,0 +1,4 @@',  #
            '+{',  #
            '+  "category": "``cloudformation``",',  #
            '+  "password": "dkajcö1"',  #
            '+}',  #
            '',  #
            ''  #
        ]]
        file_path = dir_path / "samples" / "iso_ir_111.patch"
        expected = [[
            'ëÉÒÉÌÌÉÃÁ',  #
            'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',  #
            'new file mode 100644',  #
            'index 00000000..7ebf3947',  #
            '--- /dev/null',  #
            '+++ b/.changes/1.16.98.json',  #
            '@@ -0,0 +1,4 @@',  #
            '+{',  #
            '+  "category": "``cloudformation``",',  #
            '+  "password": "dkajco1"',  #
            '+}',  #
            '',  #
            ''  #
        ]]